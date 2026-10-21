"""Read-only, offline retrieval. Python 3 standard library only."""
from pathlib import Path
import argparse, csv, json, sys

ROOT = Path(__file__).resolve().parents[1]

def retrieve(kind, query, file_prefix='', limit=10):
    if limit < 1:
        raise ValueError('limit must be positive')
    results = []
    if kind == 'term':
        with (ROOT/'assets/terms.csv').open(encoding='utf-8-sig', newline='') as f:
            for i, row in enumerate(csv.DictReader(f), 1):
                if query.casefold() in '\n'.join(row.values()).casefold():
                    results.append({'row': i, **row})
    else:
        index = json.loads((ROOT/'references/record-index.json').read_text(encoding='utf-8'))
        cache = {}
        for item in index:
            if file_prefix and not Path(item['file']).name.startswith(file_prefix):
                continue
            path = (ROOT/item['file']).resolve()
            if ROOT not in path.parents:
                raise ValueError('Index path outside skill')
            if path not in cache:
                cache[path] = path.read_text(encoding='utf-8-sig').splitlines()
            lines = cache[path]
            body = '\n'.join(lines[item['start_line']-1:item['end_line']])
            match = item['id'].casefold() == query.casefold() if kind == 'record' else query.casefold() in body.casefold()
            if match:
                results.append({**item, 'content':body})
    return {'kind':kind,'query':query,'matches':len(results),'returned':min(limit,len(results)), 'truncated':len(results)>limit,'results':results[:limit]}

if __name__ == '__main__':
    if hasattr(sys.stdout,'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('kind',choices=['record','search','term'])
    parser.add_argument('query')
    parser.add_argument('--file',default='',help='Knowledge filename prefix')
    parser.add_argument('--limit',type=int,default=10)
    args=parser.parse_args()
    if args.limit < 1:
        parser.error('--limit must be positive')
    print(json.dumps(retrieve(args.kind,args.query,args.file,args.limit),ensure_ascii=False,indent=2))
