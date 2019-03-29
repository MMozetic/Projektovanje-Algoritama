from math import floor
import random
import time

def insertion_sort(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j - 1
        while(i>=0 and A[i]>key):
            A[i+1] = A[i]
            i = i - 1
        A[i+1] = key

def BucketSort(A):
    n = len(A)
    B = []
    C = []
    for i in range(n):
        B.append(0)

    for i in range(n):
        B[floor(n*A[i])] = A[i]

    for i in range(n):
        insertion_sort(B)

    for i in range(n):
        C.append(B[i])

    return C

print("Random list:")
count = 20

l = random.sample(range(0,count),count)
print(l)

for i in range(len(l)):
    l[i] = l[i]/count

start = time.clock()
l = BucketSort(l)
print("\nSort time: " + str(1000*(time.clock()-start)) + " s")

for i in range(len(l)):
    l[i] = int(l[i]*count)

print("\nSorted list:")
print(l)