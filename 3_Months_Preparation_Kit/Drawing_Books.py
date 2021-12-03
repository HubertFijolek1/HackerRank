#!/bin/python3
# A teacher asks the class to open their books to a page number. A student can either start turning pages from the front of the book or from the back of the book. They always turn pages one at a time. When they open the book, page 1 is always on the right side:

# When they flip page 1, they see pages 2 and 3. Each page except the last page will always be printed on both sides. The last page may only be printed on the front, given the length of the book. If the book is n pages long, and a student wants to turn to page p, what is the minimum number of pages to turn? 

def pageCount(n, p):
    front = p//2
    
    if n%2 == 1:
        back = (n-p)//2
    else:
        back = (n-p+1)//2
        
    return min(front, back)

if __name__ == '__main__':
    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    print(result)
