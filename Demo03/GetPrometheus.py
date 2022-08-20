# 定义硬盘使用率空字典
import json

import requests as requests

disk_usage_dict = {}
# 定义采集时间间隔
monitorInterval = 5


def query_usage(address, expr):
    url = address + '/api/v1/query?query=' + expr
    try:
        return json.loads(requests.get(url=url).content.decode('utf8', 'ignore'))
    except Exception as e:
        print(e)
        return {}


if __name__ == '__main__':
    s= query_usage('http://192.168.136.129:3000', 'node_disk_read_bytes_total')
    print(s)