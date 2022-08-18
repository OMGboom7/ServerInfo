from xlsxwriter import workbook
import configparser
import time


# https://blog.51cto.com/xiaofanqie/1770050
def write_excel(file):
    # 生成 Excel 文件
    work = workbook.Workbook(file)
    # 建立工作表，表名默认
    worksheet = work.add_worksheet()
    # 设置字体加粗、字体大小
    format_title = work.add_format({'bold': True, 'font_size': 10})
    # 设置水平对齐、垂直对齐
    format_title.set_align('center')
    format_title.set_align('vcenter')
    format_body = work.add_format({'font_size': 14})
    # 设置样式，行高、列宽
    worksheet.set_row(0, 15)
    # 1-7列宽度
    worksheet.set_column(0, 7, 15)
    # 第8列宽度
    worksheet.set_column(8, 9, 30)
    # 第9列宽度
    worksheet.set_column(9, 10, 15)
    # 定义表头
    title = (
        '服务器IP',
        'CPU 使用率',
        '内存大小(GB)',
        '内存使用率',
        'Swap大小(GB)',
        'Swap使用率',
        '运行时间(天)',
        '系统负载',
        '磁盘超过80%',
        '其余IP',
    )
    row = 0
    col = 0
    # 写入表头
    for item in title:
        # item = unicode(item, "utf-8")
        worksheet.write(row, col, item, format_title)
        col += 1
    # 生产数据

    # 写入数据
    cf = configparser.ConfigParser()
    cf.read('info.txt')
    for ip in cf.sections():
        row += 1
        col = 0
        for opt in cf.options(ip):
            key = cf.get(ip, opt)
            worksheet.write(row, col, key, format_body)
            col += 1
    work.close()


#
#
if __name__ == '__main__':
    Excel_name = "Server_%s.xlsx" % (time.strftime("%Y-%m-%d", time.localtime()))
    write_excel(Excel_name)
#     sendmail.send_mail('********@139.com', '服务器巡检表格', 'fuliao server message', Excel_name)
