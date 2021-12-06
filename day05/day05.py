import re
with open('day05/input.txt') as input:
    lines = input.read().splitlines()

jumps = [int(i) for i in lines]
pos=0
step=0
while pos>=0 and pos<len(jumps):
    jmp=jumps[pos]
    jumps=jumps[0:pos]+[jmp+1]+jumps[pos+1:]
    pos+=jmp
    step+=1

answer1 = step
print(answer1)

jumps = [int(i) for i in lines]
#jumps = [0,3,0,1,-3]

pos=0
step=0
while pos>=0 and pos<len(jumps):
    jmp=jumps[pos]
    newjmp=jmp+1
    if jmp>=3:
        newjmp=jmp-1
    jumps=jumps[0:pos]+[newjmp]+jumps[pos+1:]
    #print(pos,jmp,newjmp,jumps)
    pos+=jmp
    step+=1

answer2 = step

print(answer1,answer2)