import os
import sys
import enchant

class SpellChecker(object):
    def __init__(self, dictionary):
        self.dictionary = enchant.Dict(dictionary)

    def checkText(self, text):
        sentences = text.split(".")
        for sentence in sentences:
            words = [(word, index) for index, word in enumerate(sentence.split(" "))]
            failures = filter(lambda (word, index) : self.dictionary.check(word), words)
            print "Assessing: " + repr(sentence)

            replacements = []
            for (failure, index) in failures:
                print failure
                # 1. print out sentence (minus the word) in green, and the word in red
                # 2. print out suggestion list
                # 3. collection suggestions
                # self.dictionary.suggest(word)

                replacement = failure
                replacements.append((index, replacement))

def main(args):
    if len(args) != 1:
        print >> sys.stderr, "usage: python spellchecker.py <filename>"
        exit(1)
    fhandle = open(args[0], "r")
    # TODO: read the file

if __name__ == "__main__":
    main(sys.argv[1:])

