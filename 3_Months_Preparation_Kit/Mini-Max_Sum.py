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