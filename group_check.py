#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 'Panmax'
"""
In English and programming, groups can be made using symbols such as "()" and "{}" that change meaning. However, these groups must be closed in the correct order to maintain correct syntax.

Your job in this kata will be to make a program that checks a string for correct grouping. For instance, the following groups are done correctly:

({})
[[]()]
[{()}]
The next are done incorrectly

{(})
([]
[])
A correct string cannot close groups in the wrong order, open a group but fail to close it, or close a group before it is opened.

Your function will take an input string that may contain any of the symbols "()" "{}" or "[]" to create groups.

It should return True if the string is empty or otherwise grouped correctly, or False if it is grouped incorrectly.
"""


def group_check(s):
    stack = []
    result = True
    for _ in s:
        if _ in ('(', '{', '['):
            stack.append(_)
        elif _ == ')':
            if not stack or stack.pop() != '(':
                result = False
                break
        elif _ == '}':
            if not stack or stack.pop() != '{':
                result = False
                break
        elif _ == ']':
            if not stack or stack.pop() != '[':
                result = False
                break
        else:
            continue
    if stack:
        result = False
    return result


BRACES = {'(': ')', '[': ']', '{': '}'}


def _group_check(s):
    stack = []
    for b in s:
        c = BRACES.get(b)
        if c:
            stack.append(c)
        elif not stack or stack.pop() != b:
            return False
    return not stack


if __name__ == '__main__':
    print group_check("()")