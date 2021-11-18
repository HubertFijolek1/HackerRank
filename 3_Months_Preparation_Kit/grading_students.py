#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

# Sam is a professor at the university and likes to round each student's grade according to these rules:

# If the difference between the grade and the next multiple of 5 is less than 3, round grade up to the next multiple of .
# If the value of grade is less 38 than , no rounding occurs as the result will still be a failing grade.
def gradingStudents(grades):
    # Write your code here
    round_list = []
    for i in grades:
        if i < 35:
            round_list.append(i)
        elif (i % 5) <3 :
            round_list.append(i)
        elif (i % 5) >=3:
            i += (5-i%5)
            round_list.append(i)
        
    return round_list

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
