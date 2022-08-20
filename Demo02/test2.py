import subprocess

import paramiko as paramiko
import psutil


def main():
    # 读取服务器列表
    server_list = open('server_list.txt', 'r')

    for line in server_list:
        # 获取IP、用户名、密码、端口
        _host = line.split()[0]
        _username = line.split()[1]
        _password = line.split()[2]
        _port = int(line.split()[3])

        try:
            _ssh_fd = paramiko.SSHClient()
            _ssh_fd.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            _ssh_fd.connect(hostname=_host, username=_username, password=_password, port=_port)
            print('server: ' + _host + '服务器登录成功！')
        except Exception as e:
            print('ssh %s@%s -p %s : %s' % (_username, _host, _port, e))
            exit()

        # 执行命令
        #
        return_code = subprocess.run(['top -b -n 1 | grep Cpu | awk ','{print $2}',' | cut -f 1 -d "%"'])
        # cmd = 'top -b -n 1 | grep Cpu | awk ' + '{print' + '$2}' + ' | cut -f 1 -d "%"'
        # print(cmd)
        # stdin, stdout, stderr = _ssh_fd.exec_command(cmd)
        # list = stdout.readlines()
        print(return_code)

        # 关闭连接
        _ssh_fd.close()

    server_list.close()


if __name__ == '__main__':
    main()
