# -*- coding: utf-8 -*-
"""
solve the popular hanoi question
"""


def hanoi(n, A, B, C):
    if n == 1:
        print 'Move', n, 'from', A, 'to', C
    else:
        hanoi(n-1,A,C,B)
        print 'Move', n, 'from', A, 'to', C
        hanoi(n-1,B,A,C)

X = int(raw_input('How many columns are there:'))
hanoi(X, 'A', 'B', 'C')
