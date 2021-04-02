from flask import Flask 
from flask import request
from flask import render_template
from flask import session
import mysql.connector
import pymysql.cursors
import pymysql
# from django.db import connection

app = Flask(__name__,static_folder="static",static_url_path="/")
app.config['SECRET_KEY'] = 'ricetia' 

@app.route("/")
def index(): 
    if 'username' in session:
        return render_template("member.html")
    return render_template("system.html")

@app.route("/member")
def member():
    name = session["name"]
    if 'username' not in session:
        return render_template("system.html")
    return render_template("member.html",data=name)

@app.route("/error",methods=['GET'])
def error():
    message = session["error"]
    return render_template("error.html",data=message)

@app.route("/signin", methods=["POST"])
def signin ():
    username = request.form["username"]
    password = request.form["password"]
    
    signup = pymysql.connect(
        host='localhost',
        user='root',
        password='ricetia',
        db='website',
        )
    with signup.cursor() as cursor:
        mysqlsave = "SELECT `password`,`name` FROM `user` WHERE `username`=%s"
        cursor.execute(mysqlsave,username)
        result = cursor.fetchall()
    signup.close()

    if len(result) > 0 :
        test_password = result[0][0]
        name = result[0][1]
        if test_password == password :
            session["name"] = name
            session["username"] = username
            session["password"] = password
            return render_template("member.html",data=name)
        else :
            error = "帳號或密碼輸入錯誤"
            session["error"] = error
            return render_template("error.html",data=error)
    else :
        error = "帳號或密碼輸入錯誤"
        session["error"] = error
        return render_template("error.html",data=error)
    

@app.route("/signout")
def signout ():
    del session["name"]
    del session["username"]
    del session["password"]
    return render_template("system.html")

@app.route("/signup", methods=["POST"])
def signup ():
    signup = pymysql.connect(
        host='localhost',
        user='root',
        password='ricetia',
        db='website',
        cursorclass=pymysql.cursors.DictCursor #以字典方式儲存
        )

    name = request.form["username"]
    username = request.form["registered_username"]
    password = request.form["registered_password"]

    with signup.cursor() as cursor:
        mysqldata = "SELECT `username` FROM `user` WHERE `username`=%s"
        cursor.execute(mysqldata,username)
        whitelist = cursor.fetchall()
    signup.close()

    if len(whitelist) < 1 :
        signup = pymysql.connect(
        host='localhost',
        user='root',
        password='ricetia',
        db='website',
        )
        with signup.cursor() as cursor:
            mysqlsave = "INSERT INTO user (name,username,password) VALUES (%s,%s,%s)"
            cursor.execute(mysqlsave,(name,username,password))
            signup.commit()
        signup.close()
        return render_template("system.html")
    else :
        error = "帳號已經被註冊過"
        return render_template("error.html",data=error)

  
app.run(port=3000)
