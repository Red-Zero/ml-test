import sqlalchemy
from sqlalchemy import Column, Integer, String, DateTime, Boolean  # 区分大小写
from models.index import db


class Order(db):
    __tablename__ = 'Orders_109'  # 表名
    id = Column(Integer,primary_key=True)
    userId = Column(String)
    payStatus = Column(Integer)
    status = Column(Integer)
    deductFee = Column(Integer)
    inDeviceOrderNo = Column(String)
    outDeviceOrderNo = Column(String)
    isTimeout = Column(Boolean)
    timeoutFee = Column(Integer)
    mileageFee = Column(Integer)
    payMethod = Column(String)
    channelNo = Column(String)
    channelUserId = Column(String)
    orderNo = Column(String)
    shardingId = Column(Integer)
    createdAt = Column(DateTime)
    updatedAt = Column(DateTime)
    tradeTime = Column(DateTime)
    deletedAt = Column(DateTime)
    chargeResult = Column(String)
    callPayCount = Column(Integer)
    realFee = Column(Integer)
    discountFee = Column(Integer)
    discountInfo = Column(String)
    mileage = Column(Integer)
    outTradeNo = Column(String)
    accState = Column(Integer)
    anccState = Column(Integer)
