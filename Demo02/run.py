import time

import WriteExcel

file_name = '111.xlsx'
WriteExcel.create_excel(file_name)
print(time.asctime(time.localtime()))
