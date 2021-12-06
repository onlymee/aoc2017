from collections import defaultdict
with open('day07/input.txt') as input:
    lines = input.read().splitlines()

programs={}
for line in lines:
    stack = line.split(' -> ')
    item,weight = stack[0].split(' ')
    weight = int(weight[1:-1])

    supports=[]
    if len(stack)>1:
        supports = stack[1].split(', ')

    programs[item]=(weight,supports)

supported=[x for p,(w,s) in programs.items() for x in s]
answer1 = bottom = list(set(programs.keys()).difference(supported))[0]

def makeBalance(prog):
    weight, supported = programs[prog]
    if not supported: return weight
    towers=[]
    for p in supported:
        towers.append(makeBalance(p))
    uniq = set(towers)
    if len(uniq)==1: return weight+sum(towers)
    heavy,problem,target=0,'',0
    for w in uniq:
        if towers.count(w)==1:
            heavy=w
            problem=supported[towers.index(w)]
        else:
            target=w
    print(programs[problem][0]-(heavy-target))
    exit()
        
makeBalance(bottom)

answer2 = -1 

print(answer1,answer2)