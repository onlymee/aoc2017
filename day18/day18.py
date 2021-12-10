from collections import defaultdict
answer1=-1
answer2=-1

with open("day18/input.txt",'r') as input:
    lines=input.read().splitlines()

regs=defaultdict(int)
code = [line.split(' ') for line in lines]

def isReg(s):
    if len(s)==1 and ord(s[0]) >= ord('a') and ord(s[0]) <= ord('z'):
        return True
    return False

sound=-1
ip=0
while True:
    if ip>=len(code): break
    inst=code[ip]
    if inst[0]=='snd':
        if isReg(inst[1]):
            op1=regs[inst[1]]
        else:
            op1=int(inst[1])
        sound=op1        
    elif inst[0]=='set':
        op1=inst[1]
        if isReg(inst[2]):
            op2=regs[inst[2]]
        else:
            op2=int(inst[2])
        regs[op1]=op2
    elif inst[0]=='add':
        op1=inst[1]
        if isReg(inst[2]):
            op2=regs[inst[2]]
        else:
            op2=int(inst[2])
        regs[op1]+=op2
    elif inst[0]=='mul':
        op1=inst[1]
        if isReg(inst[2]):
            op2=regs[inst[2]]
        else:
            op2=int(inst[2])
        regs[op1]*=op2
    elif inst[0]=='mod':
        op1=inst[1]
        if isReg(inst[2]):
            op2=regs[inst[2]]
        else:
            op2=int(inst[2])
        regs[op1]%=op2
    elif inst[0]=='rcv':
        if isReg(inst[1]):
            op1=regs[inst[1]]
        else:
            op1=int(inst[1])
        if op1!=0:
            print(f'Recovered: {sound}')       
            answer1=sound
            break
    elif inst[0]=='jgz':
        if isReg(inst[1]):
            op1=regs[inst[1]]
        else:
            op1=int(inst[1])
        if isReg(inst[2]):
            op2=regs[inst[2]]
        else:
            op2=int(inst[2])
        if op1>0:
            ip+=op2
            continue
    ip+=1

print(answer1,answer2)
