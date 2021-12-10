answer1=-1
answer2=-1

with open("day22/input.txt",'r') as input:
    lines=input.read().splitlines()

mp={}
for r,row in enumerate(lines):
    for c,ch in enumerate(row):
        if ch=='#': mp[(r,c)]=ch

r,c=(int(len(lines)/2), int(len(lines[0])/2))
dr,dc=-1,0

infected=0

for i in range(10000000):
    if (r,c) in mp:
        ch=mp[(r,c)]
        if ch=='W':
            infected+=1
            mp[(r,c)]='#'
        elif ch=='#':
            mp[(r,c)]='F'
            dr,dc=(dc,-dr)
        elif ch=='F':
            dr,dc=(-dr,-dc)
            del mp[(r,c)]
    else:
        dr,dc=(-dc,dr)
        mp[(r,c)]='W'
    r,c=r+dr,c+dc

answer1=infected
print(answer1,answer2)
