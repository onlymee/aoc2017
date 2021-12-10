from collections import defaultdict
import numpy as np
import re
answer1=-1
answer2=-1

with open("day20/input.txt",'r') as input:
    lines=input.read().splitlines()

p,v,a,d=[],[],[],[]

i=0
for line in lines:
    clean=[int(i) for i in re.sub(r'[pva= <>]+','',line).split(',')]
    p.append(clean[0:3])
    v.append(clean[3:6])
    a.append(clean[6:9])
    i+=1

pos=np.matrix(p)
vel=np.matrix(v)
acc=np.matrix(a)

i=0
while i<1000000:
    vel=np.add(vel,acc)
    pos=np.add(pos,vel)

    dist=np.sum(np.abs(pos), axis=1)
    nearest=np.argmin(dist,0)
    if i%100==0: print(nearest[0,0],i)
    i+=1

print(nearest[0,0])