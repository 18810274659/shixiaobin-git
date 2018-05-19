#encoding: utf-8

from flask_script import Manager
from flask_script_demo import app
from db_scripys import DBmanager

manager = Manager(app)


@manager.command
def runserver1():
    print '11111'

manager.add_command('db',DBmanager)

if __name__  == '__main__':
    manager.run()