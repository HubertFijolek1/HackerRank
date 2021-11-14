from itertools import permutations
# command = [i for i in input().split()]
# list_of_letters = [i for i in command[0]]
# list_of_permutations = sorted(list(permutations(list_of_letters,int(command[1]))))
# for i in list_of_permutations:
#     print( "".join(i))

#better version

s,n = input().split()
print(*[''.join(i) for i in permutations(sorted(s),int(n))],sep='\n')