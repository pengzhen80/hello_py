from ftplib import FTP
# HOST = "test.rebex.net"
# PORT = 21
# USR = 'demo'
# PASSWORD = 'password'
# ftp = FTP()
# ftp.connect(HOST,PORT)
# ftp.login(user = 'demo', passwd = 'password')
# ftp.cwd('pub/example')
# ftp.retrlines('LIST')

# path = './ftpfiles/'
# for name in ftp.nlst():
#     filenameToWrite = path + name
#     f= open(filenameToWrite,'wb')
#     filenameToRead = 'RETR '+name
#     # ftp.retrbinary(filenameToRead,f.write)
#     if name == 'readme.txt':
#         ftp.retrbinary(filenameToRead,f.write)
# ftp.quit()


class MyFtpParams:
    def __init__(self):
        self.url = ''
        self.path = ''
        self.port = 21
        self.user = ''
        self.pwd = ''


def MyFtp_downloadFile(ftpParams=MyFtpParams(), filePath):
    host = ftpParams.url
    port = ftpParams.port
    user = ftpParams.user
    pwd = ftpParams.pwd
    ftp = FTP()
    ftp.connect(host, port)
    ftp.login(user=user, passwd=pwd)
    ftp.cwd('pub/example')
    ftp.retrlines('LIST')

    path = './ftpfiles/'
    for name in ftp.nlst():
        filenameToWrite = path + name
        f = open(filenameToWrite, 'wb')
        filenameToRead = 'RETR '+name
        # ftp.retrbinary(filenameToRead,f.write)
        if name == 'readme.txt':
            ftp.retrbinary(filenameToRead, f.write)
    ftp.quit()
