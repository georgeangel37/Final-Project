import pandas as pd
class Data:


    def __init__(self,data):
        self.datasheet = pd.read_csv(data, encoding='latin1',on_bad_lines='skip')
        
