# Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

marksheet = [[input(), float(input())] for _ in range(int(input()))]
scores =  { score for _, score in marksheet}
second_lowest = sorted(scores)[1]
second_lowest_names = []
for name, score in marksheet:
    if score == second_lowest:
        second_lowest_names.append(name)
for name in sorted(second_lowest_names):
    print(name)

