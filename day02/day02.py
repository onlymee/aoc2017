import re
with open('day02/input.txt') as input:
    lines = input.read().splitlines()


def findDivs(ns):
    ns.sort(reverse=True)
    while ns:
        t=ns.pop()
        pair = [i for i in ns if i%t==0]
        if pair:
            return int(pair[0]/t)


diffs=[]
divs=[]
for line in lines:
    ns = [int(i) for i in re.split('\s+',line)]
    diffs.append(max(ns)-min(ns))
    divs.append(findDivs(ns))

answer1 = sum(diffs)
answer2 = sum(divs)

print(answer1,answer2)