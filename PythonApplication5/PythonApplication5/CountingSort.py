import random
import time
def CountingSort(A, B, k):
    C = []
    for i in range(k):
        C.append(0)

    for j in range(len(A)):
        C[A[j]] = C[A[j]] + 1

    for i in range(1,k):
        C[i] = C[i] + C[i-1]

    for j in range(len(A) - 1,-1,-1):
        B[C[A[j]]-1] = A[j]
        C[A[j]] = C[A[j]] - 1

B = []

print("Random list:")
l = random.sample(range(0,100),30)
print(l)

B = [0 for i in range(len(l))]

start = time.clock()
CountingSort(l,B,max(l)+1)
print("\nSort time: " + str(1000*(time.clock()-start)) + " s")

print("\nSorted list:")
print(B)