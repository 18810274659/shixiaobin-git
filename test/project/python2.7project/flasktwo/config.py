#encoding: utf-8

DIALECT = 'mysql'
DRIVER = 'mysqldb'
USERNAME = 'root'
PASSWORD = '123456'
HOST = '127.0.0.1'
POST = '3306'
DATABASE = 'db_demo3'

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT,DRIVER,USERNAME,PASSWORD
                                                                       ,HOST,POST,DATABASE)

SQLALCHEMY_TRACK_MODIFICATIONS = False