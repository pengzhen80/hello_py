import http.server
import socketserver
import socketserver
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

import urllib
import xml.etree.ElementTree as ET

import logging

dataToSend = []
form = '''<!DOCTYPE html>
  <title>Message Board</title>
  <form method="POST">
    <textarea name="message"></textarea>
    <br>
    <button type="submit">Post it!</button>
  </form>
  <pre>
{}
  </pre>
'''

from time import sleep
import time
def writeToLog(logname,data):
    log_file = open("./api_logs/"+logname+".txt","a+",encoding='UTF-8')
    log_file.write(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
    log_file.write(":"+data)
    log_file.write("\n")
    # log_file.close()
    

class sendCell:
    def __init__(self):
            # self.size = 0
            self.barcode = ''     
            self.name = ''     
            self.telphone = ''
            self.logistics = ''     

def my_decode_data(data):
    xml_data = data['Data']
    str_xml_data = xml_data[0]
    root = ET.fromstring(str_xml_data)
    print(root.tag, '\n')
    dataToSend = []
    for shipment in root:
        no_barcode_1 = ""
        no_barcode_2 = ""
        name = ""
        telphone = ""
        logistics = ""
        for child in shipment:
            # print(child.tag,child.text)
            if child.tag == 'NO_ECCODE1':
                no_barcode_1 = child.text
            if child.tag == 'NO_ECCODE2':
                no_barcode_2 = child.text
            if child.tag == 'NM_ORDER':
                name = child.text
            if child.tag == 'ID_TELCODE':
                telphone = child.text
            if child.tag == 'NO_LGCODE':
                logistics = child.text
        cell = sendCell()
        cell.barcode = no_barcode_1+no_barcode_2
        cell.name = name
        cell.telphone = telphone
        cell.logistics = logistics
        # cell.size = len(cell.name+cell.telphone+cell.barcode)
        # print(cell.size)
        print(cell.barcode,",",cell.telphone,",",cell.name,",",cell.logistics)
        # print(len(cell.barcode),",",len(cell.telphone),",",len(cell.name),",",len(cell.logistics))
        if((len(cell.barcode) == 25) and (len(cell.telphone) == 3) and (len(cell.name) > 0) and (len(cell.logistics)>0)):
            dataToSend.append(cell)

    # for ds in dataToSend:
    #     print(ds.barcode)
    #     print(ds.name)
    #     print(ds.telphone)
        # print(ds.logistics)
    return dataToSend


reply_form = '''
<?xml version="1.0" encoding="UTF-8"?>
<Doc>
<ShipmentNos>
<NO_LGCODE>123123212321245312</NO_LGCODE>
<ErrorCode>000</ErrorCode>
<ErrorMessage>成功</ErrorMessage>
</ShipmentNos>
<ShipmentNos>
<NO_LGCODE>123123212321245312</NO_LGCODE>
<ErrorCode>000</ErrorCode>
<ErrorMessage> 成功 </ErrorMessage>
</ShipmentNos>
</Doc>
'''

REPLY_FORM_HEAD = '''
<?xml version="1.0" encoding="UTF-8"?>
<Doc>
'''
REPLY_FORM_TAIL = '''
</Doc>
'''
REPLY_FORM_BODY_HEAD = '''
<ShipmentNos>
<NO_LGCODE>'''

REPLY_FORM_BODY_END ='''</NO_LGCODE>
<ErrorCode>000</ErrorCode>
<ErrorMessage>成功</ErrorMessage>
</ShipmentNos>
'''




class TestHttpHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # First, send a 200 OK response.
        self.send_response(200)

        # Then send headers.
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

        # 2. Put the response together out of the form and the stored messages.
        # mesg = form.format("n".join(memory))
        # self.wfile.write(mesg.encode())
        # 3. Send the response.

    def do_POST(self):
        # How long was the message?
        length = int(self.headers.get('Content-length', 0))

        # Read the correct amount of data from the request.
        # data = self.rfile.read(length).decode()
        data = urllib.parse.parse_qs(self.rfile.read(length).decode('utf-8'))
        # print(data)
        #write to log
        # print(data)
        writeToLog(log_name,str(data))
        # logging.info(data)
        # print(type(data))
        # print(data.values())
        # for key in data.keys():
        #     print(key,'/n')
                
        data_multi = my_decode_data(data)

        # myreply_body = ''''''
        # for data in data_multi:
        #     myreply_body += REPLY_FORM_BODY_HEAD+data.logistics+REPLY_FORM_BODY_END
        # myreply = REPLY_FORM_HEAD+myreply_body+REPLY_FORM_TAIL
        # self.wfile.write(myreply.encode("utf-8"))

        try:
            dataToSend = ""
            dataToSendSize = len(data_multi)        
            # print(dataToSendSize)
            if(dataToSendSize < 10):
                dataToSend += '000'
            elif(dataToSendSize < 100):
                dataToSend += '00'
            elif(dataToSendSize <1000):
                dataToSend+='000'
            dataToSend += str(dataToSendSize)
            # print(dataToSend)
            #   writeToLog(log_name,dataToSend)

            tmp_today = date.today()
            tmp_today_date = tmp_today.strftime("%d-%m-%Y")

            for data in data_multi:
                #write to db
                db_mysql_test.db_mysql_insertdata(db_conn,name=data.name,barcode=data.barcode,phone=data.telphone,date=tmp_today_date)
                #format for warehouse system
                dataToSend+=data.barcode+data.telphone+data.name+","
                # print(dataToSend)
            dataToSend = dataToSend[:-1]
            print(dataToSend)
            try:
                my_client.send(str(dataToSend).encode())
            except Exception as ex:
                print(ex)
        except Exception as ex:
            print(ex)

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        myreply_body = ''''''
        for data in data_multi:
            myreply_body += REPLY_FORM_BODY_HEAD+data.logistics+REPLY_FORM_BODY_END
        myreply = REPLY_FORM_HEAD+myreply_body+REPLY_FORM_TAIL

        self.wfile.write(myreply.encode("utf-8"))


    def do_PUT(self):
        self.send_response(400)
        self.end_headers()

    def do_DELETE(self):
        self.send_response(400)
        self.end_headers()


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

PORT = 443

from datetime import date
import db_mysql_test

if __name__ == '__main__':
    my_client = MyLocalClient()
    my_client.init()

    today = date.today()
    log_name = today.strftime("%d-%m-%Y")

    db_conn = db_mysql_test.db_mysql_init()

    with socketserver.TCPServer(("192.168.8.2", PORT), TestHttpHandler) as httpd:
        print("serving at port", PORT)
        # if(httpd.verify_request(request=))
        httpd.serve_forever()
