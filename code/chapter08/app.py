import click
from flask import Flask, redirect, url_for, request, flash, render_template
from flask_login import login_required, current_user, login_user, LoginManager, UserMixin
from flask_sqlalchemy import SQLAlchemy 
from werkzeug.security import generate_password_hash, check_password_hash




app = Flask(__name__, template_folder="templates")
login_manager = LoginManager(app) 
app.debug = True

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Fei!12345678@127.0.0.1:3306/chapter05?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭对模型修改的监控
app.config['SECRET_KEY'] = 'dev' 


db = SQLAlchemy(app)  # 初始化扩展，传入程序实例 app

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    username = db.Column(db.String(20))  # 用户名
    password_hash = db.Column(db.String(128))  #


    def set_password(self, password):  # 用来设置密码的方法，接受密码作为参数
        self.password_hash = generate_password_hash(password)  # 将生成的密码保持到对应字段

    def validate_password(self, password):  # 用于验证密码的方法，接受密码作为参数
        return check_password_hash(self.password_hash, password)  # 返回布尔值
    
    __tablename__ = 'myuser'

@login_manager.user_loader
def load_user(user_id):
    user = User.query.get(int(user_id)) 
    return user


@app.cli.command()
@click.option('--username', prompt=True, help='The username used to login.')
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True, help='The password used to login.')
def admin(username, password):
    """Create user."""
    db.create_all()

    user = User.query.first()
    if user is not None:
        click.echo('Updating user...')
        user.username = username
        user.set_password(password)  # 设置密码
    else:
        click.echo('Creating user...')
        user = User(username=username, name='Admin')
        user.set_password(password)  # 设置密码
        db.session.add(user)

    db.session.commit()  # 提交数据库会话
    click.echo('Done.')


@app.route("/login",methods=['get','post'])
def login():
    if current_user.is_authenticated:  # 如果当前用户未认证
        return redirect(url_for('index'))  # 重定向到主页
    else:
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']

            if not username or not password:
                flash('Invalid input.')
                return redirect(url_for('login'))
        
            user = User.query.first()
             # 验证用户名和密码是否一致
            if username == user.username and user.validate_password(password):
                login_user(user)  # 登入用户
                flash('Login success.')
                return redirect(url_for('index'))  # 重定向到主页
            flash('Invalid username or password.')  # 如果验证失败，显示错误消息
            return render_template('login.html')
        return render_template('login.html')

@app.route("/index")
def index():
    if current_user.is_authenticated:
        return "index"
    else:
        return redirect(url_for('login'))