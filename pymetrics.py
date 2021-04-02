import json
import sys
import ast

# https://www.ccs.neu.edu/home/amislove/publications/Pymetrics-FAccT.pdf 

f = open('data.json')
json = json.load(f)

results = json['workflows'][0]
traits = results['traits']
numTraits = 0;
totalPercent = 0;

for x in traits:
	numTraits = numTraits+1
	totalPercent = totalPercent + x['score']

print("Average Score: " + str(totalPercent/numTraits) + "%")

f.close()