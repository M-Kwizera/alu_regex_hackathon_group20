#!/usr/bin/python3

import re

def check_isbn_number(isbn_number):
    pattern = r"^ISBN\s(\d{3}-)(\d-)(\d{3}-)(\d{5}-)(\d)$"
    match = re.match(pattern, isbn_number)
    
    if match:
        print(isbn_number, "is a valid number.")
    else:
        print(isbn_number, "is not a valid number.")

#To use:
#change 'isbn_number' s digits to any ISBN number
#& call the function 'check_isbn_number' with 'isbn_number' as the argument.

isbn_number = "ISBN 123-4-567-89102-3"
check_isbn_number(isbn_number)
