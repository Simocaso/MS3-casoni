from config import app, mongo
from flask import Flask, redirect, url_for
import uuid
# , request, url_for
# from user.models (folder/file) import User (class in the file)
from user.models import User, Task


@app.route('/user/signup', methods=['POST'])
def signup():
    return User().signup() 


@app.route('/user/signout')
def signout():
    return User().signout()


@app.route('/user/login', methods=['POST'])
def login():
    return User().login() 


@app.route('/user/addTask', methods=['POST'])
def addTask():
    return Task().addTask()


@app.route('/delete_completed')
def delete_completed():
    mongo.db.tasks.delete_many({'complete_status' : True})
    return redirect(url_for('dashboard'))


@app.route('/delete_all')
def delete_all():
    mongo.db.tasks.delete_many({})
    return redirect(url_for('dashboard'))
