#!/bin/python3
#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

# There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

def sockMerchant(n, ar):
    # Write your code here
    list1 = []
    counter = 0
    for i in ar:
        if ar.count(i)>=2 and i not in list1:
            counter +=ar.count(i)//2
            list1.append(i)
    return counter
            
            
        

if __name__ == '__main__':
    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)
