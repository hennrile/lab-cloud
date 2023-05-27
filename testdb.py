import mysql.connector
# Khai báo thông tin CSDL
mydb = mysql.connector.connect(
    user = 'root',
    password = '',
    host = 'localhost'
)
print(mydb)
#con trỏ
code = 'database_test'
mycursor = mydb.cursor(code)