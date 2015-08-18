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
