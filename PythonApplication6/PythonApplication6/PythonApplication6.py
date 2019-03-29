import random
class T:
    def __init__(self, root = None, nodesNum = 1):
       self.root = root
       self.nodesNum = nodesNum

class Node:
    """
    Tree node: left child, right child and data
    """
    def __init__(self, p = None, l = None, r = None, d = None):
        """
        Node constructor 
        @param A node data object
        """
        self.parent = p
        self.left = l
        self.right = r
        self.data = d

class Data:
    """
    Tree data: Any object which is used as a tree node data
    """
    def __init__(self, val1, val2, keyval):
        """
        Data constructor
        @param A list of values assigned to object's attributes
        """
        self.a1 = val1
        self.a2 = val2
        self.key = keyval

def treeInsert(T,z):
    y = None
    x = T.root
    while x != None:
        y = x
        if z.data.key < x.data.key:
            x = x.left
        else:
            x = x.right

    z.parent = y
    if y == None:
        T.root = z
    elif z.data.key < y.data.key:
        y.left = z
    else:
        y.right = z
    
    T.nodesNum += 1

def inorderTreeWalk1(l,x):
    if x != None:
        inorderTreeWalk1(l,x.left)
        l.append(x.data.key)
        inorderTreeWalk1(l,x.right)

def inorderTreeWalk(x):
    if x != None:
        inorderTreeWalk(x.left)
        print(x.data.key)
        inorderTreeWalk(x.right)

def treeSearch(x,k):
    if x == None or k == x.data.key:
        return x
    if k < x.data.key:
        return treeSearch(x.left,k)
    else:
        return treeSearch(x.right,k)

def iterativeTreeSearch(x,k):
    while x != None and k != x.data.key:
        if k < x.data.key:
            x = x.left
        else:
            x = x.right
    return x

def treeMinimum(x):
    while x.left != None:
        x = x.left
    return x

def treeMaximum(x):
    while x.right != None:
        x = x.right
    return x

def treeSuccessor(x):
    if x.right != None:
        return treeMinimum(x.right)
    y = x.parent
    while y!=None and x == y.right:
        x = y
        y = y.parent
    return y

def transplant(T,u,v):
    if u.parent == None:
        T.root = v
    elif u == u.parent.left:
        u.parent.left = v
    else:
        u.parent.right = v

    if v != None:
        v.parent = u.parent

def treeDelete(T,z):
    if z.left == None:
        transplant(T,z,z.right)
    elif z.right == None:
        transplant(T,z,z.left)
    else:
        y = treeMinimum(z.right)
        if y.parent != z:
            transplant(T,y,y.right)
            y.right = z.right
            y.right.parent = y
        transplant(T,z,y)
        y.left = z.left
        y.left.parent = y
    T.nodesNum -= 1

d1 = Data(1,2,1)
#print(d1.a1, d1.a2, d1.key)
d2 = Data(3,4,2)
d3 = Data(5,6,3)
d4 = Data(7,8,4)
d5 = Data(9,10,5)

n1 = Node(d = d1)
n2 = Node(d = d2)
n3 = Node(d = d3)
n4 = Node(d = d4)
n5 = Node(d = d5)

tree = T(root = n1)
treeInsert(tree,n2)
treeInsert(tree,n4)
treeInsert(tree,n5)
treeInsert(tree,n3)
print("\nBroj cvorova: ")
print(tree.nodesNum)
print("\nInorder Tree Walk: ")
inorderTreeWalk(tree.root)
#n5 = iterativeTreeSearch(tree.root,3)
n5 = treeSearch(tree.root, 3)
print("\nNadjeni cvor sa kljucem 3 je: ")
print(n5.data.a1, n5.data.a2)

n5 = treeMinimum(tree.root)
print("\nNajmanji element je: ")
print(n5.data.a1,n5.data.a2)

n5 = treeMaximum(tree.root)
print("\nNajveci element je: ")
print(n5.data.a1,n5.data.a2)

n5 = treeSuccessor(n3)
print("\nTree Successor od n3 je: ")
print(n5.data.a1,n5.data.a2)

print("\nBrisanje cvora n3...")
treeDelete(tree,n3)
if treeSearch(tree.root,n3.data.key) == None:
    print("Cvor n3 je uspesno izbrisan! Novi broj cvorova: " + str(tree.nodesNum))
else:
    print("Cvor n3 nije izbrisan!")


tree = T()
list = random.sample(range(0,100),50)
print("\n\nLista: ")
print(list)
for i in range(len(list)):
    treeInsert(tree,Node(d = Data(random.randint(0,100), random.randint(0,100),list[i])))
print("\nSortirana lista")
sorted = []
inorderTreeWalk1(sorted,tree.root)
print(sorted)