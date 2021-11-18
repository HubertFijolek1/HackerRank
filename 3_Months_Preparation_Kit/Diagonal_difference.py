#!/bin/python3
import os

def diagonalDifference(arr):
    counter1 = 0
    counter2 = len(arr)-1
    left_arr = []
    right_arr = []
    for i in range(len(arr)):
        left_arr.append(arr[counter1][counter1])
        counter1+=1
    counter1 = 0
    for i in range(len(arr)):
        right_arr.append(arr[counter1][counter2])
        counter1+=1
        counter2-=1
        
    return abs(sum(left_arr) - sum(right_arr)) 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
