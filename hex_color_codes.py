#!/usr/bin/python3

import re

def validate_hex_color_code(color_code):
    pattern = r"^#[a-fA-F0-9]{6}$"
    if re.match(pattern, color_code):
        print(f"{color_code} is a valid hex color code.")
    else:
        print(f"{color_code} is not a valid hex color code.")

# Testing the function
color_codes = [
    '#123456',
    '#FFFFFF',
    '#000000',
    '#GHIJKL',
]

for color_code in color_codes:
    validate_hex_color_code(color_code)
