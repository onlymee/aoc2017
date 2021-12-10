answer1=-1
answer2=-1

with open("day24/input.txt",'r') as input:
    lines=input.read().splitlines()

bridges=[]
for line in lines:
    bridges.append([int(i) for i in line.split('/')])

def dfs(chain,bridges):
    st=chain[-1]
    avail=[(i,b) for i,b in enumerate(bridges) if st in b]
    if not avail:
        return sum(chain[1:-1])*2+chain[0]+chain[-1]
    res=[]
    for i,end in avail:
        end=end[1-end.index(st)]

        res.append(dfs(chain+[end],bridges[:i]+bridges[i+1:]))
    return max(res)
    
answer1=dfs([0],bridges)

def dfs2(chain,bridges):
    st=chain[-1]
    avail=[(i,b) for i,b in enumerate(bridges) if st in b]
    if not avail:
        return (len(chain),sum(chain[1:-1])*2+chain[0]+chain[-1])
    res=[]
    for i,end in avail:
        end=end[1-end.index(st)]

        res.append(dfs2(chain+[end],bridges[:i]+bridges[i+1:]))
    return max(res)
    
answer2=dfs2([0],bridges)[1]


print(answer1,answer2)
