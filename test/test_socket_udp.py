# -*- coding: utf-8 -*-
import commands  # 执行系统命令模块
import json
from socket import *
import time

from datetime import datetime

import thread

HOST = '192.168.24.56'
PORT = 5140


def tcp_test():
    s = socket( AF_INET, SOCK_STREAM )  # 定义socket类型，网络通信，TCP
    s.bind( (HOST, PORT) )  # 套接字绑定的IP与端口
    s.listen( 1 )  # 开始TCP监听,监听1个请求
    while 1:
        conn, addr = s.accept()  # 接受TCP连接，并返回新的套接字与IP地址
        print'Connected by', addr  # 输出客户端的IP地址
        while 1:
            data = conn.recv( 1024 )  # 把接收的数据实例化
            cmd_status, cmd_result = commands.getstatusoutput(
                data )  # commands.getstatusoutput执行系统命令（即shell命令），返回两个结果，第一个是状态，成功则为0，第二个是执行成功或失败的输出信息
            if len( cmd_result.strip() ) == 0:  # 如果输出结果长度为0，则告诉客户端完成。此用法针对于创建文件或目录，创建成功不会有输出信息
                conn.sendall( 'Done.' )
            else:
                conn.sendall( cmd_result )  # 否则就把结果发给对端（即客户端）
    conn.close()

rec_address = {}
def udp_test(threadName, delay):
    # type: () -> object
    s = socket( AF_INET, SOCK_DGRAM )
    s.bind( (HOST, PORT) )
    print '...waiting for message..'
    while True:
        data, address = s.recvfrom( 1024 )
        # print address[0]
        rec_address[address[0]] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # print rec_address
    s.close()


# 每分钟写入文件一次
def save_date(threadName, delay):
    while True:
        time.sleep(300)
        fo = open('/Users/xiong/Desktop/reciveips.txt','w+')
        for key in rec_address:
            ip = str(key)
            # print 'ip-----',ips
            ip_date = str(rec_address[key])
            fo.write(ip+':'+ip_date+'\n')
        # fo.write(json.loads(rec_address))
        fo.close()
        # print 'save_date------',rec_address


try:
    thread.start_new_thread( udp_test, ("Thread-1", 2,) )
    thread.start_new_thread( save_date, ("Thread-2", 4,) )
except:
    print "Error: unable to start thread"

while 1:
    pass
