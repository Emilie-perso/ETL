import pandas as pd 
import requests 

def fetch_data(url,record):
    response = requests.get(url)
    response.raise_for_status()
    contenu = response.json()
    records = contenu[record]
    return records 

def transform_data(records,field):
    df = pd.DataFrame.from_dict(records)
    fields_list = df[field].to_list()
    df_fields = pd.DataFrame.from_records(fields_list)
    return df_fields

def load_data(file_name,data_frame):
    return data_frame.to_csv(file_name, index=False)
