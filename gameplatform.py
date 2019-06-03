from flask import Flask

app = Flask(__name__)


# @app.route('/hello/')
def hello():
    return 'hello word'


app.add_url_rule('/hello', view_func=hello)

app.run(debug=True)
