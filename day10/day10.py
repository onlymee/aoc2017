from collections import defaultdict
with open('day10/input.txt') as input:
    lines = input.read().splitlines()

seq = [i for i in range(256)]
lengths = [int(i) for i in lines[0].split(',')]
#seq=[0,1,2,3,4]
#lengths=[3,4,1,5]
skip=0
pos=0

lseq=len(seq)
for length in lengths:
    if length>lseq:
        print('invalid')
        continue
    seq.extend(seq)
    seq=seq[:pos]+[i for i in reversed(seq[pos:pos+length])]+seq[pos+length:]
    seq=seq[lseq:pos+lseq]+seq[pos:lseq]
    pos=(pos+length+skip) % lseq
    skip+=1

answer1 = seq[0]*seq[1]
answer2 = -1 

print(answer1,answer2)