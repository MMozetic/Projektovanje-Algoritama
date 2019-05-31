from enum import Enum	
import queue
import math

class Vertex:
    """
    Graph vertex: A graph vertex (node) with data
    """
    def __init__(self, c = None, p = None, d1 = None, d2 = None, l = None,dist = None,n = None):
        """
        Vertex constructor 
        @param color, parent, auxilary data1, auxilary data2
        """
        self.c = c
        self.p = p
        self.d1 = d1
        self.d2 = d2
        self.list = l
        self.n = n
        self.dist = dist

class Data:
    """
    Graph data: Any object which is used as a graph vertex data
    """
    def __init__(self, val1, val2):
        """
        Data constructor
        @param A list of values assigned to object's attributes
        """
        self.a1 = val1
        self.a2 = val2

class VertexColor(Enum):
        BLACK = 0
        GRAY = 127
        WHITE = 255		


def ispisSuseda(v):
	print("\n")
	for i in v.list:
		print(i.n)
		
def ispisVeza(v):
	print("\n")
	for l in v.list:
		print("E(" + str(v.n) + "," + str(l.n) + ")")

def BFS(G,s):
	for u in G:
		if u == s:
			continue
		u.c = VertexColor.WHITE
		u.dist = math.inf
		u.p = None
	s.c = VertexColor.GRAY
	s.dist = 0
	s.p = None
	q = queue.Queue()
	q.put(s)
	while q.empty() != True:
		u = q.get()
		for v in u.list:
			if v.c == VertexColor.WHITE:
				v.c = VertexColor.GRAY
				v.dist = u.dist + 1
				v.p = u
				q.put(v)
		u.c = VertexColor.BLACK

def printPath(G,s,v):
	if v == s:
		print(s.n)
	elif v.p == None:
		print("No path from " + s.n + " to " + v.n)
	else:
		printPath(G,s,v.p)
		print(v.n)

v1 = Vertex(c=VertexColor.WHITE, d1=1, d2=1,n=1)
v2 = Vertex(c=VertexColor.WHITE, d1=2, d2=2,n=2)
v3 = Vertex(c=VertexColor.WHITE, d1=3, d2=3,n=3)
v4 = Vertex(c=VertexColor.WHITE, d1=4, d2=4,n=4)
v5 = Vertex(c=VertexColor.WHITE, d1=5, d2=5,n=5)

l1 = [v2, v5]
l2 = [v1, v5, v3, v4]
l3 = [v2, v4]
l4 = [v2, v5, v3]
l5 = [v4, v1, v2]

v1.list = l1
v2.list = l2
v3.list = l3
v4.list = l4
v5.list = l5

G = [v1,v2,v3,v4,v5]

for v in G:
	ispisSuseda(v)

for v in G:
	ispisVeza(v)


print("\n************************************\n")

s = Vertex(c=VertexColor.WHITE, d1=1, d2=1,n="s",dist = 0)
v = Vertex(c=VertexColor.WHITE, d1=1, d2=1,n="v", dist = math.inf)
r = Vertex(c=VertexColor.WHITE, d1=1, d2=1,n="r", dist = math.inf)
w = Vertex(c=VertexColor.WHITE, d1=1, d2=1,n="w", dist = math.inf)
t = Vertex(c=VertexColor.WHITE, d1=1, d2=1,n="t", dist = math.inf)
x = Vertex(c=VertexColor.WHITE, d1=1, d2=1,n="x", dist = math.inf)
u = Vertex(c=VertexColor.WHITE, d1=1, d2=1,n="u", dist = math.inf)
y = Vertex(c=VertexColor.WHITE, d1=1, d2=1,n="y", dist = math.inf)

G = [s,v,r,w,t,x,u,y]

sl = [r, w]
vl = [r]
rl = [s,v]
wl = [s,t,x]
tl = [w,x,u]
xl = [w,t,u,y]
ul = [t,x,y]
yl = [u,x]

s.list = sl
v.list = vl
r.list = rl
w.list = wl
t.list = tl
x.list = xl
u.list = ul
y.list = yl

BFS(G,s)

for v in G:
	print(v.n + " " + str(v.dist))

for v in G:
	print("\n")
	printPath(G,s,v)
