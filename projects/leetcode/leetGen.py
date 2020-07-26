import json
import os

with open('results.json') as f:
    data = json.load(f)
#print(data.keys())
problems = data['stat_status_pairs']
for p in problems:
    s = p['stat']
    fn = 'problems/{}_{}.py'.format(s['frontend_question_id'],s['question__title_slug'])
    if(os.path.exists(fn) == False):
        f= open(fn,"w+")
        #file = open(fn, 'w+')

totalSolved = data['num_solved']
easySolved = data['ac_easy']
mediumSolved = data['ac_medium']
hardSolved = data['ac_hard']
problems = data['stat_status_pairs']

solvedProblems = []
for p in problems:
    if(p['status'] is not None and p['status']=='ac'): solvedProblems.append(p)

results = {}
results['numSolved']=totalSolved
results['easy']=easySolved
results['medium']=mediumSolved
results['hard']=hardSolved
results['solvedProblems'] = []

#print(results)
base = 'https://github.com/ayellowman3/project-george/blob/master/projects/leetcode/problems/{}'
for p in solvedProblems:
    point = {}
    point['frontend_question_id'] = p['stat']['frontend_question_id']
    point['question__title'] = p['stat']['question__title']
    fn = '{}_{}.py'.format(p['stat']['frontend_question_id'],p['stat']['question__title_slug'])
    point['url'] = base.format(fn)
    results['solvedProblems'].append(point)
#print(results)
f = open("leetcodeResults.json", "w")
f.write(json.dumps(results))
f.close()
