import numpy as np
import math
import time
import matplotlib.pyplot as plt


def maxCrossSubArr(Arr, low, mid, high):
    leftSum = -math.inf
    sum = 0
    maxLeft= maxRight = 0
    for i in range(mid, low-1, -1): 
        sum = sum + Arr[i]
        if sum > leftSum:
            leftSum = sum
            maxLeft = i
    
    rightSum = -math.inf
    sum = 0
    for j in range(mid + 1, high):
        sum = sum + Arr[j]
        if sum > rightSum:
            rightSum = sum
            maxRight = j
    return (maxLeft, maxRight, leftSum + rightSum)

def maxSubArr(Arr, low, high):
    if high == low:
        return (low,high,Arr[low-1])
    else:
        mid = (low + high) // 2
        leftLow, leftHigh, leftSum = maxSubArr(Arr, low, mid)
        rightLow, rightHigh, rightSum = maxSubArr(Arr, mid+1, high)
        crossLow, crossHigh, crossSum = maxCrossSubArr(Arr, low, mid, high)

        if leftSum >= rightSum and leftSum >= crossSum:
            return (leftLow, leftHigh, leftSum)
        elif rightSum >= leftSum and rightSum >= crossSum:
            return (rightLow, rightHigh, rightSum)
        else:
            return (crossLow, crossHigh, crossSum)



def timeTaken(n):

    # arr = [-5,1,2,9,-5,8]
    # arr = [2,-1,4,-5,4,3]
    # arr = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
    arr = np.random.randint(-1000, 1000, n)         # generate array of size 'n' with random integers ranging from -1000 to 1000
    start = time.time()
    low,high,max_sum = maxSubArr(arr,0,len(arr))
    end = time.time()
    elapsedTime = end - start
    return elapsedTime

if __name__ == "__main__":

    nArray=[10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000, 200000]   # Array of sample size
    timeArray = []
    complexEqArray = []
    c=1/500000 

    for i in range (len(nArray)):
        complexEq= c*(nArray[i]*np.log(nArray[i]))             # time complexity equation
        timeT = timeTaken(nArray[i])
        complexEqArray.append(complexEq)
        timeArray.append(timeT)                                # Array of actual time taken
    
    
    plt.plot(nArray, timeArray, label="Actual time taken")
    plt.plot(nArray, complexEqArray, label="Theoretical complexity")
    plt.xlabel("number of samples")
    plt.ylabel("time taken")
    plt.title("Theoretical complexity vs Actual time")
    plt.grid()
    plt.legend()
    plt.show()

