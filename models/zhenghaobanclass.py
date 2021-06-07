import datetime
class zhenghaoban :
  def __init__(self, date, count):
    self.date =date#datetime.datetime.strptime(date,'%Y-%m-%d')
    self.count = count
  
  def detail(self):
    print(self.date)
    print(self.count)