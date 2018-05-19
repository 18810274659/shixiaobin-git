#encoding:utf-8

from flask import Flask,session,render_template,request
import  os

app = Flask(__name__)

app.config['SECRET_KEY'] =  os.urandom(24)

@app.route('/')
def helloword():

    return render_template('index.html')

    session['username'] = 'shixiaobin'
    #chi jiu hua 持久化
    session.permanent = True

    return 'helloword'


@app.route('/search/')
def search():
    return request.args.get('q')
    return 'search'


#默认为get请求
#想用post表明
@app.route('/login/',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        return username
    return 'login'

@app.route('/get/')
def get():
    return session.get('username')


@app.route('/delete/')
def delete():
    print session.get('username')
    session.pop('username')
    print session.get('username')
    return 'success'



if __name__ == '__main__':
    app.run(host="192.168.0.109",port = 5000)