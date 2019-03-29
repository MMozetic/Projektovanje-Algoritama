def bubble_sort(A):
    length = len(A)
    for i in range(0,length-1):
        for j in range(i+1, length):
            if(A[i]>A[j]):
                tmp = A[i]
                A[i] = A[j]
                A[j] = tmp
