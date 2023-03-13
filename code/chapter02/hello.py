from flask import Flask

app = Flask(__name__)

# __name__是用来标识模块名字的一个系统变量。
# 这里分两种情况：
# 第一种情况指的是当前运行的模块，那么当前模块__name__的值就为"__main__"；
# 第二种情况指的是该模块是使用import导入的模块，那么这个被导入模块的__name__变量的值为该模块的文件名（去掉.py）。

@app.route('/')
def hello():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'

# print(__name__) 属于第二种情况将app.py导入到Flask里面


# 这是因为 Flask 默认会假设你把程序存储在名为 app.py 或 wsgi.py 的文件中。
# 如果你使用了其他名称，就要设置系统环境变量 `FLASK_APP` 来告诉 Flask 你要启动哪个程序：
# export FLASK_APP=hello.py