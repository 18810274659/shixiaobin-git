#encoding:utf-8

from flask import Flask
from exts import db
import config
from modls import Article



app = Flask(__name__)

app.config.from_object(config)

db.init_app(app)






@app.route('/')
def helloword():
    return 'hello word'

if __name__ == '__main__':
    app.run()