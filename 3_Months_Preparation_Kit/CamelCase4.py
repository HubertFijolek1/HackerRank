def split(txt):
    new_txt = txt[0].lower()
    for letter in txt[1:]:
        if letter.isalpha():
            if letter.islower():
                new_txt += letter
            else:
                new_txt += " "
                new_txt += letter.lower()
    return new_txt

def comb(txt):
    if txt[0] == "M":
        return combined_string(txt[2:], "lower", True)
    elif txt[0] == "C":
        return combined_string(txt[2:], "upper", False)
    elif txt[0] == "V":
        return combined_string(txt[2:], "lower", False)
        
def combined_string(txt, initial_case, is_method):
    flag = initial_case
    new_txt = ""
    for letter in txt:
        if letter == " ":
            flag = "upper"
            continue
        elif flag == "lower":
            new_txt += letter.lower()
        elif flag == "upper":
            new_txt += letter.upper()
            flag = "lower"
    if is_method == True:    
        # \r is added to txt at this point and needs to be removed
        new_method_txt = new_txt.rstrip() + "()"
        return new_method_txt
    else:
        return new_txt

                
while True:
    try:
        txt = input()
        if txt == "":
            break
        elif txt[0] == "S":
            print(split(txt[4:]))
        elif txt[0] == "C":
            print(comb(txt[2:]))
    except Exception  as e:
        break

    
