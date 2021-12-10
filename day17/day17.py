from collections import deque
answer1=-1
answer2=-1

input=314

buffer=[0]
pos=0
for i in range(2017):
    pos=(pos + input) % len(buffer)
    buffer = buffer[:pos+1]+[(i+1)]+buffer[pos+1:]
    pos+=1
    if i==2016:
        answer1=buffer[(pos+1)%len(buffer)]

pos=0
lenBuffer=1
for i in range(50000000):
    pos=(pos + input) % lenBuffer
    lenBuffer+=1
    if pos==0:
        answer2=i+1
    pos+=1

print(answer1,answer2)
