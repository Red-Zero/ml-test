from models.inoutdata import register,inout,orders
import matplotlib.pyplot as plt 
x=[]
y=[]
for item in orders:
    #print(item.date,item.count)
    x.append(item.date)
    y.append(item.count)
print(x,y)
# plt.plot(x, y)
# plt.title("用户注册趋势图")
# plt.xlabel('点数')
# plt.ylabel('概率')
# plt.rcParams['font.sans-serif']=['SimHei']
# plt.rcParams['axes.unicode_minus'] =False

# plt.show()