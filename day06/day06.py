from collections import defaultdict
with open('day06/input.txt') as input:
    lines = input.readlines()

banks= {i:int(b) for i,b in enumerate(lines[0][:-1].split('\t'))}
print(banks)

def hash(banks):
    return tuple([i for i in banks.values()])

answer1,answer2=-1,-1
nbanks=len(banks)
repeated=False
seen=defaultdict(int)
i=0
while not repeated:
    h=hash(banks)
    seen[h]+=1
    if seen[h]>1:
        print(banks)
        print(i)
        answer1=i
        break
    maxb=max(banks, key=banks.get)
    val=banks[maxb]
    banks[maxb]=0
    for offset in range(1,val+1):
        banks[(maxb+offset)%nbanks]+=1    
    i+=1

repeated=False
seen=defaultdict(int)
i=0
while not repeated:
    h=hash(banks)
    seen[h]+=1
    if seen[h]>1:
        print(banks)
        print(i)
        answer2=i
        break
    maxb=max(banks, key=banks.get)
    val=banks[maxb]
    banks[maxb]=0
    for offset in range(1,val+1):
        banks[(maxb+offset)%nbanks]+=1    
    i+=1

print(answer1,answer2)