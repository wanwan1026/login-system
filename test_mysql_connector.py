import mysql.connector
import pymysql.cursors
import pymysql



# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="ricetia",
# )

# print(mydb)

#mysql -h localhost -u root -p

# name = request.form["username"]
# username = request.form["registered_username"]
username = 'rice'
# password = request.form["registered_password"]
password = 'rice'

registered = pymysql.connect(
  host='localhost',
  user='root',
  password='ricetia',
  db='website',
  )
with registered.cursor() as cursor:
    mysqlsave = "SELECT `password`,`name` FROM `user` WHERE `username`=%s"
    cursor.execute(mysqlsave,username)
    result = cursor.fetchall()
registered.close()

print(result[0][1])

result = result[0][0]

# result = result.__str__()
# result = result[3:-5]

if result == password :
  print("成功登陸")

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

    



