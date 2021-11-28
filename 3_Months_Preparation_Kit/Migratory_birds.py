#!/bin/python3

# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
# Given an array of bird sightings where every element represents a bird type id, determine the id of the most frequently sighted type. If more than 1 type has been spotted that maximum amount, return the smallest of their ids.
def migratoryBirds(arr):
    # Write your code here
    count = arr.count(arr[0])
    set1 = set(arr)
    list1 = []
    for i in set1:
        if arr.count(i)>count and i not in list1:
            count = arr.count(i)
            max = i
    return max

if __name__ == '__main__':

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)
    print(result)


