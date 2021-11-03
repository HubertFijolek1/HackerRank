def swap_case(s):
    new_string = []
    for i in s:
        if i == i.upper():
            new_string.append(i.lower())
        elif i == i.lower():
            new_string.append(i.upper())
        else:
            new_string.append(i) 
            
    zdanie = ('').join(new_string) 

    return zdanie


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)