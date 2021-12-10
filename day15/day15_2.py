answer1=-1
answer2=-1

with open("day15/input.txt",'r') as input:
    lines=input.read().splitlines()

A=722
B=354

#A=65
#B=8921

div=2147483647
facA=16807
facB=48271
facA1000=(facA**1000)%div
facB1000=(facB**1000)%div


def genA(n):
    return (n*facA) % div
def genB(n):
    return (n*facB) % div
def genA1000(n):
    return (n*facA1000) % div
def genB1000(n):
    return (n*facB1000) % div

judge=0
for i in range(5000000):
    while True:
        A=genA(A)
        if A%4==0:break
    while True:
        B=genB(B)
        if B%8==0:break
    if (A ^ B) & 65535 == 0: 
        judge+=1
        print(f'{A&65535:016b}')
        print(f'{B&65535:016b}')
        print('')

answer1=judge
print(answer1,answer2)
