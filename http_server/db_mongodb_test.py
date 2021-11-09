import pymongo
from datetime import date

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
 
dblist = myclient.list_database_names()
# dblist = myclient.database_names() 
# for tmp_db in dblist:
#     print(tmp_db)
    # print("数据库已存在！")
db_test = myclient["test"]
# for cols in db_test.list_collection_names():
#     print(cols)

# mydb = myclient["runoobdb"]
mycol = db_test["items"]

# mydict = { "name": "pengzhen", "phone": "123", "date": "27-10-2021" }
 
# x = mycol.insert_one(mydict) 

# mylist = [
#   { "name": "Taobao", "alexa": "100", "url": "https://www.taobao.com" },
#   { "name": "QQ", "alexa": "101", "url": "https://www.qq.com" },
#   { "name": "Facebook", "alexa": "10", "url": "https://www.facebook.com" },
#   { "name": "知乎", "alexa": "103", "url": "https://www.zhihu.com" },
#   { "name": "Github", "alexa": "109", "url": "https://www.github.com" }
# ]
 
# x = mycol.insert_many(mylist)

# for x in mycol.find():
#   print(x)
# myquery = { "name": "pengzhen" }
# for x in mycol.find(myquery):
#     print(x)


# collist = mydb. list_collection_names()
# if "sites" in collist:   # 判断 sites 集合是否存在
#   print("集合已存在！")

def db_mongodb_init():
    try:
        myclient = pymongo.MongoClient('mongodb://localhost:27017/')
        db_web_server = myclient["db_web_server"]
        return db_web_server
    except Exception as ex:
        print(ex)

def db_mongodb_insertdata(db_web_server,datas):
    try:
        col_items = db_web_server["items"]
        mylist = []
        today = date.today()
        today_date = today.strftime("%d-%m-%Y")
        for data in datas:
            mylist_cell = {"name":data.name,"phone":data.number,"barcode":data.barcode,"date":today_date}
            mylist.append(mylist_cell)
        col_items.insert_many(mylist)
    except Exception as ex:
        print(ex)

def db_mongodb_searchdata(db_web_server,date):
    try:
        col_items = db_web_server["items"]
        myquery = { "date": date }
        return col_items.find(myquery)
           
    except Exception as ex:
        print(ex)