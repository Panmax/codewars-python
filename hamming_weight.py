#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 'Panmax'

"""
The Hamming weight of a string is the number of symbols that are different from the zero-symbol of the alphabet used. There are several algorithms for efficient computing of the Hamming weight for numbers. In this Kata, speaking technically, you have to find out the number of '1' bits in a binary representation of a number. Thus,

The interesting part of this task is that you have to do it without string operation (hey, it's not really interesting otherwise)

;)
"""

def hamming_weight(x):
    binary = bin(x)
    count = 0
    for b in binary:
        if b == '1':
            count += 1
    return count


def _hamming_weight(x):
    return bin(x).count('1')


if __name__ == '__main__':
    print _hamming_weight(10)
