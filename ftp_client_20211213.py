


###if current time is between 10:00:00 and 11:00:00 then down load file
from datetime import datetime
from os import path
class TimeManager:
    def __init__(self, timelist):
        self.timelist = timelist

    def checkCurrentTimer():
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Current Time =", current_time)
        today11am = now.replace(hour =11,minute=0,second=0)
        today12am = now.replace(hour =12,minute=0,second=0)
        if now>today11am and now<today12am :
            return True
        else:
            return False


from time import sleep
from ftpManager.ftp_test import MyFtp_moveFile_byName, MyFtpParams,MyFtp_getFileBytes,MyFtp_downloadFile,MyFtp_downloadFile_byName
import os

# HOST = "test.rebex.net"
HOST = "127.0.0.1"
PORT = 21
USR = 'user'
PASSWORD = 'password'

if __name__ == '__main__':
    timelist = []
    timecheck = TimeManager(timelist)

    while(True):
        if timecheck.checkCurrentTimer:
            ###download file
            ftp_params = MyFtpParams()
            ftp_params.url = HOST
            ftp_params.port = 21
            ftp_params.pwd = PASSWORD
            ftp_params.user = USR
            ftp_params.cwd = "works"
            ftp_params.path =  os.getcwd()+"/ftp_files/"

            filename = 'readme.txt'

            rsp = MyFtp_downloadFile_byName(filename=filename,ftpParams=ftp_params)
            if rsp:
                ftp_params.tocwd = "ok"
                MyFtp_moveFile_byName(filename = filename,ftpParams=ftp_params)

            ###open file
            path = os.getcwd()+"/ftp_files/"
            f = open(path+filename,"r")
            print(f.read())


        sleep(10)
