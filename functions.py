import string
from this import d
import pandas as pd 
import requests 

def fetch_data(url : string, record : string):
    """
    This function fetch data from an API 

    Args:
        url (string): url of the API 
        record (string): the records field 

    Returns:
        list : list of record
    """
    response = requests.get(url)
    response.raise_for_status()
    contenu = response.json()
    records = contenu[record]
    return records 

def transform_data(records : list, field : string):
    """
    Transform Data into a data frame 

    Args:
        records (list): list of record
        field (string): field to keep 

    Returns:
        pandas.core.frame.DataFrame 
    """
    df = pd.DataFrame.from_dict(records)
    fields_list = df[field].to_list()
    df_fields = pd.DataFrame.from_records(fields_list)
    return df_fields

def load_data(file_name : string, data_frame : pd.DataFrame):
    """Load data into a csv file 

    Args:
        file_name (string): name of file 
        data_frame (pd.DataFrame): dataframe of the cleansed data 

    Returns:
        csv file 
    """
    return data_frame.to_csv(file_name, index=False)
