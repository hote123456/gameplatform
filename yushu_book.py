# -*- coding: utf-8 -*-
# @Time    : 2019-06-03 16:42
# @Author  : Magic
# @File    : yushu_book.py
from http import HTTP


class YuShuBook:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    key_url = 'http://t.yushu.im/v2/book/search?q={}&count={}'

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        result = HTTP.get(url)
        # dict
        return result

    @classmethod
    def search_by_keyword(cls, keyword, count=15, start=0):
        url = cls.key_url.format(keyword, count, start)
        result = HTTP.get(url)
        # dict
        return result
