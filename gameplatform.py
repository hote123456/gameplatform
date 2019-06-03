from flask import Flask, make_response, jsonify
import json

from helper import is_isbn_or_key
from yushu_book import YuShuBook

app = Flask(__name__)
app.config.from_object('config')


@app.route('/hello/')
def hello():
    # status code 200,404,301
    headers = {
        'content-type': 'application/json',
        'location': 'http://baidu.com'
    }
    # response = make_response('json', 301)
    # response.headers = headers
    # return response
    return '<html></html>', 301, headers


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


# app.add_url_rule('/hello', view_func=hello)
if __name__ == '__main__':
    # 生产环境 ngix+uwsgi
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=81)
