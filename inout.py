from models.order import Order
from models.index import Session
from classlib.baseData import baseData
import time,datetime

p_outStation =[]
p_inStationNo_inTradeTime=[]
p_inStationNo_inTradeTime1outStationNo=[] 
def detailDeviceOrderNo(deviceOrderNo):
    stationNo = deviceOrderNo[2:6]
    hour = deviceOrderNo[14:16]
    return stationNo,hour

def detailData(baseData,dataArr,count):
    for item in dataArr:
        if baseData.colName == item.colName and baseData.value == item.value :
            item.num+=1 
            item.probability = item.num / count 
            return 1
    baseData.probability = baseData.num/count
    dataArr.append(baseData)

orders= Session.query(Order).filter(Order.userId == '4PMJM3VB1O',  Order.tradeTime <'2021-01-09',Order.status < 2).all()
#公式: p(outStationNo | inStationNo,inTradeTime)=p(inStationNo,inTradeTime|outStationNo ) * p(outStationNo) / p(inStationNo,inTradeTime) 
def getRes(order):
 inStationInfo=detailDeviceOrderNo(orders[index].inDeviceOrderNo)
 res="",
 maxProbability=0
 p_o = 0
 p_is_it = 0
 p_is_it1os = 0
 for item in p_inStationNo_inTradeTime :
     if item.value ==inStationInfo[0]+"^"+inStationInfo[1]:
         p_is_it = item.probability
 if p_is_it == 0 :
     return ""
 for item in p_outStation:
     p_o=item.probability
     for item1 in p_inStationNo_inTradeTime1outStationNo :
         if item1.value == inStationInfo[0]+"^"+inStationInfo[1]+"|"+item.value :
             p_is_it1os=item1.probability
             p= p_is_it1os * p_o / p_is_it
             if(p>maxProbability ):
                 maxProbability = p
                 res = item.value
 return res

l = len(orders)
# 80%样本,20%预测
count= int(l*0.8)


for index in range(count):
  #计算p(outStation)
  outStationInfo=detailDeviceOrderNo(orders[index].outDeviceOrderNo)
  detailData(baseData('outStationNo',outStationInfo[0]),p_outStation,l)
  #计算p(inStationNo,inTradeTime) 
  inStationInfo=detailDeviceOrderNo(orders[index].inDeviceOrderNo)
  detailData(baseData('inStationNo-inTradeTime',inStationInfo[0]+"^"+inStationInfo[1]),p_inStationNo_inTradeTime,l)
  #统计p(inStationNo,inTradeTime|outStationNo ) 
  detailData(baseData('inStationNo-inTradeTime|outStation',inStationInfo[0]+"^"+inStationInfo[1]+"|"+outStationInfo[0]),p_inStationNo_inTradeTime1outStationNo,1)
#计算p(inStationNo,inTradeTime|outStationNo ) 
for i in p_inStationNo_inTradeTime1outStationNo:
     outStationNo = i.value.split('|')[1]
     for j in p_outStation :
         if j.value == outStationNo :
             i.probability = i.num / j.num
# for item in p_inStationNo_inTradeTime1outStationNo:
#   print(item.colName,item.value,item.num,item.probability)
c1=0
c0=0
for index in range(count,l) :
    os = getRes(orders[index])
    if(os == detailDeviceOrderNo(orders[index].outDeviceOrderNo)[0]) :
       c1+=1
    else :
        c0+=1

print(c1,c0,c1/(c1+c0))
# for item in res:
#  week = datetime.datetime.weekday(item.tradeTime)
#  hour = datetime.datetime.time(item.tradeTime).hour
#  print(week,hour)