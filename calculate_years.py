#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 'Panmax'


def calculate_years(principal, interest, tax, desired):
    year = 0
    while True:
        if principal >= desired:
            return year
        principal = principal * (1+interest) - principal*interest*tax
        year += 1


if __name__ == '__main__':
    print calculate_years(1000, 0.05, 0.18, 1100)
