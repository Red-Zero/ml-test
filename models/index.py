#conding:utf-8

from sqlalchemy import  create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#创建连接
_engine=create_engine("mysql+pymysql://root:12345678@localhost/scanapp_development",encoding='utf-8',echo=True)
db = declarative_base()
db.metadata.create_all(_engine)
_SessionClass=sessionmaker(bind=_engine) ##创建与数据库的会话，class,不是实例
Session=_SessionClass()   
 #生成session实例
# res= Session.query(user).filter(user.userId == '740ASD5A5X',user.tradeType=='25').all()
