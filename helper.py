# -*- coding: utf-8 -*-
# @Time    : 2019-06-03 15:57
# @Author  : Magic
# @File    : helper.py

def is_isbn_or_key(word):
    """
    判断书编号
    :param word:
    :return: isbn_or_key
    """
    isbn_or_key = 'key'
    if len(isbn_or_key) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    if '-' in 'q' and len(short_word) == 10 and short_word.isdigit:
        isbn_or_key = 'isbn'
    return isbn_or_key
