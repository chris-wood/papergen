import os
import sys
from subprocess import Popen, PIPE

def checkGrammar(text):
    cmd = "diction"
    proc = Popen([cmd], stdin=PIPE, stdout=PIPE)
    stdout, stderr = proc.communicate(text) 
    print stdout
    print stderr


def main(args):
    checkGrammar("Let us ask the question we wish to state.")
    checkGrammar("I have asked you to do it.")

if __name__ == "__main__":
    main(sys.argv[1:])
