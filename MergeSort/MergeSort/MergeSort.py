from math import inf
import random
import time

def random_list(l,r, size):
    return random.sample(range(l,r), size)

def merge(A,p,q,r):
    n1 = q - p + 1
    n2 = r - q
    L = []
    R = []
    for i in range(n1):
        L.append(A[p+i])

    for j in range(n2):
        R.append(A[q+j+1])

    L.append(inf)
    R.append(inf)
    i = 0
    j = 0
    for k in range(p,r+1):
        if (L[i] <= R[j]):
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1

def merge_sort(A,p,r):
    if p < r:
        q = (p+r)//2
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,p,q,r)

list = random_list(0,100,100)
print(list)
print("\n")
start = time.clock()
merge_sort(list,0,len(list)-1)
print("Vreme je: [ms]", 1000*(time.clock()-start))
print(list)