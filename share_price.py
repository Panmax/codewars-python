#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 'Panmax'


def share_price(invested, changes):
    for change in changes:
        invested *= (100 + change) / 100.0
    return "{0:.2f}".format(invested)


if __name__ == '__main__':
    print share_price(100, [-20, 30])
