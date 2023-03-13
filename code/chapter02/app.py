import os
from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)

# __name__是用来标识模块名字的一个系统变量。
# 这里分两种情况：
# 第一种情况指的是当前运行的模块，那么当前模块__name__的值就为"__main__"；
# 第二种情况指的是该模块是使用import导入的模块，那么这个被导入模块的__name__变量的值为该模块的文件名（去掉.py）。

@app.route('/')
def hello():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'

# print(__name__) 属于第二种情况将app.py导入到Flask里面


"""
    动态变量
"""
@app.route("/home/<name>")
def home(name):
    print(url_for('hello'))
    """
        endpoint = 函数名
        def url_for(endpoint, **values):
        Generates a URL to the given endpoint with the method provided.
    """
    return "hello   {}".format(escape(name))

print(os.getenv('FLASK_ENV1'))
