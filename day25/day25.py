from collections import defaultdict

from collections import defaultdict
answer1=-1
answer2=-1

with open("day25/input.txt",'r') as input:
    lines=input.read().splitlines()

startState=lines[0][-2]
steps=int(lines[1].split(' ')[5])
i=3
trans={}
while i<len(lines):
    state=lines[i][-2]
    write0=int(lines[i+2][22:-1])
    move0=-1
    if lines[i+3][27:-1]=='right': 
        move0=1
    next0=lines[i+4][26:-1]
    write1=int(lines[i+6][22:-1])
    move1=-1
    if lines[i+7][27:-1]=='right': 
        move1=1
    next1=lines[i+8][26:-1]
    trans[state]=((write0,move0,next0),(write1,move1,next1))
    i+=10

print(trans)
tape=defaultdict(int)
cursor=0
state=startState

for i in range(steps):
    w,m,n = trans[state][tape[cursor]]
    tape[cursor]=w
    cursor+=m
    state=n

answer1=list(tape.values()).count(1)

print(answer1,answer2)
