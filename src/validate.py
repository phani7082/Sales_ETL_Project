import pandas as pd 
import pandas as pd

from .logger import log_info
from .exceptions import ValidationError


def validate_data(df):

    log_info("Validation Started")

    # -----------------------------
    # Required Columns Validation
    # -----------------------------
    required_columns = [
        "transaction_id",
        "sale_date",
        "product",
        "category",
        "quantity",
        "sales",
        "region",
        "salesperson"
    ]

    for column in required_columns:

        if column not in df.columns:

            raise ValidationError(f"Missing Required Column: {column}")

    log_info("Required Columns Validation Completed")

    # -----------------------------
    # Empty Dataset Validation
    # -----------------------------
    if df.empty:

        raise ValidationError("Dataset is Empty")

    log_info("Dataset Validation Completed")

    # -----------------------------
    # Sales Validation
    # -----------------------------
    if not pd.api.types.is_numeric_dtype(df["sales"]):

        raise ValidationError("Sales column must contain numeric values")

    log_info("Sales Validation Completed")

    # -----------------------------
    # Quantity Validation
    # -----------------------------
    if not pd.api.types.is_numeric_dtype(df["quantity"]):

        raise ValueError("Quantity column must contain numeric values")

    log_info("Quantity Validation Completed")

    # -----------------------------
    # Transaction ID Validation
    # -----------------------------
    if df["transaction_id"].duplicated().any():

        raise ValueError("Duplicate Transaction IDs Found")

    log_info("Transaction ID Validation Completed")

    # -----------------------------
    # Sale Date Validation
    # -----------------------------
    try:

        df["sale_date"] = pd.to_datetime(df["sale_date"])

    except Exception:

        raise ValidationError("Invalid Sale Date Format")

    log_info("Sale Date Validation Completed")

    log_info("All Validations Completed Successfully")

    return True
