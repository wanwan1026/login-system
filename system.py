from flask import Flask 
from flask import request
from flask import render_template
from flask import session
import mysql.connector
import pymysql.cursors
import pymysql
from flask import jsonify

app = Flask(__name__,static_folder="static",static_url_path="/")
app.config['SECRET_KEY'] = 'ricetia' 

@app.route("/")
def index(): 
    if 'name' in session:
        return render_template("member.html",data=session["name"])
    else :
        return render_template("system.html")

@app.route("/member")
def member():
    if 'username' not in session:
        return render_template("system.html")
    else :
        return render_template("member.html",data=session["name"])

@app.route("/error")
def error():
    return render_template("error.html")

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
        mysqlact = "SELECT `password`,`name` FROM `user` WHERE `username`=%s"
        cursor.execute(mysqlact,username)
        result = cursor.fetchall()
    signup.close()

    if len(result) > 0 :
        if result[0][0] == password :
            session["name"] = result[0][1]
            session["username"] = username
            session["password"] = password
            return render_template("member.html",data=session["name"])
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
    registered_name = request.form["registered_name"]
    registered_username = request.form["registered_username"]
    registered_password = request.form["registered_password"]

    signup = pymysql.connect(
        host='localhost',
        user='root',
        password='ricetia',
        db='website',
        cursorclass=pymysql.cursors.DictCursor #以字典方式儲存
        )
    with signup.cursor() as cursor:
        mysqldata = "SELECT `username` FROM `user` WHERE `username`=%s"
        cursor.execute(mysqldata,registered_username)
        result = cursor.fetchall()
    
    if len(result) < 1 :
        with signup.cursor() as cursor:
            mysqlact = "INSERT INTO user (name,username,password) VALUES (%s,%s,%s)"
            cursor.execute(mysqlact,(registered_name,registered_username,registered_password))
            signup.commit() #資料上傳
        return render_template("system.html")
    else :
        error = "帳號已經被註冊過"
        return render_template("error.html",data=error)
    
    signup.close() #把資料庫關起來

@app.route("/api/users")
def users():
    result = ""
    check_username = request.args.get("username","")
    
    signup = pymysql.connect(
        host='localhost',
        user='root',
        password='ricetia',
        db='website',
        cursorclass=pymysql.cursors.DictCursor #以字典方式儲存
        )
    with signup.cursor() as cursor:
        mysqlact = "SELECT `id`,`name`,`username` FROM `user` WHERE `username`=%s"
        cursor.execute(mysqlact,check_username)
        result = cursor.fetchall()
    
    if len(result) > 0 :
        result = {'data':result[0]}
        return jsonify(result)
    else :
        result = {'data':'null'}
        return jsonify(result)
    
    signup.close()

app.run(port=3000)
