#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 'Panmax'


def unused_digits(*args):
    all_digits = "0123456789"
    for number in args:
        for i in str(number):
            all_digits = all_digits.replace(i, '')
    return all_digits


if __name__ == '__main__':
    print unused_digits(12, 34, 56, 78)
