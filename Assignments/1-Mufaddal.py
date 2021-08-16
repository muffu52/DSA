import numpy as np

def main():
    arrayInsert = arrayMerge = [3, 41, 52, 26, 38, 57, 9, 49] 
    print("Original array: ", arrayInsert)
    print("Insertion sorted array", insertion(arrayInsert))
    print("Merge sorted array", split(arrayMerge))
    

# insertion method
def insertion(A):
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1

        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j = j - 1

        A[j+1] = key
    return A

# merge sort
def split(A):
    r = len(A)
    if r > 1:
        div = r // 2 # round down
        first = A[:div]
        sec = A[div:]
        split(first)
        split(sec)
        return merge(A, first, sec)
    

def merge(Arr, L , R):
    h = i = j = 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            Arr[h] = L[i]
            i = i + 1  # move pointer
        else: 
            Arr[h] = R[j]
            j = j + 1  # move pointer
        h = h + 1     

    # join left over array to main array
    if i < len(L):
        Arr = np.concatenate((Arr[:h], L[i:]))
    else:
        Arr = np.concatenate((Arr[:h], R[j:]))

    return Arr

if __name__ == "__main__":

    main()
