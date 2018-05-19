#encoding:utf-8

from flask_script import Manager


DBmanager = Manager()

@DBmanager.command
def init():
    print 'sql init success'

@DBmanager.command
def migraate():
    print 'move'