import math
debug=True
b,c=57,57
if debug:
    b=b*100+100000
    c=b+17000
h=0
print(b,c)
for x in range(b,c+1,17):
    for d in range(2,b):
        if x%d==0:
            h+=1
            break

print(h)
