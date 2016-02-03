#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 'Panmax'



"""
Your goal in this kata is to implement an difference function, which subtracts one list from another.

It should remove all values from list a, which are present in list b.

array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]
"""


def array_diff(a, b):
    for value_b in b:
        while True:
            try:
                a.remove(value_b)
            except ValueError:
                break
    return a


if __name__ == '__main__':
    print array_diff([1,2], [1])