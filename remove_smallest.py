#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 'Panmax'


def remove_smallest(numbers):
    if not numbers:
        return []

    min_number = min(numbers)
    for index, number in enumerate(numbers):
        if number == min_number:
            del numbers[index]
            return numbers


def _remove_smallest(numbers):
    if numbers:
        numbers.remove(min(numbers))
    return numbers

