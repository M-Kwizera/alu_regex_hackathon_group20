i#!/usr/bin/python3

import re

def check_twitter_handle(handle):
    pattern = r"@\w+"
    match = re.match(pattern, handle)

    if match:
        print(handle, "is a valid Twitter handle.")
    else:
        print(handle, "is not a valid Twitter handle.")

#to use:
#replace '#twitter Handle' with your twitter handle

# Execution:
twitter_handle = "#twitter Handle"
check_twitter_handle(twitter_handle)
