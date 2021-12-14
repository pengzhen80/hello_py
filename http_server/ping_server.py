import os
from time import sleep
from datetime import datetime

count = 0
totalpingCount = 0
while True:
    hostname = "211.20.149.130" #example
    response = os.system("ping " + hostname)
    totalpingCount = totalpingCount+1
    #and then check the response...
    if response == 0:
        print(hostname, 'is up!')
    else:
        print(hostname, 'is down!')
        count = count+1
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    print("total ping count is ",totalpingCount)
    print("lost times is ",count)
    sleep(60)