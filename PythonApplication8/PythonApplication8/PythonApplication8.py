class Data:
    """
    Tree data: Any object which is used as a tree node data
    """
    def __init__(self, val1, val2):
        """
        Data constructor
        @param A list of values assigned to object's attributes
        """
        self.data = val1
        self.key = val2

def hash_function(T,k):
	return k % len(T)

def Chained_Hash_Insert(T,x):
	T[hash_function(T,x.key)].insert(0,x)

def Chained_Hash_Search(T,k):
	ind = 0
	for i in T[hash_function(T,k.key)]:
		if(i.data == k.data):
			return ind
		ind = ind + 1

	return None

def Chained_Hash_Delete(T,x):
	T[hash_function(T,x.key)].remove(x)

def Chained_Hash_Print(T):
	for i in range(len(T)):
		for j in T[i]:
			print(str(j.data) + " " + str(j .key))

T = []

for i in range(10):
	T.append([])

d1 = Data("Milos",1)
d3 = Data("Ilija", 3)
d2 = Data("Ivan",3)
d4 = Data("Ana",2)

Chained_Hash_Insert(T,d1)
Chained_Hash_Insert(T,d2)
Chained_Hash_Insert(T,d3)
Chained_Hash_Insert(T,d4)

print("Search test for Ivan,3")
print(str(hash_function(T,d2.key)) + " " + str(Chained_Hash_Search(T,d2)))

print("\n")
Chained_Hash_Print(T)

print("\n\nDelete test for Ivan,3\n")

Chained_Hash_Delete(T,d2)

Chained_Hash_Print(T)

print("\nSearch test for Ivan,3")
print(str(hash_function(T,d2.key)) + " " + str(Chained_Hash_Search(T,d2)))

print("\n")