# # -*- coding: utf-8 -*-
# # !/usr/bin/python
# # coding=utf-8
# import time
# import threading
# import socket
# import os
#
#
# class Client():
#     def __init__(self):
#         address = ('127.0.0.1', 8086)
#         s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         s.connect(address)
#         fn = 'test.zip'
#         ff = os.path.normcase(fn)
#
#         try:
#             f = open(fn, 'rb')
#             sendFile = SendFile(s, f)
#             sendFile.start()
#             print('start to send file.')
#         except IOError:
#             print('open err')
#
#
# class SendFile(threading.Thread):
#     def __init__(self, sock, file):
#         threading.Thread.__init__(self)
#         self.file = file
#         self.sock = sock
#
#     def run(self):
#         print(self.file)
#         BUFSIZE = 1024
#         count = 0
#         name = self.file.name + '\r'
#
#          # 前1k字节是为了给服务端发送文件名 一定要加上'\r',不然服务端就不能readline了
#         for i in range(1, BUFSIZE - len(self.filename) - 1):
#             name += '?'
#         print(name)
#         self.sock.send(name)
#         while True:
#             print(BUFSIZE)
#             fdata = self.file.read(BUFSIZE)
#             if not fdata:
#                 print('no data.')
#                 break
#             self.sock.send(fdata)
#             count += 1
#             if len(fdata) != BUFSIZE:
#                 print('count:' + str(count))
#                 print(len(fdata))
#             nRead = len(fdata)
#
#         print('send file finished.')
#         self.file.close()
#         self.sock.close()
#         print('close socket')
#
# c = Client()
import os
import socket
from scrapy import cmdline


try:
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM);
    print("create socket succ!")

    sock.bind(('0.0.0.0',8001))
    print('bind socket succ!')

    sock.listen(5)
    print('listen succ!')

except:
    print("init socket error!")

while True:
    print("listen for client...")
    conn,addr=sock.accept()
    print("get client")
    print(addr)

    conn.settimeout(30)
    szBuf=conn.recv(1024)
    print("recv:"+str(szBuf,'utf8'))

    if "0"==szBuf:
        conn.send(b"exit")
    else:
        conn.send(b"welcome client\n")
        # conn.close()
        #os.system("scrapy crawl ysu_spider")
        os.system("python main.py %s" % ('"'+str(szBuf,'utf8')+'"').replace(' ', ''))
        conn.send(b"spider done\n")

    conn.close()
    print("end of servive")

# args={
#     'num' : 5,
#     'b2e' : ["2019-09-22","2019-01-01"],
#     'urls' : ["http://ysu.edu.cn/index/xwtx.htm"]
# }
#
# os.system("python main.py %s" % str(args).replace(' ',''))