#encoding:utf-8

from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
import config

app = Flask(__name__)

app.config.from_object(config)
db = SQLAlchemy(app)

#zhong jian biao
article_tag = db.Table(
    'article_tag',
    db.Column('article_id',db.Integer,db.ForeignKey('article.id'),primary_key = True),
    db.Column('tag_id',db.Integer,db.ForeignKey('tag.id'),primary_key = True)
)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100),nullable = False)


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    title = db.Column(db.String(100),nullable = False)
    content = db.Column(db.Text,nullable = False)
    author_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    authon = db.relationship('User',backref=db.backref('article'))
    #duo dui duo  ,secondaru  = zhongjianbiao
    tags = db.relationship('Tag',secondary = article_tag,backref = db.backref('article'))

class Tag(db.Model):
    __tablename = 'tag'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)

db.create_all()

@app.route('/')
def index():

    #users = User(username = 'shixiaobin')
    #db.session.add(users)
    ##db.session.commit()
    #article = Article(title = 'aaa1',content = 'bbb1')
    #article.authon = User.query.filter(User.id == 1).first()
    #db.session.add(article)
    #db.session.commit()
    user = User.query.filter(User.username == 'shixiaobin').first()
    article = user.article
    for art in article:
        print art.title + "   "
    #db.session.add(article)
    #db.session.commit()

    #article = Article.query.filter(Article.title == 'aaa').first()
    #author_id = article.author_id
    #user = User.query.filter(User.id == author_id).first()
    #print user.username
    #result = Article.query.filter(Article.title == 'aaa')
    #print result;
    #xiugai updata
    #article = Article.query.filter(Article.title == 'aaa').first()
    #article.title = "new title"
    #db.session.commit()
    #delete
   # article = Article.query.filter(Article.title == 'new title').first()
    #db.session.delete(article)
    #db.session.commit()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)