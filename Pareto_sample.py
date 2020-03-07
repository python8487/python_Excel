import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline  #plt.show() # 有了%matplotlib inline 就可以省掉plt.show()了
'''
%matplotlib inline是一个魔法函数（Magic Functions）。官方给出的定义是：IPython有一组预先定义好的所谓的魔法函数（Magic Functions），
你可以通过命令行的语法形式来访问它们。可见“%matplotlib inline”就是模仿命令行来访问magic函数的在IPython中独有的形式。
————————————————
版权声明：本文为CSDN博主「LthID」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/liangzuojiayi/article/details/78183783
'''
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False  # 这里设置字体，防止中文乱码
    
# 帕累托分布分析 

data = pd.Series(np.random.randn(10)*1200+3000,
                index = list('ABCDEFGHIJ'))
 # 这里ABCDEFGHIJ表示是个产品，用随机值模拟器销售额
print(data)
print('------')
# 创建数据，10个品类产品的销售额

data.sort_values(ascending=False, inplace= True)
# 由大到小排列

plt.figure(figsize = (10,4))
data.plot(kind = 'bar', color = 'g', alpha = 0.5, width = 0.7)  
plt.title('营收柏拉图',fontsize=20)
plt.ylabel('营收_元')
# 创建营收柱状图

p = data.cumsum()/data.sum()  # 创建累计占比，Series
key = p[p>0.8].index[0]  
key_num = data.index.tolist().index(key) 
print('超过80%累计占比的节点值索引为：' ,key)
print('超过80%累计占比的节点值索引位置为：' ,key_num)
print('------')
# 找到累计占比超过80%时候的index
# 找到key所对应的索引位置

p.plot(style = '--ko', secondary_y=True)  # secondary_y → y副坐标轴
# plt.axvline(key_num,hold=None,color='r',linestyle="--",alpha=0.8)  
plt.axvline(key_num,color='r',linestyle="--",alpha=0.8)  
plt.text(key_num+0.2,p[key],'累计占比为：%.3f%%' % (p[key]*100), color = 'r')  # 累计占比超过80%的节点
plt.ylabel('营收_比例')
# 绘制营收累计占比曲线
plt.show()

key_product = data.loc[:key]
print('核心产品为：')
print(key_product)
# 输出决定性因素产品
