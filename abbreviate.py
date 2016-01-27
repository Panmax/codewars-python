#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 'Panmax'

"""
The word i18n is a common abbreviation of internationalization the developer community use instead of typing the whole word and trying to spell it correctly. Similarly, a11y is an abbreviation of accessibility.

Write a function that takes a string and turns any and all words within that string of length 4 or greater into an abbreviation following the same rules.

Notes:

A "word" is a sequence of alphabetical characters. By this definition, any other character like a space or hyphen (eg. "elephant-ride") will split up a series of letters into two words (eg. "elephant" and "ride").
The abbreviated version of the word should have the first letter, then the number of removed characters, then the last letter (eg. "e6t-r2e").
"""
import re


def abbreviate(s):
    words = re.findall(r"\w+", s)
    others = re.findall(r"\W+", s)
    if len(others) < len(words):
        others.append("")

    results = []
    for word, symbol in zip(words, others):
        if len(word) >= 4:
            word = word[0] + str(len(word[1:-1])) + word[-1]
        results.append(word)
        results.append(symbol)
    return ''.join(results)


if __name__ == '__main__':
    print abbreviate("a-doggy. doggy-doggy; cat: balloon-the; a, balloon;")
