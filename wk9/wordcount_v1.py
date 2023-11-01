import sys
import string
import os

def f1(file_name):
    # read file and words
    if os.path.exists(file_name):
        fhand = open(file_name)
    else:
        return 'IO_error'

    counts = {}
    words = fhand.read().split()

    # create a dictionary
    if len(words) == 0:
        fhand.close()
    else:
        for word in words:
            translator = str.maketrans('', '', string.punctuation)
            w = word.upper().translate(translator)
            if (len(w) > 0):
                counts[w] = counts.get(w, 0) + 1
        fhand.close()

    return counts


def f2(counts):
    # sort a dictionary reversely based on count of each word
    if len(counts) != 0:
        lst = []
        for key, val in counts.items():
            newtup = (val, key)
            lst.append(newtup)
            lst = sorted(lst, reverse=True)
        return lst