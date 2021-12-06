from collections import defaultdict
with open('day08/input.txt') as input:
    lines = input.read().splitlines()

instr=[]
for line in lines:
    bits = line.split(' ')
    reg=bits[0]
    op=bits[1]
    val=int(bits[2])
    creg=bits[4]
    cop=bits[5]
    cval=int(bits[6])
    instr.append((reg,op,val,creg,cop,cval))

def testCond(cop,val1,val2):
    return eval(f'{val1} {cop} {val2}')


def doInstr(inst,regs):
    reg,op,val,creg,cop,cval = inst
    if creg not in regs: regs[creg]=0
    if reg not in regs: regs[reg]=0
    if testCond(cop,regs[creg],cval):
        if op=='inc':
            regs[reg]+=val
        elif op=='dec':
            regs[reg]-=val
        else:
            raise Error('Panic')
    return regs[reg]

regs={}
maxmax=-1000000
for inst in instr:
    val = doInstr(inst,regs)
    if val>maxmax: maxmax=val

print(regs)
answer1 = max(regs.values())
answer2 = maxmax

print(answer1,answer2)