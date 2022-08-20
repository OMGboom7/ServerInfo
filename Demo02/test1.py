import os


def get_ip():
    """获取ip地址"""

    IP = os.popen("ip add list |grep global |awk -F[/' '] '{print $6}'").readlines()

    getip = IP[0]

    # return getip.strip('\n')
    print(getip.strip('\n'))
