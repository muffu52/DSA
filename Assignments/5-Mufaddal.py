import numpy as np
import time
import matplotlib.pyplot as plt

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

# insertion method
def insertion(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1

        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j = j - 1

        A[j+1] = key


def bucketSort(A):
    B = [0] * len(A)
    n = len(A)
    for i in range(0, n):
        B[i] = []
    for i in range(0, n):
        B[int(n*A[i])].append(A[i])
    for i in range(0, n):
        insertion(B[i])
        
    h=0
    for i in range(0,n):
        for j in range(len(B[i])):
            A[h] = B[i][j]
            h = h + 1


def countingSort(A):
    k = np.max(A)
    C = [0] * (k+1)
    B = [0] * len(A)

    for i in range(0, k+1):
        C[i]= 0
    for j in range(0, len(A)):
        C[A[j]] = C[A[j]] + 1
    for i in range(1, k+1):
        C[i] = C[i] + C[i-1]
    for j in range(len(A)-1,-1,-1):
        B[C[A[j]]-1] = A[j]
        C[A[j]] = C[A[j]] - 1
    return B
    
def countingSortRad(A,index):
    k = np.max(A)
    C = [0] * (k+1)
    B = [0] * len(A)


    # use the specific digit from A[j] instead of the full value
    for i in range(0, k+1):
        C[i]= 0
    for j in range(0, len(A)):
        C[(A[j] // 10**index)%10] = C[(A[j] // 10**index)%10] + 1
    for i in range(1, k+1):
        C[i] = C[i] + C[i-1]
    for j in range(len(A)-1,-1,-1):
        B[C[(A[j] // 10**index)%10]-1] = A[j]
        C[(A[j] // 10**index)%10] = C[(A[j] // 10**index)%10] - 1
    # copy specific digit sorted array to be the main array
    for i in range(0,len(A)):
        A[i] = B[i]

    

def radix(A):
    
    max_digits = len(str(np.max(A)))
    for i in range(1,max_digits+1):
        countingSortRad(A,i)        # we use counting sort in radix sort as it is a stable sort.


def timeTaken():

    radix_time_array = []
    quick_time_array = []
    
    no_of_digits = []

    for i in range(0,6):
        arrRad = []
        arrQuick = []
        no_of_digits.append(i+1)

        arr = np.random.randint(1*10**i, (10*10**i)-1, 16).tolist() 
        arrRad = arr
        arrQuick = arr
        # print("Original array     : ",arrRad)
        # print("Original array     : ",arrQuick)
        start = time.time()
        radix(arrRad)        # apply radix sort
        end = time.time()
        elapsedTime = end - start
        radix_time_array.append(elapsedTime)
        start = time.time()
        quickSort(arrQuick, 0, len(arrQuick)-1)      # apply quick sort
        end = time.time()  
        elapsedTime = end - start
        quick_time_array.append(elapsedTime)

    return no_of_digits, radix_time_array, quick_time_array
    

if __name__ == "__main__":
    Arr = [0.79,0.13,0.16,0.64,0.39,0.20,0.89,0.53,0.71,0.42]
    Arr1 = [6,0,2,0,1,3,4,6,1,3,2]
    
    Arr2 =  [329,457,657,839,436,720,355]
    Arr3 =  [329,457,657,839,436,720,355]
    print("Original array     : ",Arr)
    bucketSort(Arr)
    print("Bucket sorted array: ",Arr)
    # print("Original array     : ",Arr1)
    # Arr1 = countingSort(Arr1)
    # print("Counting sort array: ",Arr1)
    print("Original array     : ",Arr2)
    radix(Arr2)
    print("Radix sort array   : ",Arr2)
    print("Original array     : ",Arr3)
    quickSort(Arr3, 0, len(Arr3)-1)
    print("quickSort array    : ",Arr3)

    nArray, radix_time, quicksort_time = timeTaken()

    plt.plot(nArray, radix_time, label="Time taken by RadixSort")
    plt.plot(nArray, quicksort_time, label="Time taken by QuickSort")
    plt.xlabel("Number of digits")
    plt.ylabel("Time taken")
    plt.title("Time taken for radix and quicksort")
    plt.grid()
    plt.legend()
    plt.show()

# from the graph we see that quick sort is good as long as the number of digits are low as well.
# As the number of digits increase the taken for radis sort becomes higher
