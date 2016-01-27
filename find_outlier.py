#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 'Panmax'

"""
You are given an array (which will have a length of at least 3, but could be very large) containing integers. The integers in the array are either entirely odd or entirely even except for a single integer N. Write a method that takes the array as an argument and returns N.

For example:

[2, 4, 0, 100, 4, 11, 2602, 36]

Should return: 11

[160, 3, 1719, 19, 11, 13, -21]

Should return: 160
"""


def find_outlier(integers):
    odds = []
    evens = []
    for integer in integers:
        if integer % 2 == 0:
            evens.append(integer)
        else:
            odds.append(integer)
    if len(odds) == 1:
        result = odds[0]
    else:
        result = evens[0]
    return result


if __name__ == '__main__':
    print find_outlier([2, 6, 8, 10, 3])
