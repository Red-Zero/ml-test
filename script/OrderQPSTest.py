import sys 
sys.path.append("..") 
from models.order import Order
from models.inoutrecord import InOutrecords
from models.index import Session


item = Order
def query():
    print(item.__tablename__)
    item.__tablename__ = "Orders_01"
    orders= Session.query(item).filter(item.userId == '4PMJM3VB1O',  item.tradeTime <'2021-01-09',item.status < 2).all()