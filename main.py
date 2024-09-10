# from flask import Flask, render_template
#
# app = Flask(__name__)
#
# @app.route("/")
# def index():
#     return render_template('index.html')
#
# @app.route("/index")
# def home():
#     return render_template('index.html')
#
# @app.route("/about")
# def about():
#     return render_template('about.html')
#
# @app.route("/contact")
# def contact():
#     return render_template('contact.html')
#
# @app.route("/post")
# def post():
#     return render_template('post.html')
#
# app.run(debug=True)


import pymysql

pymysql.install_as_MySQLdb()

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# from flask import Flask, render_template, request
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/dbname'

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:@localhost@server/first_website"
db = SQLAlchemy(app)

'''sno, name, phone_num, msg, date, email'''


class Contact(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    phone_num = db.Column(db.String(120), nullable=False)
    msg = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    email = db.Column(db.String(20), nullable=False)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/index")
def home():
    return render_template('index.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if (request.method == 'POST'):
        ''''Add entry to the database'''
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        massage = request.form.get('massage')
        entry = Contact(name=name, phone_num=phone, msg=massage, email=email)
        db.session.add(entry)
        db.session.commit()

    return render_template('contact.html')


@app.route("/post")
def post():
    return render_template('post.html')


app.run(debug=True)
