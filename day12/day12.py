from collections import defaultdict
answer1=-1
answer2=-1

with open("day12/input.txt",'r') as input:
    lines=input.read().splitlines()

progs=defaultdict(set)
for line in lines:
    prog, to = line.split(' <-> ',2)
    prog=int(prog)
    to=[int(i) for i in to.split(', ')]
    progs[prog]=progs[prog].union(to)
    for p in progs[prog]:
        progs[p].add(p)
    
def reachableFrom(frm,progs):
    visited=set()
    found=True
    while found:
        found=False
        for p in frm.difference(visited):
            frm=frm.union(progs[p])
            visited.add(p)
            found=True
    return frm

fromZero=reachableFrom(set([0]),progs)
answer1=len(fromZero)

groups=[fromZero]
while True:
    found=[i for x in groups for i in x]
    left = set(progs.keys()).difference(found)
    if not left: break
    left=list(left)[0]
    groups.append(reachableFrom(set([left]),progs))
answer2=len(groups)
print(answer1,answer2)
