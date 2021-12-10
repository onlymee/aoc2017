answer1=-1
answer2=-1

with open("day19/input.txt",'r') as input:
    lines=input.read().splitlines()

route={}
for r,row in enumerate(lines):
    for c,ch in enumerate(row):
        route[(r,c)]=ch

start=(0,lines[0].index('|'))

letters=''
done=False
r,c=start
dr,dc=(1,0)
steps=0
while not done:
    r,c=r+dr,c+dc
    steps+=1
    ch=route[(r,c)]
    chnext=route[(r+dr,c+dc)]
    if ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        letters+=ch
    elif ch in '|-':
        continue
    elif ch=='+' or chnext is None or chnext==' ':
        p1=(r-dc,c-dr)
        p2=(r+dc,c+dr)
        if route[p1]!=' ':
            dr,dc=(-dc,-dr)
        elif route[p2]!=' ':
            dr,dc=(dc,dr)
        else:
            done=True

        
answer1=letters
answer2=steps
print(answer1,answer2)
