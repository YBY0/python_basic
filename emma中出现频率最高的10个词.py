# -*- coding: utf-8 -*-
"""
计算《爱玛》中出现频率最高的十个词
"""

import re


def calculate(f):
    """
    计算一本书中出现频率最高的十个词
    :param f: 书本的txt文件
    :return: 出现频率最高的十个词
    """
    dic = {}
    for line in f:
        words_t = line.strip()
        words = re.split('\W', words_t)
        for word in words:
            if word in dic:
                dic[word] += 1
            else:
                dic[word] = 1
    dic_lst = dic.items()
    dic_lst.sort(key=lambda x: x[1],reverse=True)

    for w in dic_lst[:10]:
        print w[0]

fi = open('emma.txt')
calculate(fi)
fi.close()


