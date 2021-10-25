# Task
# Given an n integer,  perform the following conditional actions:
# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5 print Not Weird
# If n even and in the inclusive range of 6 to 20  print Weird
# If nis even and greater than 20 , print Not Weird



n = int(input())
if n % 2 == 0:
    if n in range(2,6):
        print("Not Weird")
    elif n in range(6,21):
        print("Weird")
    elif n > 20:
        print("Not Weird")
else:
    print("Weird")
