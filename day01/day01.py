with open('day01/input.txt') as input:
    lines = input.read().splitlines()
line=lines[0]
ns = [int(ch) for ch in line]

keep=[]

N=len(ns)
for i in range(len(ns)):
    if ns[i]==ns[(i+1) % N]:
        keep.append(ns[i])

answer1 = sum(keep)

keep=[]
for i in range(len(ns)):
    if ns[i]==ns[(i+int(N/2)) % N]:
        keep.append(ns[i])

answer2 = sum(keep)
print(answer1,answer2)