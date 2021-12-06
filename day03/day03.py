import math
input=289326

def locate(addr):
    if addr==1: return (0,0)
    ringw=int(math.sqrt(addr))
    if ringw%2==1 and addr==ringw**2: 
        return (-int(ringw/2),-int(ringw/2))
    ringw+=1+ringw%2
    hw=int(ringw/2)
    backstep=ringw**2-addr
    for i in range(ringw-1):
        if backstep==0:
            return (-hw,-hw+i)
        backstep-=1
    for i in range(ringw-1):
        if backstep==0:
            return (-hw+i,hw)
        backstep-=1
    for i in range(ringw-1):
        if backstep==0:
            return (hw,hw-i)
        backstep-=1
    for i in range(ringw-1):
        if backstep==0:
            return (hw-i,-hw)
        backstep-=1
    return -1

x,y=locate(input)
print(abs(x)+abs(y))


seq={(0,0):1}
done=False
while not done:
    x,y=locate(len(seq)+1)
    neigh = set(seq.keys()).intersection([(x-1,y-1), (x+1,y-1),
                                          (x-1,y),   (x+1,y),
                                          (x-1,y+1), (x+1,y+1),
                                          (x,y-1),   (x,y+1) ])
    seq[(x,y)]=sum([seq[p] for p in neigh])
    if seq[(x,y)]>input: done=True
    print((x,y),seq[(x,y)])
    x=x
