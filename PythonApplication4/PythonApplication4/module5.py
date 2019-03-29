from module1 import insertion_sort

def binary_search(A, l, r, x):
    mid = (l+r)//2

    if(A[mid]==x):
        return mid

    if(A[mid]>x):
        return binary_search(A,l,mid-1,x)
    else:
        return binary_search(A,mid+1,r,x)