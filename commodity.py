from datetime import datetime
from oanda import *
from data import *
class Commodity:

    def __init__(self, currency, trade_total, trade_unit, risk, start_date, current_date):
        self.trade_total = trade_total
        ##self.unit = self.calculate_unit(self.trade_total,self.n, self.dpp)
        oanda_file = Oanda('GBP', currency, start_date, current_date)
        oanda_file.create_data
        self.data = Data('forex_data.csv')
        self.current_date = self.data.datasheet.iloc[-1].at ["time"]
        self.previous_day = self.data.datasheet.iloc[-2].at ["time"]
        self.initialise_n()
        self.unit = self.calculate_unit(trade_total, trade_unit, risk)


    def update_date(self):
         if self.current_date == datetime.today().strtime('%y-%m-%d'):
             return
         elif datetime.today().strtime('%Y-%m-%d') == (self.data.datasheet).iloc[-1].at ["time"]:
            self.current_date = self.data.datasheet.iloc[-1].at ["time"]
            self.previous_day = self.data.datasheet.iloc[-2].at ["time"]
            self.pdn = self.n
            return
         elif self.current_date == "":
             self.current_date = self.data.datasheet.iloc[-1].at ["time"]
             self.previous_day = self.data.datasheet.iloc[-2].at ["time"]
             self.pdn = self.n
         else:
             return
             

    def update_(self):
        return (self.data.datasheet).iloc[-2].at ["time"]

    def calculate_n(self):
        tr = self.calculate_tr(-1,-2)
        self.n = (19*self.pdn+tr)/20
        return
    
    def calculate_dpp(self, trade_unit, risk):
        return trade_unit/risk
    

    def calculate_unit(self, total, trade_unit, risk):
        onepercent = total*0.01
        return onepercent/self.n*self.calculate_dpp(trade_unit, risk)
    
    def calculate_pdc(self, number):
        mytest = self.data.datasheet.iloc[number].at ["mid"]
        mytest1 = mytest.find('c')
        mytest2 = mytest[mytest1 + 5: mytest1 + 11]
        self.pdc = float(mytest2)
        return
    
    def calculate_tr(self,n1,n2):
        mytest = self.data.datasheet.iloc[n1].at ["mid"]
        myhigh = mytest.find('h')
        myhigh = float(mytest[myhigh + 5: myhigh + 11])
        mylow = mytest.find('l')
        mylow = float(mytest[mylow + 5: mylow + 11])
        self.calculate_pdc(n2)
        trlist = [myhigh - mylow, myhigh - self.pdc, self.pdc - mylow]
        return max(trlist)

    def initialise_n(self):
        trlist= []
        for i in range(20):
            trlist.append(float(self.calculate_tr(i+1, i)))
        average =  sum(trlist)/len(trlist)
        self.n = (19*average+average)/20 
        return 

        
