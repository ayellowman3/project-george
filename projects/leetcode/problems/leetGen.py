import json
import os

with open('results.json') as f:
  data = json.load(f)
print(data.keys())
problems = data['stat_status_pairs']
for p in problems:
    s = p['stat']
    fn = 'problems/{}_{}.py'.format(s['question_id'],s['question__title_slug'])
    if(os.path.exists(fn) == False):
        file = open(fn, 'w+')

print(json.dumps(data, indent = 2))
