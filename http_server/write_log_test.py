from time import sleep
import time
def writeToLog(logname,data):
    log_file = open("./web_logs/"+logname+".txt","w+")
    log_file.write(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
    log_file.write(":"+data)
    log_file.write("\n")
    log_file.close()


from datetime import date
today = date.today()
log_name = today.strftime("%d-%m-%Y")
writeToLog(log_name,data = "hello")