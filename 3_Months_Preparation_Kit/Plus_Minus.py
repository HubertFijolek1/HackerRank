n = float(input())
lst = [int(x) for x in input().split()]
print (format(len([x for x in lst if x > 0])/n, ".6f"))
print (format(len([x for x in lst if x < 0])/n, ".6f"))
print (format(len([x for x in lst if x == 0])/n, ".6f"))