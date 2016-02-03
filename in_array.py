#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 'Panmax'


"""
Given two arrays of strings a1 and a2 return a sorted array r in lexicographical order and without duplicates of the strings of a1 which are substrings of strings of a2.

Example 1:

a1 = ["arp", "live", "strong"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

returns ["arp", "live", "strong"]

Example 2:

a1 = ["tarp", "mice", "bull"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

returns []
"""


def in_array(array1, array2):
    results = []
    for a1 in array1:
        for a2 in array2:
            if (a2.find(a1) != -1) and (a1 not in results):
                results.append(a1)
                break
    results.sort()
    return results


def _in_array(a1, a2):
    return sorted({sub for sub in a1 if any(sub in s for s in a2)})


if __name__ == '__main__':
    a1 = ["live", "arp", "strong"]
    a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
    r = ['arp', 'live', 'strong']
    print in_array(a1, a2) == r
