import pandas as pd 
from .logger import log_info

def load_data(df,outputfile):
    log_info("load stage started")
    df.to_csv(outputfile, index=False)
    log_info("output file created")
    return("data loaded sucessfully")


    