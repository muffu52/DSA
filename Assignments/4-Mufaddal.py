import numpy as np
import math
import time

def heapSort(A):
    buildMaxHeap(A)
    for i in range(len(A)-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        maxHeapify(A,0,i)

def buildMaxHeap(A):
    for i in range((len(A)//2) -1, -1, -1):
        maxHeapify(A,i,len(A))

def maxHeapify(A, i, heapsize):
    l = 2*i + 1
    r = 2*i + 2

    if l < heapsize and A[l] > A[i]:
        largest = l
    else:
        largest = i
    
    if r < heapsize and A[r] > A[largest]:
        largest = r

    if largest != i:
        A[i] , A[largest] = A[largest], A[i]
        maxHeapify(A, largest, heapsize)

def quickSort(A,p,r):
    if p < r:
        q = partition(A,p,r)
        quickSort(A,p,q-1)
        quickSort(A,q+1,r)

def partition(A,p,r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[r] = A[r], A[i+1]
    return (i+1)


if __name__ == "__main__":
    Arr = Arr2 = [15,13,9,5,12,8,7,4,0,6,2,1]
    print("original array    : ",Arr)
    quickSort(Arr, 0, len(Arr)-1)
    heapSort(Arr2)
    print("Heapsorted array  : ",Arr2)
    print("Quick sorted array: ",Arr)
    

