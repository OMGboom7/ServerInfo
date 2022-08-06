#!/usr/bin/python
# coding:utf-8

import re
import paramiko

# https://www.cnblogs.com/klb561/p/9157569.html 服务器常用信息获取
# https://www.jianshu.com/p/b9e942f3682c        网卡速率

host = "mc.p07.icu"
port = 26613
username = "root"
password = "Zyc644031332."


# 获取服务器连接
def session():
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port, username, password)
        # print("Login %s is successful" % host)
        return ssh
    except Exception as e:
        print(e)


# 获取Linux系统版本信息
def get_version():
    client = session()
    stdin, stdout, stderr = client.exec_command("cat /etc/redhat-release")
    data = stdout.read().decode()
    client.close()
    return data


# 获取Linux系统CPU信息
def get_cpu():
    cpu_mode = ''
    cpu_num = 0
    processor = 0
    client = session()
    stdin, stdout, stderr = client.exec_command("cat /proc/cpuinfo")
    cpuinfo = stdout.readlines()
    # with stdout.read() as cpuinfo:
    for i in cpuinfo:
        if i.startswith('physical id'):
            # cpu_num = "物理CPU数量：" + i.split(":")[1]
            cpu_num = i.split(":")[1]
        if i.startswith('processor'):
            # processor = "逻辑CPU数量：" + processor + 1
            processor = processor + 1
        if i.startswith('model name'):
            # cpu_mode = "物理CPU型号：" + i.split(":")[1]
            cpu_mode = i.split(":")[1]
    client.close()
    return int(cpu_num) + 1, processor, cpu_mode


# 获取服务器时间
def get_date():
    client = session()
    stdin, stdout, stderr = client.exec_command("date")
    date = stdout.read().decode()
    client.close()
    return date


# 获取IP
def get_ifconfig():
    client = session()
    stdin, stdout, stderr = client.exec_command("ifconfig")
    data = stdout.read()
    # ret = re.compile('((?:1[0-9][0-9]\.)|(?:25[0-5]\.)|(?:2[0-4][0-9]\.)|(?:[1-9][0-9]\.)|(?:[0-9]\.)){3}((1[0-9][
    # 0-9])|(2[0-4][0-9])|(25[0-5])|([1-9][0-9])|([0-9]))')
    ret = re.compile(
        '(?:19[0-9]\.)((?:1[0-9][0-9]\.)|(?:25[0-5]\.)|(?:2[0-4][0-9]\.)|(?:[1-9][0-9]\.)|(?:[0-9]\.)){2}((1[0-9]['
        '0-9])|(2[0-4][0-9])|(25[0-5])|([1-9][0-9])|([0-9]))')
    match = ret.search(data).group()
    client.close()
    return match


# 获取主机名
def get_hostname():
    client = session()
    stdin, stdout, stderr = client.exec_command("hostname")
    hostname = stdout.read().decode()
    client.close()
    return hostname


# 获取Linux系统内存信息
def get_memory():
    memory = ''
    client = session()
    stdin, stdout, stderr = client.exec_command("cat /proc/meminfo")
    meminfo = stdout.readlines()
    # with open('/proc/meminfo') as meminfo:
    for i in meminfo:
        if i.startswith('MemTotal'):
            memory = int(i.split()[1].strip())
            memory = '%.f' % (memory / 1024.0) + 'MB'
        else:
            pass

        client.close()
        return memory


# 获取Linux系统网卡信息
def get_ethernet():
    client = session()
    stdin, stdout, stderr = client.exec_command("lspci")
    data = stdout.read()
    ret = re.compile('Eth[^\d].*')
    eth = ret.search(data).group()
    client.close()
    return eth


#
# version = "系统版本：" + get_version()
# print(version)
# cpu = get_cpu()
# for i in cpu:
#     print(cpu)
if __name__ == '__main__':
    get_ethernet()
    get_cpu()
    get_memory()
    get_hostname()
    get_date()
    get_version()
    get_ifconfig()
