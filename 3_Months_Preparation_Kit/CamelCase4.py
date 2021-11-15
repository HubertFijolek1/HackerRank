# Camel Case is a naming style common in many programming languages. In Java, method and variable names typically start with a lowercase letter, with all subsequent words starting with a capital letter (example: startThread). Names of classes follow the same pattern, except that they start with a capital letter (example: BlueCar).

# Your task is to write a program that creates or splits Camel Case variable, method, and class names.

# Input Format

# Each line of the input file will begin with an operation (S or C) followed by a semi-colon followed by M, C, or V followed by a semi-colon followed by the words you'll need to operate on.
# The operation will either be S (split) or C (combine)
# M indicates method, C indicates class, and V indicates variable
# In the case of a split operation, the words will be a camel case method, class or variable name that you need to split into a space-delimited list of words starting with a lowercase letter.
# In the case of a combine operation, the words will be a space-delimited list of words starting with lowercase letters that you need to combine into the appropriate camel case String. Methods should end with an empty set of parentheses to differentiate them from variable names.
# Output Format

# For each input line, your program should print either the space-delimited list of words (in the case of a split operation) or the appropriate camel case string (in the case of a combine operation).
# Sample Input

# S;M;plasticCup()

# C;V;mobile phone

# C;C;coffee machine

# S;C;LargeSoftwareBook

# C;M;white sheet of paper

# S;V;pictureFrame

# Sample Output

# plastic cup

# mobilePhone

# CoffeeMachine

# large software book

# whiteSheetOfPaper()

# picture frame

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

    
