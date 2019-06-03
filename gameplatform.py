from flask import Flask, make_response

app = Flask(__name__)
app.config.from_object('config')


@app.route('/hello/')
def hello():
    # status code 200,404,301
    headers = {
        'content-type': 'application/json',
        'location':'http://baidu.com'
    }
    response = make_response('json', 301)
    response.headers = headers
    return response


# app.add_url_rule('/hello', view_func=hello)
if __name__ == '__main__':
    # 生产环境 ngix+uwsgi
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=81)
