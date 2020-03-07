
import xlrd
import xlwt
import time

print("注意事项： \n\
	一、需要将需处理的xlsx文件放在和程序一起的目录里面---重要！！！\n\
	二、本程序只能处理2列数据,请按test.xlsx表格的数据方式存储才能处理\n\
	三、要求输入的文件名称要带扩展名。例:test.xlsx\n\
	")
path=str(input('请输入要处理重复数据并做合计的Excel文件名称:'))

# 用xlrd打开待处理的excel文件，读取待处理的数据
xlsfile = path
book = xlrd.open_workbook(xlsfile) # 获取Excel文件的book对象
 
# sheet0 = book.sheet_by_index(0) # 通过sheet索引获得sheet对象
# nrows = sheet0.nrows # 获取需要处理的数据的行数
 
sheet_name = book.sheet_names()[0] # 尝试通过sheet名字来获取，当然如果知道sheet名字就可以直接指定
sheet1 = book.sheet_by_name(sheet_name)
nrows = sheet1.nrows # 获取需要处理的数据的行数

item1=sheet1.row_values(0)[0]
item2=sheet1.row_values(0)[1]
# print(type(item1),type(item2),item1,item2)


# 用xlwt创建一个excel对象,并初始化第一行的数据，为写入数据做准备
book_new = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet_new = book_new.add_sheet("sheet1", cell_overwrite_ok=True)
sheet_new.write(0, 0,item1)
sheet_new.write(0, 1,item2)
line = 1 #后面自动写入的数据从第二行开始
 
 
# 处理逻辑, calc list用来记录行是否已经处理过的标志，先将所有待处理的行初始为“待处理”的标志
calc = []
for k in range(1,nrows+1): # 第一行是列名，无须处理
    calc.append(False)     # False表示对应的行未被处理过
 
# 读取数据进行合并处理，并写入xlwt创建的对象中
for i in range(1,nrows):
    if calc[i] == False:  # False表示对应的行未被处理过相加过，True表示已相加过，跳过这条数据
        totol_i = sheet1.row_values(i)[1]  # 获取该行型号的初始数量
 
        for j in range(i+1, nrows):
            if sheet1.row_values(i)[0] == sheet1.row_values(j)[0]: #表示查到了同型号规格的数据
                totol_i += sheet1.row_values(j)[1]
                calc[j] = True #将第j列标志为已处理
 
        #将计算的值写入新建的sheet_new
        sheet_new.write(line, 0, sheet1.row_values(i)[0])
        sheet_new.write(line, 1, totol_i)
        line += 1

# 处理完毕，保存到桌面
book_new.save(r'合计结果.xls')
print("处理完毕，合计结果.xls文件保存在程序所在目录里。")
time.sleep(3)
# 版权声明：本文为CSDN博主「Pansc2004」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/Pansc2004/article/details/80400742