import time
from datetime import datetime as dt
print('hello')
hosts_path = r'/private/etc/hosts'
hosts_temp = '/Users/xiaodonghuo/PycharmProjects/web_blocker/hosts'
redirect = '127.0.0.1'
websites_list = ['www.youtube.com', 'youtube.com']
file = open('/private/etc/hosts','r')
print(file)

while True:
    if 8<dt.now().hour<=23:
        print(dt.now())
        print('now it is day time')
        with open(hosts_path,'r+') as file:
            content = file.read()
            for website in websites_list:
                if website in content:
                    pass
                else:
                    file.write('\n'+redirect+ '\t' + website)
            print(content)
    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websites_list):
                    file.write(line)
            file.truncate()
        print('time not in range')
    time.sleep(3)
