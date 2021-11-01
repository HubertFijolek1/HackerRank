def mutate_string(string, position, character):
    zdanie = string.split(' ')
    zdanie.insert(position, character)
    return ('').join(zdanie)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)