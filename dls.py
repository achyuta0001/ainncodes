from collections import defaultdict

class Graph:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def dls(self,source,target,maxd):
        if source==target:
            return True
        if maxd<=0:
            return False
        for i in self.graph[source]:
            if(self.dls(i,target,maxd-1)):
                return True
        return False
    
g=Graph(9)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,3)
g.addEdge(1,4)
g.addEdge(2,5)
g.addEdge(2,6)
g.addEdge(3,7)
g.addEdge(3,8)
target=3
maxd=2
source=0

if g.dls(source,target,maxd)==True:
    print("reachable")
else:
    print("yoyo")