import json, sys
from detector import rank_records
if __name__ == '__main__':
    payload = json.load(sys.stdin)
    scores = rank_records(payload['train'], payload['test'])
    json.dump({'scores': scores}, sys.stdout, allow_nan=False, separators=(',', ':'))
    sys.stdout.write(chr(10))
