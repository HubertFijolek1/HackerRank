# This tool returns successive r length permutations of elements in an iterable.

# If r is not specified or is None, then  defaults to the length of the iterable, and all possible full length permutations are generated.

# Permutations are printed in a lexicographic sorted order. So, if the input iterable is sorted, the permutation tuples will be produced in a sorted order.

# Sample Input

# HACK 2
# Sample Output

# AC
# AH
# AK
# CA
# CH
# CK
# HA
# HC
# HK
# KA
# KC
# KH
# Explanation

# All possible size 2 permutations of the string "HACK" are printed in lexicographic sorted order.

from itertools import permutations
# command = [i for i in input().split()]
# list_of_letters = [i for i in command[0]]
# list_of_permutations = sorted(list(permutations(list_of_letters,int(command[1]))))
# for i in list_of_permutations:
#     print( "".join(i))

#better version

s,n = input().split()
print(*[''.join(i) for i in permutations(sorted(s),int(n))],sep='\n')