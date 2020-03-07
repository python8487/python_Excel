# 导入要用到的第三方库
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 读取excel数据并赋值给df
df=pd.DataFrame(pd.read_excel(r'D:\Pythondemo\python_excel数据处理\柏拉图例子\柏拉图数据.xlsx'))

# 查看数据表维度和数据信息，以检测是否读取成功
# print(df.shape)
# print(df)
# df.columns.values.tolist()  #获取列名列表
ylabel=df.columns[1]   #从数据中获取左Y轴的列表信息

# 设置图表字体，防止中文乱码
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False



# 将df里的转换为x,y轴的array类型的数据
x_col=df.iloc[:,0]
y_col=df.iloc[:,1]
x=x_col.values
y=y_col.values
# print(x)  #确认是否转换成功

data = pd.Series(y,index=list(x))
# print(data)   #确认是否转换成功pd.Series结构
print('-------------------------')
# 以上是将DataFrame结构数据转换为Series数据结构

data.sort_values(ascending=False,inplace=True)  
# 由大到小排列

plt.figure(figsize = (10,4))
data.plot(kind = 'bar', color = 'g', alpha = 0.5, width = 0.7)
# --------------柏拉图标题-------------
plt.title('2020年3月需求柏拉图', fontsize = 20)     
# --------------柏拉图标题-------------
plt.ylabel(ylabel)
# 创建营收柱状图

p = data.cumsum()/data.sum()  #创建累计占比，Series
key = p[p > 0.8].index[0]
key_num = data.index.tolist().index(key)
print('超过80%累计占比的节点值索引为:', key)
print('超过80%累计占比的节点值索引位置为:', key_num)
print('-------------------------')
# 找到累计占比超过80%时候的index
# 找到key所对应的索引位置

p.plot(style = '--ko', secondary_y=True)  # secondary_y → y副坐标轴
plt.axvline(key_num, color='r', linestyle='--', alpha=0.8)

# plt.grid(color='#95a5a6',linestyle='--',axis='y',linewidth=1,alpha=0.4)
plt.text(key_num+0.2, p[key], '累计占比为：%.1f%%' % (p[key]*100), color='r')    # 累计占比超过80%的节点


# --------------柏拉图标题-------------
plt.ylabel(ylabel+'_占比')
# 绘制营收累计占比曲线

# ---------------为直方图添加数据标签--------------





# --------------核心数据汇总输出-------------
key_product = data.loc[:key]
print("核心数依次为：\n{}".format(key_product))

plt.show()
# 显示柏拉图界面










