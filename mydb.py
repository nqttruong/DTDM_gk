import pymysql

# Thiết lập kết nối ban đầu với MySQL mà không chỉ định cơ sở dữ liệu
dataBase = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'CSDL2021',

)

# Tạo một con trỏ để thực hiện các truy vấn
cursorObject = dataBase.cursor()
# Tạo cơ sở dữ liệu
# cursorObject.execute("CREATE DATABASE my_database_qlcf")

print("All Done")
