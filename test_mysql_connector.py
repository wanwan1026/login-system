import mysql.connector
import pymysql.cursors
import pymysql

check_username = 'mango'
# check_username = request.form["check_username"]

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
else :
  result = {'data':'null'}
# return jsonify(result)
print(result)


# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="ricetia",
# )

# print(mydb)

#mysql -h localhost -u root -p

# name = request.form["username"]
# username = request.form["registered_username"]
# username = 'rice'
# password = request.form["registered_password"]
# password = 'rice'

# registered = pymysql.connect(
#   host='localhost',
#   user='root',
#   password='ricetia',
#   db='website',
#   )
# with registered.cursor() as cursor:
#     mysqlsave = "SELECT `password`,`name` FROM `user` WHERE `username`=%s"
#     cursor.execute(mysqlsave,username)
#     result = cursor.fetchall()
# registered.close()

# print(result[0][1])

# result = result[0][0]

# # result = result.__str__()
# # result = result[3:-5]

# if result == password :
#   print("成功登陸")

# user_test_index = 0
# for i in range(len(whitelist)) :
#   user_test = whitelist[i]["username"]
#   username = '2132132123'
#   if username != user_test:
#     user_test_index=user_test_index+0
#   else :
#     user_test_index=user_test_index+1

# print(user_test_index)
# if user_test_index == 0 :
#   a=132
#   print(a)




# with registered.cursor() as cursor:
#   name = '草莓'
#   username = 'abc'
#   password = '123'
#   mysqlsave = "INSERT INTO user (name,username,password) VALUES (%s,%s,%s)"
#   cursor.execute(mysqlsave,(name,username,password))
#   registered.commit()
#   registered.close()

# for i in range(len(whitelist)) :
#   user_test = whitelist[i]["username"]
#   print(user_test)
#   username = 'abc'

# while 
  # print(user_test)
#   name = request.form["username"]
#   username = request.form["registered_username"]
  # username = 'abc'
#   password = request.form["registered_password"]
  # if username != user_test :
  #   print(user_test)
#     return render_template("error.html")
#   else :
#     registered = pymysql.connect(
#     host='localhost',
#     user='root',
#     password='ricetia',
#     db='website',
#     )
#     with registered.cursor() as cursor:
#       mysqldata = "INSERT INTO user (`name`,`username`,`password`) VALUES (name,username,password)"
#       cursor.execute(mysqldata)
#     registered.close()


    # signup = pymysql.connect(
    # host='localhost',
    # user='root',
    # password='ricetia',
    # db='website',
    # cursorclass=pymysql.cursors.DictCursor #以字典方式儲存
    # )

    # with signup.cursor() as cursor:
    #     mysqldata = "SELECT `username` FROM `user`"
    #     cursor.execute(mysqldata)
    #     whitelist = cursor.fetchall()
    # signup.close()

    # name = request.form["username"]
    # username = request.form["registered_username"]
    # password = request.form["registered_password"]

    # if username != whitelist[0] :
    #   signup = pymysql.connect(
    #     host='localhost',
    #     user='root',
    #     password='ricetia',
    #     db='website',
    #     )
    #   with signup.cursor() as cursor:
    #       mysqlsave = "INSERT INTO user (name,username,password) VALUES (%s,%s,%s)"
    #       cursor.execute(mysqlsave,(name,username,password))
    #       signup.commit()
    #   signup.close()
    #   return render_template("system.html")
    # else :
    #   error = "帳號已經被註冊過"
    #     return render_template("error.html",data=error)


# @app.route("/signup", methods=["POST"])
# def signup ():
#     signup = pymysql.connect(
#     host='localhost',
#     user='root',
#     password='ricetia',
#     db='website',
#     cursorclass=pymysql.cursors.DictCursor #以字典方式儲存
#     )


#     with signup.cursor() as cursor:
#         mysqldata = "SELECT `username`,`password` FROM `user`"
#         cursor.execute(mysqldata)
#         whitelist = cursor.fetchall()
#     signup.close()

#     name = request.form["username"]
#     username = request.form["registered_username"]
#     password = request.form["registered_password"]
#     user_test_index = 0
#     for i in range(len(whitelist)) :
#         user_test = whitelist[i]["username"]
#         if username != user_test:
#             user_test_index=user_test_index+0
#         else :
#             user_test_index=user_test_index+1
#     if user_test_index == 0 :
#         signup = pymysql.connect(
#             host='localhost',
#             user='root',
#             password='ricetia',
#             db='website',
#             )
#         with signup.cursor() as cursor:
#             mysqlsave = "INSERT INTO user (name,username,password) VALUES (%s,%s,%s)"
#             cursor.execute(mysqlsave,(name,username,password))
#             signup.commit()
#         signup.close()
#         return render_template("system.html")
#     else :
#         error = "帳號已經被註冊過"
#         return render_template("error.html",data=error)


    



