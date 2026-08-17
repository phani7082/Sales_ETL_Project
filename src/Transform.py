from .logger import log_info
from .exceptions import TransformationError

def transform_data(df):

    log_info("Transformation Started")

    # -----------------------------------
    # Remove Duplicate Records
    # -----------------------------------
    df = df.drop_duplicates()

    log_info("Duplicate Records Removed")

    # -----------------------------------
    # Remove Missing Values
    # -----------------------------------
    df = df.dropna()

    log_info("Missing Values Removed")

    # -----------------------------------
    # Standardize Product Names
    # -----------------------------------
    df["product"] = df["product"].str.strip().str.title()

    log_info("Product Names Standardized")

    # -----------------------------------
    # Standardize Category Names
    # -----------------------------------
    df["category"] = df["category"].str.strip().str.title()

    log_info("Category Names Standardized")

    # -----------------------------------
    # Standardize Region Names
    # -----------------------------------
    df["region"] = df["region"].str.strip().str.title()

    log_info("Region Names Standardized")

    # -----------------------------------
    # Standardize Salesperson Names
    # -----------------------------------
    df["salesperson"] = df["salesperson"].str.strip().str.title()

    log_info("Salesperson Names Standardized")

    # -----------------------------------
    # Convert Negative Sales
    # -----------------------------------
    df["sales"] = df["sales"].abs()

    log_info("Negative Sales Converted")

    # -----------------------------------
    # Convert Negative Quantity
    # -----------------------------------
    df["quantity"] = df["quantity"].abs()

    log_info("Negative Quantity Converted")

    # -----------------------------------
    # Calculate Unit Price
    # -----------------------------------
    df["unit_price"] = df["sales"] / df["quantity"]

    log_info("Unit Price Calculated")

    # -----------------------------------
    # Assign Sales Category
    # -----------------------------------
    df["sales_category"] = df["sales"].apply(
        lambda x: "High" if x >= 50000 else "Medium" if x >= 20000 else "Low"
    )

    log_info("Sales Category Assigned")

    # -----------------------------------
    # Business Metrics
    # -----------------------------------
    total_records = len(df)

    total_sales = df["sales"].sum()

    average_sales = df["sales"].mean()

    highest_sale = df["sales"].max()

    lowest_sale = df["sales"].min()

    high_sales = len(df[df["sales_category"] == "High"])

    medium_sales = len(df[df["sales_category"] == "Medium"])

    low_sales = len(df[df["sales_category"] == "Low"])

    log_info(f"Total Records : {total_records}")

    log_info(f"Total Sales : {total_sales}")

    log_info(f"Average Sale : {average_sales:.2f}")

    log_info(f"Highest Sale : {highest_sale}")

    log_info(f"Lowest Sale : {lowest_sale}")

    log_info(f"High Sales Transactions : {high_sales}")

    log_info(f"Medium Sales Transactions : {medium_sales}")

    log_info(f"Low Sales Transactions : {low_sales}")

    log_info("Transformation Completed")

    return df