import time

import openpyxl
import GetPassword

import ExcelCreate

# 1
print('创建Excel')
localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(localtime)
ExcelCreate.create_excel()

# 2
wb = openpyxl.Workbook()
ws = wb.active
info = GetPassword.get_yaml_data('config.yaml')
for i in list(info):
    keys = list(info[i].keys())
    values = list(info[i].values())

    print(values[1])

for i in (0, len(info)):
    print(i)
