# coding=utf-8
"""
描述： 输入N个整数。判断这N个整数是否可以构建一个等差数列。（1<N<1000）

输入： N个整数(以空格分隔）

输出： 可以构成等差数列输出True，否则输出False。

(1)input：

5 3 2 1 7 6 4 8 10 9

output: True

(2)input：

4 6 3 2 7

output: False
"""

import string

n_nums = raw_input('Enter numbers:')
input_list = [int(x) for x in n_nums.split(' ')]


def merge_sort(left, right):
    """
    merge two sorted lists into one
    :param left: a sorted list
    :param right: a sorted list
    :return: a sorted list combined left and right
    """
    result = []
    while len(left) >= 1 and len(right) >= 1:
        if left[0] <= right[0]:
            result += [left[0]]
            left = left[1:]
        else:
            result += [right[0]]
            right = right[1:]
    result += left + right
    return result


def sort_list(lst):
    # sort a list using quick sort
    if len(lst) < 2:
        return lst
    else:
        mid = int(len(lst)/2)
        left = sort_list(lst[:mid])
        right = sort_list(lst[mid:])
        return merge_sort(left, right)


def is_arith_pro(lst):
    n = lst[1] - lst[0]
    i = 0
    while i <= len(lst)-2:
        if lst[i+1] - lst[i] != n:
            return False
        i += 1
    return True

sorted_list = sort_list(input_list)
print is_arith_pro(sorted_list)


