#!/bin/python3

import os


# Given an array of integers and a positive k, determine the number of (i,j) pairs where i<j and ar[i]+ ar[j] is divisible by k.

#Example
#ar = [1,2,3,4,5,6]
#k = 5
#Three pairs meet the criteria: [1,4], [2,3] and [4,6].

def divisibleSumPairs(n, k, ar):
    # Write your code here
    count = 0
    for i in range(n-1):
        j = i+1
        while j < n:
            if ((ar[i] + ar[j]) % k) == 0:
                count += 1
            j += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
