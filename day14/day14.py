from collections import deque
from functools import reduce
answer1=-1
answer2=-1

input='xlqgujun'
#input='flqrgnkx'
def knotHash(str):
    seq = [i for i in range(256)]
    lengths = [ord(i) for i in str]+[17,31,73,47,23]
    skip=0
    pos=0
    lseq=len(seq)
    for round in range(64):
        for length in lengths:
            if length>lseq:
                print('invalid')
                continue
            seq.extend(seq)
            seq=seq[:pos]+[i for i in reversed(seq[pos:pos+length])]+seq[pos+length:]
            seq=seq[lseq:pos+lseq]+seq[pos:lseq]
            pos=(pos+length+skip) % lseq
            skip+=1

    hash=''
    for i in range(16):
        hash+=f'{reduce(lambda x,y: x^y,seq[i*16:][:16],0):08b}'
    return hash 

if knotHash('aoc2017')[:32] =='10100000110000100000000101110000':
    print('test passed')
else:
    print('test failed')
if knotHash('flqrgnkx-0')[:8] =='11010100':
    print('test passed')
else:
    print('test failed')


used={}
for i in range(128):
    hash=knotHash(f'{input}-{i}')
    for j,ch in enumerate(hash):
        if ch=='1': used[(i,j)]='#'
answer1=len(used)

def getAdj(pnt):
    x,y=pnt
    return set([
        (x+1,y),
        (x-1,y),
        (x,y+1),
        (x,y-1)
    ])

regions=[]
while used:
    pnt,ch=used.popitem()
    queue=deque([pnt])
    queue.extend(getAdj(pnt).intersection(used))
    region=[pnt]
    while queue:
        search=queue.popleft()
        if search not in used: continue
        region.append(search)
        del used[search]
        queue.extend(getAdj(search).intersection(used))
    if region: regions.append(region)
answer2=len(regions)

scope={}
for r in range(8):
    row=''
    for c in range(8):
        for n,region in enumerate(regions):
            if (r,c) in region:
                if n not in scope: scope[n]=len(scope)
        ch='.'
        for s in scope:
            if (r,c) in regions[s]: ch=chr(scope[s]+ord('A'))
        row+=ch
    print(row)
        


print(sum([len(i) for i in regions]))
print(answer1,answer2)
