通过多线程实现基于paramiko的ssh,sftp的批量管理主机功能

需求：
1.主机分组
2.登录后显示主机分组，选择分组后查看主机列表
3.可批量执行命令、发送文件，结果实时返回
4.主机用户名密码可以不同

只能执行paramiko.exec_command能执行的指令，例如top等不能执行
通过多线程实现从data目录读取主机数据（ip,pwd等）利用paramiko实现ssh登录执行命令或sftp发送接收远程主机的文件

|-- paramiko_manage
    |-- bin   # 程序启动目录
    |   |-- 1.txt
    |   |-- manage_host.py
    |   |-- __init__.py
    |-- conf   # 配置文件目录
    |   |-- setting.py
    |   |-- __init__.py
    |   |-- __pycache__
    |   |   |-- setting.cpython-37.pyc
    |   |   |-- __init__.cpython-37.pyc
    |-- core # 批量管理主功能
    |   |-- main.py  # 程序主入口（界面、线程启动）
    |   |-- paramiko_function.py  # paramiko实现ssh,sftp
    |   |-- __init__.py
    |   |-- __pycache__
    |   |   |-- main.cpython-37.pyc
    |   |   |-- paramiko_function.cpython-37.pyc
    |   |   |-- __init__.cpython-37.pyc
    |-- data # 数据目录
    |   |-- admin_data.txt # 管理员登录数据
    |   |-- create_admin.py
    |   |-- create_data.py
    |   |-- host_data.txt # 主机数据
    |   |-- __init__.py