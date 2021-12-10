answer1=-1
answer2=-1

with open("day13/input.txt",'r') as input:
    lines=input.read().splitlines()

layers={}
severity=0
for line in lines:
    l,d = [int(i) for i in line.split(': ',1)]
    layers[l]=d
    if l % ((d-1)*2)==0:
        severity+=l*d
answer1=severity

delay=1
while True:
    caught=False
    for l,d in layers.items():
        if (l+delay) % ((d-1)*2)==0:
            caught=True
            break
    if not caught:
        answer2=delay
        break
    delay+=1

answer2=delay


print(answer1,answer2)
