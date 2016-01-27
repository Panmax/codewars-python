#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 'Panmax'

"""
Is Prime

Define a function isPrime that takes one integer argument and returns true or false depending on if the integer is a prime.

Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 1 and itself.

Example

isPrime(5)
=> true
"""


def is_prime(num):
    if num < 2:
        return False
    for n in range(2, num):
        if num % n == 0:
            return False
    return True


def _is_prime(num):
    return num > 1 and not any(num % n == 0 for n in range(2, num))


if __name__ == '__main__':
    print is_prime(2)
