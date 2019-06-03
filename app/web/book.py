# -*- coding: utf-8 -*-
# @Time    : 2019-06-03 17:24
# @Author  : Magic
# @File    : book.py
import json
from flask import jsonify
from helper import is_isbn_or_key
from yushu_book import YuShuBook


@app.route('/book/search/<q>/<page>')
def search(q, page):
    """
    :return: search data
    """
    isbn_or_key = is_isbn_or_key(q)
    if is_isbn_or_key == 'isbn':
        YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    return jsonify(result)
    # return json.dumps(result), 200, {'content-type': 'application/json'}
