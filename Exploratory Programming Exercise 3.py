#Importing this allows user to use Regex
import re

def afunct(astr):
    if type(astr) != str:
        raise TypeError("This is not a string")
    regex = r"(\w*[a][t]\b)"
    for i in regex:
        if len(regex) <= 4:
            print i

import thevalleyofgold.txt

afunct("some string")
