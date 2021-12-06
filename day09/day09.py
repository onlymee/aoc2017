from collections import defaultdict
with open('day09/input.txt') as input:
    lines = input.read()


score=0
accum=0
inGarbage=False
garbage=0
while lines:
    ch=lines[0]
    lines=lines[1:]

    if inGarbage:
        if ch=='!':
            lines=lines[1:]
        elif ch=='>':
            inGarbage=False
        else:
            garbage+=1
    else:
        if ch=='{':
            score+=1
        elif ch=='}':
            accum+=score
            score-=1
        elif ch=='<':
            inGarbage=True
    

answer1 = accum
answer2 = garbage

print(answer1,answer2)