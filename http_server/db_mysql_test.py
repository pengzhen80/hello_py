import pymysql
import pymysql.cursors
from datetime import date
from datetime import timedelta

# 資料庫參數設定
db_settings = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "12345678",
    "db": "db_web_server",
    "charset": "utf8"
}

cmd_createTable = '''
create table table_api_data(
sn integer auto_increment primary key,
name char(20),
barcode char(50),
phone char(20),
date char(50)
);
'''
cmd_insertData = '''
insert into table_api_data(name,barcode,phone,date) values('{name}','{barcode}','{phone}','{date}');
'''
cmd_searchData_byDate = '''
select * from table_api_data where date = '{date}'
'''

def db_mysql_init():
    try:
        # 建立Connection物件
        conn = pymysql.connect(**db_settings)
        return conn
    except Exception as ex:
        print(ex)
def db_mysql_createTable(conn):
    try:
        with conn.cursor() as cursor:
            command = cmd_createTable
            cursor.execute(command)
            conn.commit()
    except Exception as ex:
        print(ex)
        conn.connect()

def db_mysql_insertdata(conn, name, barcode, phone, date):
    try:
        # 建立Cursor物件
        with conn.cursor() as cursor:
            # 新增資料SQL語法
            # command = cmd_createTable
            # today = date.today()
            # today_date = today.strftime("%d-%m-%Y")
            command = cmd_insertData.format(
                name=name, barcode=barcode, phone=phone, date=date)
            print(command)
            cursor.execute(command)
            conn.commit()
    except Exception as ex:
        print(ex)
        conn.connect()
        try:
            with conn.cursor() as cursor:
            # 新增資料SQL語法
            # command = cmd_createTable
            # today = date.today()
            # today_date = today.strftime("%d-%m-%Y")
                command = cmd_insertData.format(
                    name=name, barcode=barcode, phone=phone, date=date)
                print(command)
                cursor.execute(command)
                conn.commit()
        except Exception as ex:
                print(ex)


def db_mysql_searchdata(conn,date):
    try:
        # 建立Cursor物件
        with conn.cursor() as cursor:
            command = cmd_searchData_byDate.format(date=date)
            print(command)
            cursor.execute(command)
            result = cursor.fetchall()
            print(result)
            return result
            # 儲存變更
            conn.commit()
    except Exception as ex:
        print(ex)
        conn.connect()
       



# conn = db_mysql_init()
# # today = date.today()
# # today_date = today.strftime("%d-%m-%Y")

# yesterday = date.today() - timedelta(days=4)
# yesterday_date = yesterday.strftime("%d-%m-%Y")
# print(yesterday_date)
# result = db_mysql_searchdata(conn = conn,date =yesterday_date)
# for data in result:
#     print(data)
#     # for sub_data in data:
#     #     print(sub_data)
#     print("name is :",data[1])
#     print("barcode is :",data[2])
#     print("phone is :",data[3])
#     print("date is :",data[4])