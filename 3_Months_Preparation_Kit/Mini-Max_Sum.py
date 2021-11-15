# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

def miniMaxSum(arr):
    arr.sort()
    s = sum(arr)
    maxResult = s - arr[0]
    minResult = s - arr[len(arr) - 1]
    
    print(minResult, maxResult)


def Main():
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)


if __name__ == '__main__':
    Main()