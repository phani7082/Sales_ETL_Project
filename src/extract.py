import pandas as pd

from .database import get_connection
from .config_reader import load_config
from .logger import log_info



def extract_data(offset, batch_size):

    log_info(f"Starting Extraction For Offset : {offset}")

    config = load_config()

    source_table = config["source_table"]
    region_filter = config["region_filter"]
    category_filter = config["category_filter"]
    minimum_sales = config["minimum_sales"]

    connection = get_connection()

    query = f"""
    SELECT
        transaction_id,
        sale_date,
        product,
        category,
        quantity,
        sales,
        region,
        salesperson
    FROM {source_table}
    WHERE
        region = ?
        AND category = ?
        AND sales >= ?
    ORDER BY transaction_id
    OFFSET ? ROWS
    FETCH NEXT ? ROWS ONLY
    """

    df = pd.read_sql(
        query,
        connection,
        params=[
            region_filter,
            category_filter,
            minimum_sales,
            offset,
            batch_size
        ]
    )

    connection.close()

    log_info(
        f"Extracted {len(df)} Records From Offset {offset}"
    )

    return df