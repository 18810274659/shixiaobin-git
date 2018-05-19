#encoding: utf-8
from flask import Flask,url_for,redirect,render_template
import config

app = Flask(__name__)


@app.route('/')
def hellowore():
    comment = [
        {
            'user':'shi',
            'content':'xxx'
        },
        {
            'user':'bin',
            'content':'hao'
        }
    ]



    return render_template("index.html",comment=comment)
    return  redirect("/login/")
    print url_for("my_list")
    print url_for("article",id='abc')
    #return 'helloworddssddddd'

@app.route('/article/<id>')
def article(id):
    return 'dddd %s' % id


@app.route('/login/')
def login():
    return "dddd"

@app.route('/list/')
def my_list():
    return 'list'


if __name__ == '__main__':
    app.run()

