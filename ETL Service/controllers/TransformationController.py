import pandas as pd
import json
from pandas import json_normalize
class TransformationController:

    def return_list(self , data):
        drop_duplicates_list = self.drop_duplicates(data)
        list_dropna_list = self.list_dropna(drop_duplicates_list)
        clean_data_list = self.clean_date(list_dropna_list)
        return clean_data_list
    
    def drop_duplicates(self , data):
    
        # convert json to DataFrame
        df = pd.DataFrame(data)
        #print(df)
        duplicated = df.drop_duplicates()
        json_list = duplicated.to_dict(orient='records')
        return json_list

    def list_dropna(self , data):
        
        # convert json to DataFrame
        df = pd.DataFrame(data)
        #print(df)
        list_dropna = df.fillna('-')
        
        json_list = list_dropna.to_dict(orient='records')
        return json_list
    
    def clean_date(self , data):
        
        # convert json to DataFrame
        df = pd.DataFrame(data)
        print("DataFrame info Before to_Datetime")
        print(df.info())
        #print(df)
        if 'Date' in df.columns:
            df['Date'] = pd.to_datetime(df['Date'])
        #print(df['Date'])
        print("DataFrame info After to_Datetime")
        
        print(df.info())

        json_list = df.to_dict(orient='records')
        return json_list
