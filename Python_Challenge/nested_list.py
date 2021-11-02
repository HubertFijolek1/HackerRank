marksheet = [[input(), float(input())] for _ in range(int(input()))]
scores =  { score for _, score in marksheet}
second_lowest = sorted(scores)[1]
second_lowest_names = []

for name, score in marksheet:
    if score == second_lowest:
        second_lowest_names.append(name)
for name in sorted(second_lowest_names):
    print(name)

