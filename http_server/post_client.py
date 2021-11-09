#-*-coding:UTF-8 -*-
import requests
import ast

my_data = {"name":"pengzhen"}

f= open("./web_logs/06-11-2021.txt",'r',encoding='UTF-8')

datas = f.read()
# print(datas)
data = datas.split("2021-11-07 21:15:35")
data = data[1]
# data = data.split("2021-11-07 21:01:13")
# data = data[0]
data = data[1:-1]

res = ast.literal_eval(data)

data_formal_1106 = res
r = requests.post("http://223.22.240.67:443",data = data_formal_1106)
print(r.headers)
print(r.content)