from ctypes import sizeof
import socket
from time import sleep
class MyLocalClient:
    LOCAL_PORT = 4431
    LOCAL_HOST = '127.0.0.1'
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def init(self):
        self.s.connect((self.LOCAL_HOST, self.LOCAL_PORT))
        return 
    def send(self,data):
        self.s.send(data)

    def init_alwaysConenct(self):
        connected = False  
        while not connected:  
            # attempt to reconnect, otherwise sleep for 2 seconds  
            try:  
                self.s.connect((self.LOCAL_HOST, self.LOCAL_PORT))  
                connected = True  
                print( "re-connection successful" )  
            except socket.error:  
                sleep( 1 ) 

if __name__ == '__main__':
    my_client = MyLocalClient()
    my_client.init_alwaysConenct()