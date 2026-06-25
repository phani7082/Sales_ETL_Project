import pandas as pd

from logger import log_info

def extract_data(file_path):

    log_info("Extract Stage Started")

    df = pd.read_csv(file_path)

    log_info("Data Extracted Successfully")

    return df

data = extract_data("data/raw_sales.csv")

print(data)