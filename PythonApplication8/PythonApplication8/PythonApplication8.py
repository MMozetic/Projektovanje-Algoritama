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

def hash_function1(T,k,i):
	return (hash_function(T,k)+i)%len(T)

def Hash_Insert(T,k):
	i = 0
	while i!=len(T):
		j = hash_function1(T,k.key,i)
		if T[j] == None or T[j] == "Smece":
			T[j] = k
			return j
		else:
			i = i + 1

	return None

def Hash_Search(T,k):
	i = 0
	j = hash_function1(T,k.key,i)
	while T[j] != None and i != len(T):
		j = hash_function1(T,k.key,i)
		if T[j] == k:
			return j
		i = i + 1

	return None

def Hash_Delete(T,k):
	T[Hash_Search(T,k)] = "Smece"

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

print("\n\n\n")

print("Open addressing: \n")

T1 = []
for i in range(10):
	T1.append(None)

d1 = Data("Milos",1)
d3 = Data("Ilija", 3)
d2 = Data("Ivan",3)
d4 = Data("Ana",2)

Hash_Insert(T1,d1)
Hash_Insert(T1,d2)
Hash_Insert(T1,d3)
Hash_Insert(T1,d4)

for i in T1:
	if(i == None):
		continue
	print(str(i.data) + " " + str(i.key))

print("\nSearch test for Ilija,3")
print("Index is " + str(Hash_Search(T1,d3)))

print("\nDelete test for Ivan,3")
Hash_Delete(T1,d2)
for i in T1:
	if(i == None):
		continue
	if(i == "Smece"):
		print("Smece")
		continue
	print(str(i.data) + " " + str(i.key))

print("\nSearching for Ivan,3")
if(Hash_Search(T1,d2) == None):
	print("Ivan,3 doesn't exist")
else:
	print("Ivan,3 exists")

print("\nSearching for Ilija,3")
if(Hash_Search(T1,d3) == None):
	print("Ilija,3 doesn't exist")
else:
	print("Ilija,3 exists")

print("\nInserting Ivan,3 again")
Hash_Insert(T1,d2)
for i in T1:
	if(i == None):
		continue
	if(i == "Smece"):
		print("Smece")
		continue
	print(str(i.data) + " " + str(i.key))

print("\n")