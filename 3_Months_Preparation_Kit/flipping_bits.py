for _ in range(int(input())):
    s = 2**32 ^ int(input())
    t = str(bin(s))[2:]
    t = t.replace('0', '2')
    t = t.replace('1', '0')
    t = t.replace('2', '1')
    print(int(t,2))