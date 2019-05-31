from enum import Enum
import math

class Vertex:
    """
    Graph vertex: A graph vertex (node) with data
    """
    def __init__(self, c = None, p = None,dist = None,n = None):
        """
        Vertex constructor 
        @param color, parent, auxilary data1, auxilary data2
        """
        self.c = c
        self.p = p
        self.n = n
        self.dist = dist

class Graph:
    """
    Graph data: Any object which is used as a graph vertex data
    """
    def __init__(self, lv, le):
        """
        Data constructor
        @param A list of values assigned to object's attributes
        """
        self.lv = lv
        self.le = le

class Edge:
    """
    Graph data: Any object which is used as a graph vertex data
    """
    def __init__(self, src, dst, weight):
        """
        Data constructor
        @param A list of values assigned to object's attributes
        """
        self.src = src
        self.dst = dst
        self.weight = weight

class VertexColor(Enum):
        BLACK = 0
        GRAY = 127
        WHITE = 255

def makeGraph(lv,le):
	return Graph(lv,le)

def printGraph(G):
	for v in G.lv:
		print(v.n)
	for e in G.le:
		print(e.src.n + " " + e.dst.n + " - " + str(e.weight))

def getInDegrees(G):
	l = []
	for v in G.lv:
		cnt = 0
		for e in G.le:
			if e.dst.n == v.n:
				cnt = cnt + 1
		l.append(cnt)

	return l

def getOutDegrees(G):
	l = []
	for v in G.lv:
		cnt = 0
		for e in G.le:
			if e.src.n == v.n:
				cnt = cnt + 1
		l.append(cnt)

	return l

def initializeSingleSource(G,s):
	for v in G.lv:
		v.dist = math.inf
		v.p = None
	s.dist = 0

def relax(u,v,w):
	if v.dist > u.dist + w:
		v.dist = u.dist + w
		v.p = u

def bellmanFord(G,s):
	initializeSingleSource(G,s)
	for i in range(0,len(G.lv)):
		for e in G.le:
			relax(e.src, e.dst, e.weight)
	for e in G.le:
		if e.dst.dist > e.src.dist + e.weight:
			return False
	return True

def getEdge(G,u,v):
	for e in G.le:
		if e.src == u and e.dst == v:
			return e
	return None

def shortestPath(G,s,v):
	bellmanFord(G,s)
	l = []
	duzina = 0
	a = v
	while a is not None:
		l.append(a.n)
		if a.p != None:
			duzina = duzina + getEdge(G,a.p,a).weight
		a = a.p
	l.reverse()
	return l, duzina


def updateEdge(G,s,v,weight):
	edge = getEdge(G,s,v)
	if edge == None:
		e = Edge(s,v,weight)
		G.le.append(e)
	else:
		edge.weight = weight

#********************************************
a = Vertex(n = "a")
b = Vertex(n = "b")
c = Vertex(n = "c")
d = Vertex(n = "d")
e = Vertex(n = "e")
f = Vertex(n = "f")
g = Vertex(n = "g")
lv = [a,b,c,d,e,f,g]
ab = Edge(a,b,8)
ac = Edge(a,c,6)
bd = Edge(b,d,10)
cd = Edge(c,d,15)
ce = Edge(c,e,9)
de = Edge(d,e,14)
df = Edge(d,f,4)
ef = Edge(e,f,13)
eg = Edge(e,g,17)
fg = Edge(f,g,7)
le = [ab,ac,bd,cd,ce,de,df,ef,eg,fg]

G = makeGraph(lv,le)
printGraph(G)
l1 = getInDegrees(G)
l2 = getOutDegrees(G)

for i in l1:
	print(i)

print("\n")

for i in l2:
	print(i)

print("\n")
l,d = shortestPath(G,a,g)

print(d)
for i in l:
	print(i)

updateEdge(G,b,c,-4)
printGraph(G)