from flask import Flask 
from flask import request
from flask import render_template
from flask import session

app = Flask(__name__,static_folder="static",static_url_path="/")
app.config['SECRET_KEY'] = 'ricetia' 

@app.route("/")
def index(): 
    if 'IDnumber' in session:
        return render_template("member.html")
    return render_template("system.html")

@app.route("/member")
def member():
    if 'IDnumber' not in session:
        return render_template("system.html")
    return render_template("member.html")

@app.route("/error")
def error():
    return render_template("error.html")

@app.route("/signin", methods=["POST"])
def signin ():
    IDnumber = request.form["IDnumber"]
    password = request.form["password"]
    whitelist = {"test":"test"}
    for key,value in whitelist.items():
        if IDnumber == key :
            if password == value :
                session["IDnumber"] = IDnumber
                session["password"] = password
                return render_template("member.html")
            else :
                return render_template("error.html")
        else :
            return render_template("error.html")

@app.route("/signout")
def signout ():
    del session["IDnumber"]
    del session["password"]
    return render_template("system.html")



#啟動網站伺服器，可透過port參數指定埠號
app.run(port=3000)
