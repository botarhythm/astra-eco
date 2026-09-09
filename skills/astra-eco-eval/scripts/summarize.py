"""Read explicitly supplied JSONL; descriptive statistics only, no API calls."""
import argparse
import json
import math
import statistics
from pathlib import Path

METRICS = ('input_tokens', 'output_tokens', 'duration_seconds', 'cost_usd')


def summarize(rows):
    groups, seen = {}, set()
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError('Each record must be an object')
        rid = row.get('run_id')
        if not isinstance(rid, str) or not rid or rid in seen:
            raise ValueError('Missing or duplicate run_id')
        seen.add(rid)
        if row.get('kind') not in ('task', 'evaluation'):
            raise ValueError('Invalid kind')
        if row.get('variant') not in ('baseline', 'eco'):
            raise ValueError('Invalid variant')
        if row.get('passed') is not None and type(row['passed']) is not bool:
            raise ValueError('passed must be boolean or null')
        for field in ('model', 'effort', 'skill_version'):
            if row.get(field) is not None and not isinstance(row[field], str):
                raise ValueError(field + ' must be string or null')
        for field in METRICS:
            value = row.get(field)
            if value is not None and (type(value) not in (int, float) or not math.isfinite(value) or value < 0):
                raise ValueError(field + ' must be finite nonnegative number or null')
            if value is not None and field.endswith('_tokens') and int(value) != value:
                raise ValueError('Token counts must be integral')
        key = tuple(row.get(k) for k in ('kind', 'variant', 'model', 'effort', 'skill_version'))
        groups.setdefault(key, []).append(row)
    result = []
    for key, records in groups.items():
        group = dict(zip(('kind', 'variant', 'model', 'effort', 'skill_version'), key))
        known = [r['passed'] for r in records if r.get('passed') is not None]
        group.update(n=len(records), quality_known=len(known), passed=sum(known),
                     pass_rate=sum(known) / len(known) if known else None)
        for field in METRICS:
            values = [r[field] for r in records if r.get(field) is not None]
            group[field] = dict(known=len(values), missing=len(records)-len(values),
                                median=statistics.median(values) if values else None,
                                minimum=min(values) if values else None,
                                maximum=max(values) if values else None,
                                observed_sum=sum(values) if values else None)
        complete = len(known) == len(records) and group['cost_usd']['missing'] == 0
        group['cost_per_pass_usd'] = group['cost_usd']['observed_sum'] / sum(known) if complete and sum(known) else None
        result.append(group)
    return dict(scope='descriptive_only_not_causal', runs=len(seen), groups=result)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('records', type=Path)
    args = parser.parse_args()
    try:
        with args.records.open(encoding='utf-8-sig') as stream:
            result = summarize(json.loads(line) for line in stream if line.strip())
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except (OSError, ValueError) as error:
        parser.exit(2, f'Invalid records: {error}\n')


if __name__ == '__main__':
    main()
