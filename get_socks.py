#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 'Panmax'


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
