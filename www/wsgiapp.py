#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Alex Wang'

import logging; logging.basicConfig(level=logging.INFO)
import os

from transwarp import db
from transwarp.web import WSGIApplication, Jinja2TemplateEngine

from config import configs

# 初始化数据库
db.create_engine(**configs.db)

wsgi = WSGIApplication(os.path.dirname(os.path.abspath(__file__)))
# os.path.abspath(__file__) 文件的绝对路径
# os.path.dirname(os.path.abspath(__file__)) 文件的父路径
# 初始化jinja2模板引擎
template_engine = Jinja2TemplateEngine(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'))
# os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates') 结合多个路径
wsgi.template_engine = template_engine

#
import urls
wsgi.add_module(urls)

#
if __name__ == '__main__':
    wsgi.run(9000)
