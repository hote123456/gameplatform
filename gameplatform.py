from flask import Flask

app = Flask(__name__)
app.config.from_object('config')


@app.route('/hello/')
def hello():
    return 'hello word'


# app.add_url_rule('/hello', view_func=hello)
if __name__ == '__main__':
    # 生产环境 ngix+uwsgi
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=81)
