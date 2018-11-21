#!/usr/bin/env python
# coding:utf-8
# Author:Yang


import json

admin_data={
    "username":"admin",
    "password":"960314"
}

with open("admin_data.txt","w+") as f:
    f.write(json.dumps(admin_data))
f.close()

