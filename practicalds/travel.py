from itertools import permutations 
cites=[[0, 10, 15, 20], [10, 0, 35, 25],[15, 35, 0, 30], [20, 25, 30, 0]]
citysize=4
c1=cites[0]
c2=cites[1]
c3=cites[2]
c4=cites[3]
possibleout=list(permutations([c2,c3,c4]))
finalpos=[]
for k in range(len(possibleout)):
    ob=list(possibleout[k])
    ob.insert(0,c1)
    finalpos.append(ob)
dist=[]
ways=len(finalpos)
pathwithweight=[]
for i in range(ways):
    ob=finalpos[i]
    for k in range(len(ob)):
        a=0
        obj=ob[k]
        for p in range(len(obj)):
            #print(obj[p])
            if p==0:
                a+=obj[1]
            elif p==1:
                a+=obj[2]
            elif p==2:
                a+=obj[3]
            elif p==3:
                a+=obj[0]
    dist.append([ob,a])

def minpath(paths):
    minu=[]
    for o in range(len(paths)):
        mins=paths[o]
        mi=mins[1]
        minu.append(mi)

    return minu
#print(paths[0])
print(minpath(dist))

# print(dist[path])    
# #print(dist)
