#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 'Panmax'



"""
There exists a sequence of numbers that follows the pattern

          1
         11
         21
        1211
       111221
       312211
      13112221
     1113213211
          .
          .
          .
Starting with "1" the following lines are produced by "saying what you see", so that line two is "one one", line three is "two one(s)", line four is "one two one one".

Write a function that given a starting value as a string, returns the appropriate sequence as a list. The starting value can have any number of digits. The termination condition is a defined by the maximum number of iterations, also supplied as an argument.
"""


def look_and_say(data='1', maxlen=5):
    results = []
    for i in range(maxlen):
        index = 0
        _data = ''
        while True:
            n = 1
            d = data[index]
            for _ in data[index+1:]:
                if _ == d:
                    n += 1
                    index += 1
                else:
                    break
            _data += str(n) + d
            index += 1
            if index >= len(data):
                break
        data = _data
        results.append(data)
    return results


from itertools import groupby


def _look_and_say(data='1', maxlen=5):
    L = []
    for i in range(maxlen):
        data = "".join(str(len(list(g)))+str(n) for n, g in groupby(data))
        L.append(data)
    return L

if __name__ == '__main__':
    print look_and_say()
