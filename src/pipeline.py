import time

from .config_reader import load_config
from .extract import extract_data
from .validate import validate_data
from .transform import transform_data
from .load import load_data
from .logger import log_info, log_error


def run_pipeline():

    log_info("========== ETL Pipeline Started ==========")

    config = load_config()

    batch_size = config["batch_size"]
    max_retries = config["max_retries"]

    offset = 0

    total_batches = 0
    successful_batches = 0
    failed_batches = 0
    total_records = 0

    fastest_batch = float("inf")
    slowest_batch = 0
    total_batch_time = 0

    start_time = time.time()

    while True:

        df = extract_data(offset, batch_size)

        if df.empty:
            log_info("No More Records Found")
            break

        total_batches += 1
        total_records += len(df)

        retry_count = 0

        batch_start_time = time.time()

        while retry_count < max_retries:

            try:

                validated_df = validate_data(df)

                transformed_df = transform_data(validated_df)

                load_data(transformed_df)

                successful_batches += 1

                batch_execution_time = (
                    time.time() - batch_start_time
                )

                total_batch_time += batch_execution_time

                fastest_batch = min(
                    fastest_batch,
                    batch_execution_time
                )

                slowest_batch = max(
                    slowest_batch,
                    batch_execution_time
                )

                log_info(
                    f"Batch {total_batches} Completed Successfully"
                )

                break

            except Exception as e:

                retry_count += 1

                log_error(
                    f"Batch {total_batches} Failed "
                    f"(Retry {retry_count}/{max_retries}) : {e}"
                )

                if retry_count == max_retries:

                    failed_batches += 1

                    log_error(
                        f"Skipping Batch {total_batches}"
                    )

        offset += batch_size

    end_time = time.time()

    execution_time = end_time - start_time

    average_batch_time = (
        total_batch_time / successful_batches
        if successful_batches > 0
        else 0
    )

    records_per_second = (
        total_records / execution_time
        if execution_time > 0
        else 0
    )

    batches_per_minute = (
        total_batches / (execution_time / 60)
        if execution_time > 0
        else 0
    )

    log_info("========== ETL SUMMARY ==========")

    log_info(f"Total Batches : {total_batches}")
    log_info(f"Successful Batches : {successful_batches}")
    log_info(f"Failed Batches : {failed_batches}")
    log_info(f"Total Records : {total_records}")

    log_info(f"Execution Time : {execution_time:.2f} Seconds")

    log_info(f"Fastest Batch : {fastest_batch:.2f} Seconds")
    log_info(f"Slowest Batch : {slowest_batch:.2f} Seconds")
    log_info(f"Average Batch : {average_batch_time:.2f} Seconds")

    log_info(f"Records / Second : {records_per_second:.2f}")
    log_info(f"Batches / Minute : {batches_per_minute:.2f}")

    log_info("========== ETL Pipeline Completed ==========")