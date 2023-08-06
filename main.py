from data import *
from oanda import *
from commodity import*
import pandas as pd

capital = 1000000

def main():
   test = Commodity('EUR', capital,5,0.02,'2021-01-01','2021-09-03')
   print(test.n)
   print(test.unit)
   

if __name__ == "__main__":
    main()