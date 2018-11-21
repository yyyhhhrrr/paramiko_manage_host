#!/usr/bin/env python
# coding:utf-8
# Author:Yang


import json
import threading
from conf import setting
from core import paramiko_function
class Main_View(object):

     def __init__(self,username,password):
         self.username=username
         self.password=password
         self.host=[]
         self.host_pwd=[]
         self.username=[]
     def group_view(self):
         print('''
         
         -----------分组列表---------
         
         1.interface
         2.mycentos7
         ''')

         choice=int(input("请选择你要进入的主机组:"))
         if choice==1:
            self.happy_view()
         elif choice ==2:
            self.mycentos7_view()

     def mycentos7_view(self):
         with open(setting.BASE_DIR + "\\data\\host_data.txt", "r") as f:
             data = json.loads(f.read())
             self.host.append(data['host3']['hostname'])
             self.host_pwd.append(data['host3']['password'])
             self.username.append(data['host3']['username'])
         f.close()
         print('''
         ----------主机列表--------
         1.单独执行
         （1）%s
         2.批量执行
         '''%self.host[0])
         choice=int(input("请输入主机序号:"))
         if choice ==1:
             self.manage_view(0)
         elif choice ==2:
             self.mass_view()
         else:
             print("输入错误")

     def happy_view(self):
         with open(setting.BASE_DIR+"\\data\\host_data.txt","r") as f:
             data=json.loads(f.read())
             for i in range(1,3):
                 self.host.append(data['host%s'%i]['hostname'])
                 self.host_pwd.append(data['host%s'%i]['password'])
                 self.username.append(data['host%s'%i]['username'])


         f.close()


         print('''
         ------------主机列表--------
         1.单独执行
         2.批量执行
         ''')
         choice = int(input("请输入操作:"))
         if choice==1:
             print('''--------主机列表-----
             1.%s
             2.%s
             '''%(self.host[0],self.host[1]))
             choice2 = int(input("请选择主机:"))
             self.manage_view(choice2-1)
         elif choice ==2:
             self.mass_view()
         else:
             print("输入错误")


     def manage_view(self,index):
         print('''
         ------------%s 终端---------
         '''
        %self.host[index])
         p=paramiko_function.Paramiko_Funciton(self.host[index],self.host_pwd[index],self.username[index])
         while True:
             cmd=input(">>")
             if cmd.split()[0] != "get" and cmd.split()[0] !="put":
                 result=p.ssh_cmd(cmd)
                 print(result)
             else:
                 p.sftp_cmd(cmd)


     def mass_thread(self,index,cmd):
         print('''
         ----------%s--------
         '''%self.host[index])
         p=paramiko_function.Paramiko_Funciton(self.host[index],self.host_pwd[index],self.username[index])
         if cmd.split()[0] != "get" and cmd.split()[0] != "put":
             result = p.ssh_cmd(cmd)
             print(result)
         else:
             p.sftp_cmd(cmd)


     def mass_view(self):
         print('''
         ---------批量执行终端-------
         ''')
         while True:
             cmd=input(">>")
             for i in range(len(self.host)):
                 t=threading.Thread(target=self.mass_thread,args=(i,cmd,))
                 t.start()








