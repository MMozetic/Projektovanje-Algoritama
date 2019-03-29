import random
import time
global heap_len

def parent(i):
    return (i-1)//2

def left(i):
    return 2*i+1

def right(i):
    return 2*i+2

def MaxHeapify(A,i):
    global heap_len

    l = left(i)
    r = right(i)
    if l < heap_len and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < heap_len and A[r] > A[largest]:
        largest = r

    if largest != i:
        tmp = A[i]
        A[i] = A[largest]
        A[largest] = tmp
        MaxHeapify(A,largest)

def BuildMaxHeap(A):
    global heap_len
    
    heap_len = len(A)
    for i in range(len(A)//2,-1,-1):
        MaxHeapify(A,i)

def HeapSort(A):
    global heap_len
    
    BuildMaxHeap(A)
    for i in range(len(A)-1,0,-1):
        tmp = A[0]
        A[0] = A[i]
        A[i] = tmp
        heap_len = heap_len - 1
        MaxHeapify(A,0)

print("Random list:")
l = random.sample(range(0,100),30)
print(l)

start = time.clock()

HeapSort(l)

print("\nSort time: " + str(1000*(time.clock()-start)) + " s")

print("\nSorted list:")
print(l)