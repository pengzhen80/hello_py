import db_mysql_test
import socket
class MyLocalClient:
    LOCAL_PORT = 4431
    LOCAL_HOST = '127.0.0.1'
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def init(self):
        self.s.connect((self.LOCAL_HOST, self.LOCAL_PORT))
        return 
    def send(self,data):
        self.s.send(data)

class sendCell:
    def __init__(self):
            self.barcode = ''     
            self.name = ''     
            self.telphone = ''

def searchDataByDate(conn,myDate):
    result = db_mysql_test.db_mysql_searchdata(conn,myDate)
    dataMulti = []
    for data in result:
        name = data[1]
        barcode = data[2]
        phone = data[3]
        cell = sendCell()
        cell.barcode = barcode
        cell.name = name
        cell.telphone = phone
        dataMulti.append(cell)
    return dataMulti

import sys
import random

if __name__ == '__main__':
    list_of_args = sys.argv
    # for data in list_of_args :
    #     print(data)
    search_date = list_of_args[1]
    print(search_date)

    db_conn = db_mysql_test.db_mysql_init()
    dataMulti = searchDataByDate(db_conn,search_date)

    my_client = MyLocalClient()
    my_client.init()

    dataToSend = ""
    for data in dataMulti:
        dataToSend+=data.barcode+data.telphone+data.name+","
    dataToSend = dataToSend[:-1]
    print(dataToSend)
    my_client.send(str(dataToSend).encode())

