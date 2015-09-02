import os
import sys
from subprocess import Popen, PIPE

def checkGrammar(text):
    cmd = "diction"
    proc = Popen([cmd, "-s"], stdin=PIPE, stdout=PIPE)
    stdout, stderr = proc.communicate(text) 
    print stdout


def main(args):
    checkGrammar("How doe sthis sound? THIS SHOULD BE CHANGED HATH DOES IT.")

if __name__ == "__main__":
    main(sys.argv[1:])
