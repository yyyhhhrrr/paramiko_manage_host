#!/usr/bin/env python
# coding:utf-8
# Author:Yang

from conf import setting
import sys
import json
from core import main
BASE_DIR=setting.BASE_DIR

sys.path.append(BASE_DIR)

if __name__=='__main__':

    while True:
        username=input("请输入用户名:")
        password=input("请输入密码:")
        with open(BASE_DIR+"\\data\\admin_data.txt","r") as f:
            data=json.loads(f.read())

        f.close()

        if username == data["username"]:
            if password == data["password"]:
                m = main.Main_View(username,password)
                m.group_view()
            else:
                print("密码不正确")
        else:
            print("账号错误")


