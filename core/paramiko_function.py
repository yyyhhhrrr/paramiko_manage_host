#!/usr/bin/env python
# coding:utf-8
# Author:Yang

import paramiko

class Paramiko_Funciton(object):

      def __init__(self,hostname,password,username):
          self.hostname=hostname
          self.passowrd=password
          self.username=username

      def ssh_cmd(self,cmd):
          ssh=paramiko.SSHClient()
          ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
          ssh.connect(hostname=self.hostname,port=22,username=self.username,password=self.passowrd)

          stdin,stdout,stderr=ssh.exec_command(cmd)
          res,err=stdout.read(),stderr.read()
          result = res if res else err
          ssh.close()
          return result.decode()

      def sftp_cmd(self,cmd):
          # cmd 传进来要先变成一个列表
          cmd_split=cmd.split()
          transport=paramiko.Transport((self.hostname,22))
          transport.connect(username=self.username,password=self.passowrd)

          sftp=paramiko.SFTPClient.from_transport(transport)
          cmd_string=cmd_split[0]


          if hasattr(sftp,cmd_string):
              if cmd_string == 'get':
                  cmd_remote_path = cmd_split[1]
                  cmd_local_path = cmd_split[2]
                  sftp.get(cmd_remote_path,cmd_local_path)
                  print("远程主机%s的远程文件:%s 已下载到本地:%s"%(self.hostname,cmd_remote_path,cmd_local_path))

              else:
                  cmd_remote_path = cmd_split[2]
                  cmd_local_path = cmd_split[1]
                  sftp.put(cmd_local_path,cmd_remote_path)
                  print("本地文件:%s 已上传到远程主机%s:%s"%(cmd_local_path,self.hostname,cmd_remote_path))
              transport.close()
          else:
              print("请输入正确指令")



