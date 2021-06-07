import sqlalchemy
from sqlalchemy import Column,Integer,String,DateTime, Boolean #区分大小写
from models.index import db

class InOutrecords_109(db):
    __tablename__ = 'InOutrecords_109' #表名
    id = Column(Integer, primary_key=True)
    tradeTime = Column(DateTime)
    tradeType=Column(String)
    lineNo=Column(String)
    stationNo=Column(String)
    deviceNo=Column(String)
    deviceType=Column(String)
    deviceSerialNo=Column(String)
    deviceStatus=Column(String)
    qrcode=Column(String(512))
    deviceOrderNo=Column(String)
    scanTime=Column(DateTime)
    userId=Column(String)
    userCardNo=Column(String)
    userAccountType=Column(String)
    payAccountNo=Column(String)
    bomStationNo=Column(String)
    bomTradeTime=Column(DateTime)
    bomEventNo=Column(String)
    pairStatus=Column(Boolean)
    qrcodeType=Column(String)
    qrcodeCertificate=Column(String)
    channelNo=Column(String)
    cardPlatform=Column(String)
    shardingId=Column(String)
    sourceBom=Column(Boolean)
    dataSource=Column(Integer)
    pushStatus=Column(Integer)
    reTryCount=Column(Integer)
    isPairSingle=Column(Boolean)
    isBomDeleted=Column(Boolean)
    accState=Column(Integer)
    anccState=Column(Integer)
    faceTradeSerialNo=Column(String)
    createdAt = Column(DateTime)
    updatedAt = Column(DateTime)
    deletedAt = Column(DateTime)


class inoutmap :
   def __init__(self, key, count):
    self.date =key#datetime.datetime.strptime(date,'%Y-%m-%d')
    self.count = count
def indexOf(array,value):
 for i in range(len(array)) :
     if array[i].key == value :
        array[i].value +=1  
        return i 
 return -1
