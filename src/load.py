from .logger import log_info, log_error
from .exceptions import LoadError
from .database import get_connection


def load_to_csv(df, output_file):
    """
    Save transformed data into CSV.
    """
    try:
        log_info("CSV Load Started")

        df.to_csv(output_file, index=False)

        log_info("CSV File Created Successfully")

    except Exception as e:
        log_error(f"CSV Load Failed: {e}")
        raise LoadError(f"CSV Load Error: {e}")


def load_to_sql(df):
    """
    Save transformed data into SQL Server.
    """

    connection = None
    cursor = None

    try:
        log_info("SQL Server Load Started")

        connection = get_connection()
        cursor = connection.cursor()

        # -----------------------------
        # FULL LOAD STRATEGY
        # -----------------------------
        log_info("Deleting existing records from clean_sales")

        cursor.execute("DELETE FROM clean_sales")

        log_info("Old records deleted successfully")

        # -----------------------------
        # INSERT NEW RECORDS
        # -----------------------------
        for _, row in df.iterrows():

            cursor.execute(
                """
                INSERT INTO clean_sales
                (
                    sale_id,
                    product_name,
                    category,
                    region,
                    sales_amount,
                    sale_date
                )
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    row["sale_id"],
                    row["product_name"],
                    row["category"],
                    row["region"],
                    row["sales_amount"],
                    row["sale_date"]
                )
            )

        # Save transaction permanently
        connection.commit()

        # -----------------------------
        # LOAD VERIFICATION
        # -----------------------------
        cursor.execute("SELECT COUNT(*) FROM clean_sales")

        loaded_records = cursor.fetchone()[0]

        expected_records = len(df)

        if loaded_records == expected_records:

            log_info(
                f"Load Verification Successful : {loaded_records} records loaded."
            )

        else:

            raise LoadError(
                f"Verification Failed. Expected {expected_records}, Found {loaded_records}"
            )

        log_info("SQL Server Load Completed Successfully")

    except Exception as e:

        if connection:
            connection.rollback()

        log_error(f"SQL Load Failed: {e}")

        raise LoadError(f"SQL Load Error: {e}")

    finally:

        if cursor:
            cursor.close()

        if connection:
            connection.close()


def load_data(df, output_file):
    """
    Main Load Stage
    """

    log_info("Load Stage Started")

    load_to_csv(df, output_file)

    load_to_sql(df)

    log_info("Load Stage Completed Successfully")

    return "Data Loaded Successfully"