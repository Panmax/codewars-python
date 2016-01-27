#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 'Panmax'


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
