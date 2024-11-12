from app import app
from flask import render_template, url_for


@app.route("/")
def homepage():
    userTest = 'User Test'
    phone = 00000

    data = {
        'userTest': userTest,
        'phone': phone
    }

    return render_template('index.html', data=data)


@app.route("/new/")
def newPage():
    return 'New Page'