from random import random
import random
import time

def random_list(l,r, size):
    return random.sample(range(l,r), size)


def partition(A,p,r):
    x = A[r]
    i = p - 1
    for j in range(p,r):
        if A[j] <= x:
            i = i + 1
            tmp = A[i]
            A[i] = A[j]
            A[j] = tmp
    tmp = A[i+1]
    A[i+1] = A[r]
    A[r] = tmp
    return i+1

def randomized_partition(A,p,r):
    i = random.randint(p,r)
    tmp = A[r]
    A[r] = A[i]
    A[i] = tmp
    return partition(A,p,r)

def randomized_quicksort(A,p,r):
    if p<r:
        q = randomized_partition(A,p,r)
        randomized_quicksort(A,p,q-1)
        randomized_quicksort(A,q+1,r)

l = random_list(0,100,10)
print(l)
print("\n")
start = time.clock()
randomized_quicksort(l,0,len(l)-1)
end = time.clock()-start
print(l)
print("Vreme sortiranja je: [ms]", end*1000)