from collections import defaultdict
from functools import reduce
with open('day10/input.txt') as input:
    lines = input.read().splitlines()

seq = [i for i in range(256)]
lengths = [ord(i) for i in lines[0]]+[17,31,73,47,23]
#seq=[0,1,2,3,4]
#lengths=[3,4,1,5]
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
    hash+=f'{reduce(lambda x,y: x^y,seq[i*16:][:16],0):x}'

answer2 = hash

print(answer2)