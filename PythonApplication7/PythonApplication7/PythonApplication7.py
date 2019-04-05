def insertion_sort(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j - 1
        while(i>=0 and A[i].freq>key.freq):
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key

class Element:
    def __init__(self, val1 = None, val2 = None,p = None):
        """
        Data constructor
        @param A list of values assigned to object's attributes
        """
        self.value = val1
        self.freq = val2
        self.parent = p

class Node:
    """
    Tree node: left child, right child and data
    """
    def __init__(self, l = None, r = None, f = None, d = None, p = None):
        """
        Node constructor 
        @param A node data object
        """
        self.left = l
        self.right = r
        self.freq = f
        self.value = d
        self.parent = p

def getHistogram(list):
    dict = {}
    output = []
    for i in list:
        if i not in dict.keys():
            dict[i] = 1
        else:
            dict[i] += 1

    for v,f in dict.items():
        output.append(Element(v,f))

    return output

def getMinFreqElem(list):
    return list[0]

def removeElem(list):
    list.remove(list[0])

def makeNewElem(e1,e2):
    n = Node()
    n.freq = e1.freq + e2.freq
    if e1.freq < e2.freq:
        n.left = e1
        n.right = e2
    e1.parent = n
    e2.parent = n

    return n

def putElem(l,e):
    l.append(e)
    insertion_sort(l)

def getEncVal(list, el):
    res = []
    e = list[0]
    while e.value == None:
        if el.freq <= e.freq/2:
            e = e.left
            res.append(0)
        else:
            e = e.right
            res.append(1)

    return res

input5 = ['a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'd', 'd', 'e', 'e', 'f']
print(input5)
output = getHistogram(input5)
print("\n")
insertion_sort(output)
for el in output:
    print(el.value, el.freq)

while(len(output)>1):
    e1 = getMinFreqElem(output)
    removeElem(output)
    e2 = getMinFreqElem(output)
    removeElem(output)

    n = makeNewElem(e1,e2)
    putElem(output, n)
    print("\n")
    for el in output:
        print(el.value, el.freq)

e1 = Element('f', 1)
print(getEncVal(output, e1))