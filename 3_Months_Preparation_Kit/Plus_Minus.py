# Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line with  digits after the decimal. The function should not return a value.

# Print the following 3 lines, each to 6 decimals:

# proportion of positive values
# proportion of negative values
# proportion of zeros

n = float(input())
lst = [int(x) for x in input().split()]
print (format(len([x for x in lst if x > 0])/n, ".6f"))
print (format(len([x for x in lst if x < 0])/n, ".6f"))
print (format(len([x for x in lst if x == 0])/n, ".6f"))