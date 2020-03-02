from PyLyrics import *


def get_lyrics(title, artist):
    print(PyLyrics.getLyrics(artist, title))


def search_for_keywords(songs, keywords):
    for keyword in keywords:
        for lyrics in songs:
            # if keyword not in lyrics:
            if not lyrics.__contains__(keyword):
                print(lyrics)
                del lyrics
    print(songs)


def check_input(args):
    if len(args) < 3:
        print("Syntax incorrect")
    if len(args) == 1:
        print("Make sure you supply the necessary requirements\nThe first argument should be a spotify playlist uri. "
              "All following arguments should be search keywords")
