import http.server
import socketserver
import socketserver
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

import urllib
import xml.etree.ElementTree as ET
import json

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

class sendCell:
    def __init__(self):
            self.barcode = ''     
            self.name = ''     
            self.telphone = ''     

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
        cell = sendCell()
        cell.barcode = no_barcode_1+no_barcode_2
        cell.name = name
        cell.telphone = telphone
        dataToSend.append(cell)

    for ds in dataToSend:
        print(ds.barcode)
        print(ds.name)
        print(ds.telphone)
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
<
ErrorCode> ErrorCode
<
ErrorMessage 成功 ErrorMessage
</ShipmentNos>
</Doc>
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
        print(data)
        # print(type(data))
        # print(data.values())
        # for key in data.keys():
        #     print(key,'/n')
        
        # dataToSend = my_decode_data(data)
        # my_client.send(str(dataToSend).encode())
        my_client.send(str(data).encode())

        # Extract the "message" field from the request data.
        # message = parse_qs(data)["name"][0]

        # # Escape HTML tags in the message so users can't break world+dog.
        # message = message.replace("<", "&lt;")

        # Store it in memory.
        # memory.append(message)

        # 1. Send a 303 redirect back to the root page.
        self.send_response(303)
        self.send_header('Location', '/')
        # self.send_header("reply", reply_form.encode("utf-8"))
        self.end_headers()
        self.wfile.write(reply_form.encode("utf-8"))

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

PORT = 7000

if __name__ == '__main__':
    my_client = MyLocalClient()
    my_client.init()
    with socketserver.TCPServer(("192.168.8.2", PORT), TestHttpHandler) as httpd:
        print("serving at port", PORT)
        # if(httpd.verify_request(request=))
        httpd.serve_forever()
