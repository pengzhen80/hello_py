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

if __name__ == '__main__':
    my_client = MyLocalClient()
    my_client.init()
    my_client.send("hello".encode())

# while True:
#     outdata = input('please input message: ')
#     print('send: ' + outdata)
#     s.send(outdata.encode())
    
#     indata = s.recv(1024)
#     if len(indata) == 0: # connection closed
#         s.close()
#         print('server closed connection.')
#         break
#     print('recv: ' + indata.decode())
# s.recv()
# s.close()