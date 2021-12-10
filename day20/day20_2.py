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
    clean=[int(i) for i in re.sub(r'[pva= <>]','',line).split(',')]
    p.append(clean[0:3])
    v.append(clean[3:6])
    a.append(clean[6:9])
    i+=1

pos=np.matrix(p)
vel=np.matrix(v)
acc=np.matrix(a)

i=0
while i<100:
    vel=np.add(vel,acc)
    pos=np.add(pos,vel)

    p,inv,counts=np.unique(pos, axis=0, return_counts=True,return_inverse=True)
    keep=[i for i,inv in enumerate(inv) if counts[inv]==1]
    pos=pos[keep,]
    vel=vel[keep,]
    acc=acc[keep,]

    #print(destroy)
    #np.delete(pos,destroy, axis=0)
    #np.delete(vel,destroy, axis=0)
    #np.delete(acc,destroy, axis=0)
    i+=1

print(np.size(pos,axis=0))