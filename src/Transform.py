import pandas as pd

from logger import log_info

def trnsform_data(df):
    log_info("Transformation Started")
    df=df.drop_duplicates()
    log_info("Duplicate Records Removed")
    df=df.dropna()
    log_info("Null Values Removed")
    return (df)


    