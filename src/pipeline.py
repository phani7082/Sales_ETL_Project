import time

from .config_reader import load_config
from .extract import extract_data
from .validate import validate_data
from .transform import transform_data
from .load import load_data
from .logger import log_info, log_error


def run_pipeline():

    try:

        log_info("Pipeline Started")

        start_time = time.time()

        config = load_config()

        source_file = config["source_file"]
        destination_file = config["destination_file"]

        data = extract_data(source_file)

        validate_data(data)

        clean_data = transform_data(data)

        status = load_data(clean_data, destination_file)

        end_time = time.time()

        execution_time = end_time - start_time

        log_info(f"Pipeline Execution Time: {execution_time:.2f} seconds")
        log_info("Pipeline Completed Successfully")

        print(status)

    except Exception as e:

        log_error(str(e))

        print(e)