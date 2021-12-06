from collections import defaultdict
with open('day11/input.txt') as input:
    lines = input.read().splitlines()

moves = lines[0].split(',')

x,y=0,0
maxdist=0
for move in moves:
    if move=='ne':
        x+=1
    elif move=='n':
        x+=1
        y+=1
    elif move=='nw':
        x-=1
        y+=1
    elif move=='sw':
        x-=1
    elif move=='s':
        x-=1
        y-=1
    elif move=='se':
        x+=1
        y-=1
    if max(x,y)>maxdist: maxdist=max(x,y)
    
    
answer1,answer2=max(x,y),maxdist
print(answer1,answer2)