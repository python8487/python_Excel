# Excel数据合并--多个sheet合并为一个sheet




# 第一步：调用pandas包
import os
import pandas as pd
import time
print("注意事项： \n\
	一、需要合并处理的xlsx文件内的数据结构需要一样---重要！\n\
    二、需要处理的xlsx文件必须放在程序同一目录的‘concat’文件夹内---重要！！\n\
    三、不需处理文件请不要放在‘concat’文件夹内，否则会一起处理掉--重要！！!\n\
	三、合并后的表格数据显示不正常的在Excel做相应处理才能正常显示\n\
	1)日期数据合并后显示一串数字的，需要将所在数据单元格格式改为日期【快捷键crtl+1】\n\
	2)有些超长数字在合并后显示科学计数的数字，想以文本显示数据的需如此操作:\n\
	【选中所有需处理的数据单元格->数据->分列->固定宽度->下一步->调整宽度->下一步->文本->完成】\n\
	3)百分比数据合并后显示一串数字的，需要将所在数据单元格格式改为百分比【快捷键crtl+1】\
	")
# path=str(input('请输入要合并sheet表格的文件名称:'))
outfile=str(input('请输入合并成功后的文件名称(文件会保存在程序同目录下)：'))


# 将文件读取出来放一个列表里面
pwd = 'concat' # 获取文件目录
# 新建列表，存放文件名
file_list = []
# 新建列表存放每个文件数据(依次读取多个相同结构的Excel文件并创建DataFrame)
dfs = []
for root,dirs,files in os.walk(pwd):  # 第一个为起始路径，第二个为起始路径下的文件夹，第三个是起始路径下的文件。
    for file in files:
        file_path = os.path.join(root, file)
        file_list.append(file_path) # 使用os.path.join(dirpath, name)得到全路径
        df = pd.read_excel(file_path) # 将excel转换成DataFrame
        dfs.append(df)
# 将多个DataFrame合并为一个
df = pd.concat(dfs)
# 写入excel文件，不包含索引数据
df.to_excel(outfile+'.xlsx', index=False)
print("合并完毕，"+outfile+".xlsx 文件保存在程序所在目录里。")
time.sleep(3)
