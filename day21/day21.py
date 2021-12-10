answer1=-1
answer2=-1

with open("day21/input.txt",'r') as input:
    lines=input.read().splitlines()

def flip(patch):
    sz=patch.count('/')+1
    if sz==2:
        return ''.join([patch[i] for i in [1,0,2,4,3]])
    if sz==3:
        return ''.join([patch[i] for i in [2,1,0,3,6,5,4,7,10,9,8]])

def rotate(patch):
    sz=patch.count('/')+1
    if sz==2:
        return ''.join([patch[i] for i in [1,4,2,0,3]])
    if sz==3:
        return ''.join([patch[i] for i in [2,6,10,3,1,5,9,7,0,4,8]])

edits={}
for line in lines:
    l,r = line.split(' => ')

    pnts=[]
    sz=r.count('/')+1
    i,j=0,0
    for ch in r:
        if ch=='/':
            j+=1
            i=0
            continue
        if ch=='#': pnts.append((i,j))
        i+=1
    edits[l]=pnts

#Add missing rotations/flips
origl=list(edits.keys())
for l in origl:
    pnts=edits[l]
    for i in range(4):
        if not l in edits: edits[l]=pnts
        l=rotate(l)
    l=flip(l)
    for i in range(4):
        if not l in edits: edits[l]=pnts
        l=rotate(l)


def getPatch(pnt,mp,n=2):
    r,c=pnt
    trace=''
    for dr in range(n):
        for dc in range(n):
            ch='.'
            if (r+dr,c+dc) in mp:
                ch='#'
            trace+=ch
        trace+='/'
    return trace[:-1]
            
def step(mp,sz,edits):
    newmp={}
    if sz%2==0:
        d=2
    elif sz%3==0:
        d=3
    else:
        print('error')
        exit(1)
    
    dsz=int(sz/d)    
    for r in range(0,dsz):
        for c in range(0,dsz):
            patch=getPatch((r*d,c*d),mp,d)
            for dr,dc in edits[patch]:
                newmp[(r*(d+1)+dr,c*(d+1)+dc)]='#'
    return newmp,int(sz/d*(d+1))


sz=3
mp={(0,1):'#',(1,2):'#',(2,0):'#',(2,1):'#',(2,2):'#'}

for i in range(5):
    mp,sz=step(mp,sz,edits)        

answer1=len(mp)
for i in range(13):
    mp,sz=step(mp,sz,edits)        
answer2=len(mp)

print(answer1,answer2)
