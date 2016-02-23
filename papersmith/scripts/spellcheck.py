import os
import sys
import enchant
import string
from terminal import *

# TODO: use pycurses for a nice CLI

class Sentence(object):
    pass

class SpellChecker(object):
    def __init__(self, dictionary):
        self.dictionary = enchant.Dict(dictionary)

    def printSentenceWithError(self, words, index):
        for wordIndex, word in enumerate(words):
            if index == wordIndex:
                cprint("red", word)
            else:
                cprint("green", word)

    def checkText(self, text):
        sentences = filter(lambda s : len(s) > 0, text.split("\n"))
        for sentence in sentences:

            exclude = set(string.punctuation)
            words = [(''.join(ch for ch in word.strip() if ch not in exclude), index) for index, word in enumerate(sentence.split(" "))]
            failures = filter(lambda (word, index) : len(word) > 0 and not self.dictionary.check(word), words)

            replacements = []
            for (failure, index) in failures:

                suggestions = self.dictionary.suggest(failure)
                replacement = failure
                if len(suggestions) > 0:
                    # TODO: need to print the original sentence -- not the reduced verison that has puncuation removed
                    self.printSentenceWithError(map(lambda t : t[0], words), index)

                    # print failure, index
                    # 1. print out sentence (minus the word) in green, and the word in red
                    # 2. print out suggestion list
                    # 3. collection suggestions

                    print ""
                    print "\t0: Skip!"
                    for changeIndex, change in enumerate(suggestions):
                        print "\t%d: %s" % (changeIndex + 1, change)
                    choice = int(raw_input("> "))

                    skipped = False
                    if (choice == 0):
                        skipped = True

                    while choice < 0 or choice > len(suggestions):
                        print "Invalid selection. Try again."
                        choice = int(raw_input("> "))
                    if not skipped:
                        replacement = suggestions[int(choice) - 1]

                replacements.append((index, replacement))
                words[index] = (replacement, index)

def main(args):
    if len(args) != 1:
        print >> sys.stderr, "usage: python spellchecker.py <filename>"
        exit(1)
    fhandle = open(args[0], "r")
    text = fhandle.read()

    checker = SpellChecker("en_US")
    checker.checkText(text)

if __name__ == "__main__":
    main(sys.argv[1:])
