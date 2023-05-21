#!/usr/bin/python3

import re

def check_movie_title(movie_title):
    pattern = r"^(.*?) \(\d{4}\)$"
    match = re.match(pattern, movie_title)
    
    if match:
        print(movie_title, "is a valid movie title.")
    else:
        print(movie_title, "is not a valid movie title.")

#To use:
#change 'movie_title' s value to a movie title of choice
#& call the fuction 'check_movie_title with movie title as the argument'

movie_title = "Charlie and the Chocolate Factory (2005)"
check_movie_title(movie_title)
