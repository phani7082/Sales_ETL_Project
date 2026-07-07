from .logger import log_info


def transform_data(df):

    log_info("Transformation Started")

    df = df.drop_duplicates()

    log_info("Duplicate Records Removed")

    df = df.dropna()

    log_info("Missing Values Removed")

    df["product"] = df["product"].str.title()

    log_info("Product Names Standardized")

    df["region"] = df["region"].str.title()

    log_info("Region Names Standardized")

    df["sales"] = df["sales"].abs()

    log_info("Negative Sales Converted to Positive")

    total_records = len(df)

    total_sales = df["sales"].sum()

    log_info(f"Total Sales: {total_sales}")

    log_info(f"Total Records After Transformation: {total_records}")

    log_info("Transformation Completed")

    return df