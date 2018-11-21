#!/usr/bin/env python
# coding:utf-8
# Author:Yang

import json

host_data={

    "host1":
    { # 176
        "hostname":"39.104.137.176",
        "password":"CDsy85306092",
        "username":"root",
        "group":"happy-yoyo"
    },
    "host2":
    { # 49
        "hostname": "39.104.13.49",
        "password": "CDsy85306092",
        "username": "root",
        "group": "happy-yoyo"
    },
    "host3":
    { # centos7
        "hostname": "172.16.95.132",
        "password": "960314",
        "username": "root",
        "group": "mycentos7"
    }
}


with open("host_data.txt","w+") as f:
    f.write(json.dumps(host_data))
f.close()

