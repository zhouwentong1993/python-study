# 设置表格样式
import xlwt as xlwt

# def set_style(name, height, bold=False):
#     style = xlwt.XFStyle()
#     font = xlwt.Font()
#     font.name = name
#     font.bold = bold
#     font.color_index = 4
#     font.height = height
#     style.font = font
#     return style


# 写Excel
# def write_excel():
#     f = xlwt.Workbook()
#     sheet1 = f.add_sheet('学生', cell_overwrite_ok=True)
#     row0 = ["姓名", "年龄", "出生日期", "爱好", "性别"]
#     colum0 = ["张三", "李四", "恋习Python", "小明", "小红", "无名"]
#     # 写第一行
#     for i in range(0, len(row0)):
#         sheet1.write(0, i, row0[i], set_style('Times New Roman', 220, True))
#     # 写第一列
#     for i in range(0, len(colum0)):
#         sheet1.write(i + 1, 0, colum0[i], set_style('Times New Roman', 220, True))
#
#     for i in range(0, len(colum0)):
#         gender = '男'
#         if i % 2 == 0:
#             gender = '男'
#         else:
#             gender = '女'
#
#         sheet1.write(i + 1, 4, gender, set_style('Times New Roman', 220, True))
#
#     sheet1.write(1, 3, 'aaaa')
#     sheet1.write_merge(6, 6, 1, 3, '未知')  # 合并行单元格
#     # sheet1.write_merge(1, 2, 3, 3, '打游戏')  # 合并列单元格
#     sheet1.write_merge(4, 5, 3, 3, '打篮球')
#
#     f.save('test.xls')


import xlrd

from datetime import date, datetime

file = '123.xlsx'


def read_excel():
    wb = xlrd.open_workbook(filename=file)  # 打开文件

    print(wb.sheet_names())  # 获取所有表格名字

    sheet1 = wb.sheet_by_index(0)  # 通过索引获取表格
    #
    sheet2 = wb.sheet_by_name('截面数据')  # 通过名字获取表格
    #
    print(sheet1, sheet2)
    #
    print(sheet1.name, sheet1.nrows, sheet1.ncols)
    #
    # rows = sheet1.row_values(2)#获取行内容
    #
    # cols = sheet1.col_values(1)#获取列内容
    #
    # print(rows)
    #
    # print(cols)
    #
    print(sheet1.cell(2, 1).value)  # 获取表格里的内容，三种方式

    sum = 0
    for i in range(2, 16):
        sum = sum + int(sheet1.cell(i, 1).value)

    print(sum)
    sum1 = 0
    for i in range(2, 16):
        sum1 = sum1 + int(sheet1.cell(i, 2).value)
    print(sum1)
    print(round(sum1 / sum, 4))
    print(100 * round(sum1 / sum, 4))

    print('%.2f%%' % (round(sum1 / sum, 2) *100))

    a = round(sum1 / sum, 5)
    bb = "%.2f%%" % (a * 100)
    print(bb)


#
# print(sheet1.cell_value(1,0))
#
# print(sheet1.row(1)[0].value)


if __name__ == '__main__':
    read_excel()
