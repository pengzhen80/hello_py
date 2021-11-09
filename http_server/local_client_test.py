
class sendCell:
    def __init__(self):
            self.size = 0
            self.barcode = ''     
            self.name = ''     
            self.telphone = ''

from ctypes import sizeof
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

cell_send = sendCell()
cell_send.barcode = "1234567890123456789012345"
cell_send.telphone = "123"
cell_send.name = "pengzhen"
cell_send.size = len(cell_send.name+cell_send.telphone+cell_send.barcode)
print(cell_send.size)
data_multi = []

for i in range(1000):
    data_multi.append(cell_send)

if __name__ == '__main__':
    my_client = MyLocalClient()
    my_client.init()

    # dataToSend = cell_send.barcode+cell_send.telphone+cell_send.name
    dataToSend = ""
    dataToSendSize = len(data_multi)        
    print(dataToSendSize)
    if(dataToSendSize < 10):
        dataToSend += '000'
    elif(dataToSendSize < 100):
        dataToSend += '00'
    elif(dataToSendSize <1000):
        dataToSend+='000'
    dataToSend += str(dataToSendSize)
    print(dataToSend)

    for data in data_multi:
        dataToSend+=str(data.size)+data.barcode+data.telphone+data.name
    print(dataToSend)
    my_client.send(dataToSend.encode())

    
