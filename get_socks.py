#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 'Panmax'

"""
Description:

Punky loves wearing different colored socks, but Henry can't stand it.

Given an array of different colored socks, return a pair depending on who was picking them out.

Example:

get_socks('Punky', ['red','blue','blue','green']) -> ['red', 'blue']
Note that Punky can have any two colored socks, in any order, as long as they are different and both exist. Henry always picks a matching pair.

If there is no possible combination of socks, return an empty array.
"""


def get_socks(name, socks):
    if len(socks) < 2:
        return []
    if name == 'Punky':
        sock1 = socks[0]
        for sock in socks[1:]:
            if sock != sock1:
                return [sock, sock1]
        else:
            return []
    if name == 'Henry':
        sock1 = socks[0]
        for sock in socks[1:]:
            if sock == sock1:
                return [sock, sock]
        else:
            return []
