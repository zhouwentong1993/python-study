import xlrd

def b():
    wb = xlrd.open_workbook('test2.xlsx')
    sheet = wb.sheet_by_index(0)
    automationsum=0
    personsum=0
    a_threesum=0
    a_selfsum=0
    p_threesum=0
    p_selfsum=0
    p_foursum = 0
    p_fivesum = 0
    p_sixsum = 0
    for i in range(1, sheet.nrows):
        if sheet.cell(i,6).value=='自动化模型通过':
            automationsum=automationsum+1
        else:  personsum=personsum+1
        if (round((1 - sheet.cell(i, 3).value / sheet.cell(i, 4).value), 2)) ==0.3 and sheet.cell(i,6).value == '自动化模型通过':
            a_threesum =  a_threesum+ 1
        if (round((1 - sheet.cell(i, 3).value / sheet.cell(i, 4).value), 2)) > 0.3 and sheet.cell(i,6).value == '自动化模型通过':
            a_selfsum =  a_selfsum+1
        if (round((1 - sheet.cell(i, 3).value / sheet.cell(i, 4).value), 2)) ==0.3 and sheet.cell(i,6).value == '正常审批通过':
            p_threesum =p_threesum+1
        if (round((1 - sheet.cell(i, 3).value / sheet.cell(i, 4).value), 2)) > 0.3 and (sheet.cell(i,6).value == '正常审批通过' or sheet.cell(i,6).value =='增加共借人通过' or ('A910-1' in sheet.cell(i,6).value and ('A910-2'not in sheet.cell(i,6).value or'A910-3'not in sheet.cell(i,6).value or'A910-4' not in sheet.cell(i,6).value))):
            p_selfsum =p_selfsum+1
        if round((1 - sheet.cell(i, 3).value / sheet.cell(i, 4).value), 2) > 0.3 and 'A910-2' in sheet.cell(i, 6).value:
            p_foursum = p_foursum + 1
        if round((1 - sheet.cell(i, 3).value / sheet.cell(i, 4).value), 2) > 0.3 and 'A910-3' in sheet.cell(i,6).value:
            p_fivesum =p_fivesum + 1
        if round((1 - sheet.cell(i, 3).value / sheet.cell(i, 4).value), 2) > 0.3 and 'A910-4' in sheet.cell(i,6).value:
            p_sixsum =p_sixsum + 1
    return automationsum,personsum, a_threesum,a_selfsum,p_threesum,p_selfsum,p_foursum ,p_fivesum , p_sixsum


import xlwt as xlwt

def set_style(name, height, bold=False):
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font
    return style


# 写Excel
def write_excel(automationsum,personsum, a_threesum,a_selfsum,p_threesum,p_selfsum ,p_foursum ,p_fivesum , p_sixsum):
    f = xlwt.Workbook()
    sheet1 = f.add_sheet('首付成数分析', cell_overwrite_ok=True)
    sheet1.write(0,0,'自动审批数')
    sheet1.write(0,1,'人工审批数')
    sheet1.write(2,0,'自动3成通过')
    sheet1.write(2,1,'自动自提首付通过')
    sheet1.write(4,0,'人工3成通过')
    sheet1.write(4, 1, '人工自提首付通过')
    sheet1.write(4,2,'人工提1成通过')
    sheet1.write(4,3,'人工提绿色通过')
    sheet1.write(4,4,'人工提深蓝通过')

    sheet1.write(1,0,automationsum)
    sheet1.write(1,1,personsum)
    sheet1.write(3,0, a_threesum)
    sheet1.write(3,1,a_selfsum)

    sheet1.write(5,0,p_threesum)
    sheet1.write(5,1, p_selfsum)
    sheet1.write(5,2, p_foursum)
    sheet1.write(5,3, p_fivesum)
    sheet1.write(5,4,p_sixsum)
    f.save('test6.xls')




if __name__ == '__main__':
    # sum = a()
    # write_excel(sum)
    # sum=b()
    # write_excel(sum)
    automationsum, personsum, a_threesum, a_selfsum, p_threesum, p_selfsum, p_foursum, p_fivesum, p_sixsum= b()
    write_excel(automationsum,personsum, a_threesum,a_selfsum,p_threesum,p_selfsum ,p_foursum ,p_fivesum , p_sixsum)
