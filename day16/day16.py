from collections import defaultdict, deque

answer1=-1
answer2=-1

with open("day16/input.txt",'r') as input:
    lines=input.read().splitlines()

moves=lines[0].split(',')
progs={i:chr(ord('a')+i) for i in range(16)}

def getOrder(progs):
    return ''.join(progs[i] for i in range(16))

def dance(progs,moves):
    for m in moves:
        if m[0]=='s':
            n=int(m[1:])
            progs={((i+n)%16):v for i,v in progs.items()}
        elif m[0]=='x':
            p1, p2 = m[1:].split('/')
            p1, p2 = int(p1), int(p2)
            progs[p1], progs[p2] = progs[p2], progs[p1]
        elif m[0]=='p':
            p1, p2 = m[1:].split('/')
            p1 = [k for k, v in progs.items() if v==p1][0]
            p2 = [k for k, v in progs.items() if v==p2][0]
            progs[p1], progs[p2] = progs[p2], progs[p1]
    return progs

progs=dance(progs,moves)
answer1 = getOrder(progs)

found=defaultdict(list)
progs={i:chr(ord('a')+i) for i in range(16)}
i=0
while True:
    order=getOrder(progs)
    found[order].append(i)
    if len(found[order])>1:
        div=found[order][1]-found[order][0]
        i=1000000000-(1000000000 % div)
        break
    progs=dance(progs,moves)
    i+=1
while i<1000000000:
    progs=dance(progs,moves)
    i+=1

answer2 = getOrder(progs)

print(answer1,answer2)
