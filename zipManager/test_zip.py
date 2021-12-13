import os
import zipfile


# zipfile example
def zip_compress_dir_encrypt(path,pwd):
    zf = zipfile.ZipFile('{}.zip'.format(path), 'w', zipfile.ZIP_DEFLATED)
    
    for root, dirs, files in os.walk(path):
        for file_name in files:
            zf.write(os.path.join(root, file_name))
    zf.setpassword(pwd)

def zip_decompress_file_encrypted(path,pwd):
    with zipfile.ZipFile(path,'r') as myzip:
        for filename in myzip.namelist():
            with myzip.open(filename,pwd=pwd) as myfile:
                # print(myfile.read())
                return myfile.read()

def zip_list_zipfiles(file_path):
    zf = zipfile.ZipFile(file_path, 'r')
    print(zf.namelist())

if __name__ == '__main__':
    ## test funcs
    path = './zipfiles'
    pwd = "1234"
    zip_compress_dir_encrypt(path,pwd=pwd.encode("utf-8"))

    # path = "./zipfiles.zip"
    # zip_list_zipfiles(path)

    path = "./zipfiles.zip"
    contents = zip_decompress_file_encrypted(path,pwd.encode("utf-8"))
    print(contents)