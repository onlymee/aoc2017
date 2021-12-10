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

machine1={'ip': 0, 'regs': defaultdict(int), 'outq': [], 'inq': [], 'state': 'run'}
machine2={'ip': 0, 'regs': defaultdict(int), 'outq': [], 'inq': [], 'state': 'run'}
machine2['regs']['p']=1

print(machine2)

def run(machine,code):
    if machine['ip']>=len(code): 
        machine['state']='stopped'
        return machine
    inst=code[machine['ip']]
    if inst[0]=='snd':
        if isReg(inst[1]):
            op1=machine['regs'][inst[1]]
        else:
            op1=int(inst[1])
        machine['outq'].append(op1)
    elif inst[0]=='set':
        op1=inst[1]
        if isReg(inst[2]):
            op2=machine['regs'][inst[2]]
        else:
            op2=int(inst[2])
        machine['regs'][op1]=op2
    elif inst[0]=='add':
        op1=inst[1]
        if isReg(inst[2]):
            op2=machine['regs'][inst[2]]
        else:
            op2=int(inst[2])
        machine['regs'][op1]+=op2
    elif inst[0]=='mul':
        op1=inst[1]
        if isReg(inst[2]):
            op2=machine['regs'][inst[2]]
        else:
            op2=int(inst[2])
        machine['regs'][op1]*=op2
    elif inst[0]=='mod':
        op1=inst[1]
        if isReg(inst[2]):
            op2=machine['regs'][inst[2]]
        else:
            op2=int(inst[2])
        machine['regs'][op1]%=op2
    elif inst[0]=='rcv':
        #print(f"recv {machine['regs']['p']} {machine['inq']}")
        if len(machine['inq'])==0:
            machine['state']='wait'
            return machine
        machine['regs'][inst[1]]=machine['inq'][0]
        machine['inq']=machine['inq'][1:]
    elif inst[0]=='jgz':
        if isReg(inst[1]):
            op1=machine['regs'][inst[1]]
        else:
            op1=int(inst[1])
        if isReg(inst[2]):
            op2=machine['regs'][inst[2]]
        else:
            op2=int(inst[2])
        if op1>0:
            machine['ip']+=op2
            return machine
    machine['ip']+=1
    return machine

answer2=0
i,j=0,0
while machine1['state']=='run' or machine1['state']=='run':
    if machine1['state']=='run': 
        machine1=run(machine1,code)
        i+=1
    if machine2['state']=='run': 
        machine2=run(machine2,code)
        j+=1
    answer2+=len(machine2['outq'])
    machine1['inq'].extend(machine2['outq'])
    machine2['inq'].extend(machine1['outq'])
    #print(f"{machine1['inq']}     {machine2['inq']}")
    
    machine1['outq']=[]
    machine2['outq']=[]

    if machine1['inq'] and machine1['state']=='wait': machine1['state']='run'
    if machine2['inq'] and machine2['state']=='wait': machine2['state']='run'

print(answer1,answer2)
