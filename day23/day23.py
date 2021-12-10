from collections import defaultdict
answer1=-1
answer2=-1

with open("day23/input.txt",'r') as input:
    lines=input.read().splitlines()

regs=defaultdict(int)
code = [line.split(' ') for line in lines]

def isReg(s):
    if len(s)==1 and ord(s[0]) >= ord('a') and ord(s[0]) <= ord('z'):
        return True
    return False

machine1={'ip': 0, 'regs': defaultdict(int), 'outq': [], 'inq': [], 'state': 'run'}

def run(machine,code):
    if machine['ip']>=len(code): 
        machine['state']='stopped'
        return machine
    inst=code[machine['ip']]
    if inst[0]=='set':
        op1=inst[1]
        if isReg(inst[2]):
            op2=machine['regs'][inst[2]]
        else:
            op2=int(inst[2])
        machine['regs'][op1]=op2
    elif inst[0]=='sub':
        op1=inst[1]
        if isReg(inst[2]):
            op2=machine['regs'][inst[2]]
        else:
            op2=int(inst[2])
        machine['regs'][op1]-=op2
    elif inst[0]=='mul':
        op1=inst[1]
        if isReg(inst[2]):
            op2=machine['regs'][inst[2]]
        else:
            op2=int(inst[2])
        machine['regs'][op1]*=op2
    elif inst[0]=='jnz':
        if isReg(inst[1]):
            op1=machine['regs'][inst[1]]
        else:
            op1=int(inst[1])
        if isReg(inst[2]):
            op2=machine['regs'][inst[2]]
        else:
            op2=int(inst[2])
        if op1!=0:
            machine['ip']+=op2
            return machine
    machine['ip']+=1
    return machine

answer2=0
i,j=0,0
nmul=0
while machine1['state']=='run':
    if machine1['state']=='run': 
        if machine1['ip']<len(code) and code[machine1['ip']][0]=='mul':
            nmul+=1
        machine1=run(machine1,code)
        i+=1
answer1=nmul
print(answer1,answer2)
