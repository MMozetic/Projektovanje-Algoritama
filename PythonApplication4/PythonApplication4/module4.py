from module1 import insertion_sort

def binary_search(A, a):
    first = 0
    last = len(A)-1

    insertion_sort(A)

    while(first <= last):
        mid = (first+last)//2
        
        if(A[mid]==a):
            return mid

        if(A[mid]>a):
            last = mid - 1
        else:
             first = mid + 1