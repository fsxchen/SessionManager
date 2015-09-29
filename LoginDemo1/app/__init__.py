#!/usr/bin/env python
#coding:utf-8
import os, sys
base_dir = os.path.dirname(os.path.abspath(os.getcwd()))
sys.path.append(os.path.join(base_dir, "server"))

from flask import Flask, request, flash, redirect, render_template, make_response
app = Flask(__name__)


@app.route('/', methods = ['GET', 'POST'])
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "admin" and password == "admin":
            resp = make_response(render_template('login.html'))
            resp.set_cookie('username', username)
            resp.set_cookie('password', password)
            return resp
        else:
            # flash("Error!")
            pass
    return render_template('login.html')

@app.route('/auth_page', methods = ['GET'])
def auth_page():
    return render_template('auth_page.html', username="xx", password="yy")


@app.route('/logout', methods = ['GET'])
def logout():
    return render_template('logout.html')