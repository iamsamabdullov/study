import time
from datetime import datetime

start= datetime(datetime.now().year,datetime.now().month, datetime.now().day, 9)
finish= datetime(datetime.now().year,datetime.now().month, datetime.now().day, 18)

hosts = 'C:\Windows\System32\drivers\etc\hosts'
hosts = "hosts.txt"

redirect = '127.0.0.1'

blocked = ["www.vk.com", "vk.com"]

while True:
    if start < datetime.now() < finish:
        print('limited')

        with open(hosts, 'r+') as file:
            src = file.read()
            for site in blocked:
                if site in src:
                    pass
                else:
                    file.write(f'{redirect}{site}\n')
    else:


        with open(hosts, "r+") as file:
            src = file.readlines()
            file.seek(0)

            for line in src:
                if not any(site in line for site in blocked):
                    file.write(line)
            file.truncate()
        print('is open')
    time.sleep(5)
