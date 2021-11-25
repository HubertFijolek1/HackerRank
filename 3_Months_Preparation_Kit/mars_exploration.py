#!/bin/python3
import os

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

# Letters in some of the SOS messages are altered by cosmic radiation during transmission. Given the signal received by Earth as a string, , determine how many letters of the SOS message have been changed by radiation.

# Example
#s = 'SOSTOT'

# The original message was SOSSOS. Two of the message's characters were changed in transit.

def marsExploration(s):
    res = 0
    for ind in range(0, len(s), 3):
        if s[ind] != 'S':
            res += 1
        if s[ind+1] != 'O':
            res += 1
        if s[ind+2] != 'S':
            res += 1
            
    return res
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
