#!/usr/bin/python3

import re

def check_episode_title(episode_title):
    pattern = r"^(.*)(S\d+E\d+\:)(\s.*)$"
    match = re.match(pattern, episode_title)
    
    if match:
        print(episode_title, "is a valid episode title.")
    else:
        print(episode_title, "is not a valid episode title.")

#Usage:
#change 'episode_title'to a episode title of choice
#& call the function 'check_episode_title' with 'episode_title' as the argument

episode_title = "Grays Anatomy S10E12: surgery"
check_episode_title(episode_title)

