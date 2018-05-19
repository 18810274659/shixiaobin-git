

#encoding:utf-8

from flask import Flask


app = Flask(__name__)

@app.route('/')
def helloword():
    return helloword

if __name__ == 'main':
    app.run(debug = True)