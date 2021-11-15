#!/bin/python3

# Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. She tabulates the number of times she breaks her season record for most points and least points in a game. Points scored in the first game establish her record for the season, and she begins counting from there.

# Example

# scores = [12,24,10,24]

# Scores are in the same order as the games played. She tabulates her results as follows:

#                                      Count
#     Game  Score  Minimum  Maximum   Min Max
#      0      12     12       12       0   0
#      1      24     12       24       0   1
#      2      10     10       24       1   1
#      3      24     10       24       1   1
# Given the scores for a season, determine the number of times Maria breaks her records for most and least points scored during the season.

import os
def breakingRecords(scores):
    min = scores[0]
    max = scores[0]
    min_record = 0
    max_record = 0

    for i in range(1, len(scores)):
        if min > scores[i]:
            min = scores[i]
            min_record += 1
        elif max < scores[i]:
            max = scores[i]
            max_record += 1

    return  max_record, min_record

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
