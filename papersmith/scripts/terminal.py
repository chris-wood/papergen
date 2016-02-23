import os
import sys

ansiRed = "\x1b[31m";
ansiGreen = "\x1b[32m";
ansiYellow = "\x1b[33m";
ansiBlue = "\x1b[34m";
ansiMagenta = "\x1b[35m";
ansiCyan = "\x1b[36m";
ansiReset = "\x1b[0m";

## TODO: implement prettyprint word wrapping at specific number of characters

def colorize(color, string):
    result = string
    if color == "red":
        result = ansiRed + string + ansiReset
    elif color == "green":
        result = ansiGreen + string + ansiReset
    elif color == "yellow":
        result = ansiYellow + string + ansiReset
    elif color == "blue":
        result = ansiBlue + string + ansiReset
    elif color == "magenta":
        result = ansiMagenta + string + ansiReset
    elif color == "cyan":
        result = ansiCyan + string + ansiReset
    else:
        print >> sys.stderr, "Bad color name:", color

    return result

def cprintln(color, string):
    print colorize(color, string)

def cprint(color, string):
    print colorize(color, string),
