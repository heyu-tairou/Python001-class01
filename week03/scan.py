import socket
import os
import threading
import time

IPList = []

def ping_ip(ip):  # 1、ping指定IP判断主机是否存活
    output = os.popen('ping -n 1 %s' % ip).readlines()  # 注：若在Linux系统下-n 改为 -c
    for w in output:
        if str(w).upper().find('TTL') >= 0:
            IPList.append(ip)
    print(output)

def ping_net(ip):  # 2、ping所有IP获取所有存活主机
    pre_ip = (ip.split('.')[:-1])
    for i in range(1, 256):
        add = ('.'.join(pre_ip)+'.'+str(i))
        threading._start_new_thread(ping_ip, (add,))
        time.sleep(0.01)


if __name__ == '__main__':
    ping_net(socket.gethostbyname(socket.gethostname()))
    for ip in IPList:
        print(ip)
