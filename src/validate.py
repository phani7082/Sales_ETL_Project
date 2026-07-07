import pandas as pd

from .logger import log_info


def validate_data(df):

    log_info("Validation Started")

    required_columns = [
        "product",
        "sales",
        "region"
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

    return True