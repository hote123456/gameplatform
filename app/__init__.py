# -*- coding: utf-8 -*-
# @Time    : 2019-06-03 18:04
# @Author  : Magic
# @File    : __init__.py
from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    register_blueprin(app)
    return app

def register_blueprin(app):
    from app.web.book import web
    app.register_blueprin(web)