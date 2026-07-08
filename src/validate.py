import pandas as pd

from .logger import log_info


def validate_data(df):

    log_info("Validation Started")

    required_columns = [
    "transaction_id",
    "sale_date",
    "product",
    "category",
    "sales",
    "quantity",
    "region",
    "salesperson"
     ]

    for column in required_columns:

        if column not in df.columns:

            raise ValueError(f"Missing Required Column: {column}")

    log_info("Column Validation Completed")

    if df.empty:

        raise ValueError("Dataset is Empty")

    log_info("Dataset Validation Completed")

    if not pd.api.types.is_numeric_dtype(df["sales"]):

        raise ValueError("Sales column must contain numeric values")

    log_info("Numeric Validation Completed")

    if not pd.api.types.is_numeric_dtype(df["quantity"]):
    raise ValueError("Quantity column must contain numeric values")

    log_info("Quantity Validation Completed")

    if df["transaction_id"].duplicated().any():
    raise ValueError("Duplicate Transaction IDs Found")

    log_info("Transaction ID Validation Completed")

    df["sale_date"] = pd.to_datetime(df["sale_date"])

    log_info("Date Validation Completed")

    return True