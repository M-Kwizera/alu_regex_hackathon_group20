#!/usr/bin/python3

import re

def check_song_lyrics(lyrics):
    pattern = r"\[Verse (\d+)\] (.*)"
    match = re.match(pattern, lyrics)
    
    if match:
        verse_number = match.group(1)
        some_lyrics = match.group(2)
        print("Song lyrics match the pattern.")
    else:
        print("Song lyrics do not match the pattern.")

#To use:
# Down in the Example of usage,
#change the song_lyrics variable to any lyric line you wish to check


# Example of  usage
song_lyrics = "[Verse 3] People always told me be careful of what you do"
check_song_lyrics(song_lyrics)
