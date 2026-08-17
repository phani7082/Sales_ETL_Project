from pipeline import run_pipeline
from logger import log_info, log_error


def main():

    try:

        log_info("========== APPLICATION STARTED ==========")

        run_pipeline()

        log_info("========== APPLICATION FINISHED ==========")

    except KeyboardInterrupt:

        log_error("Pipeline Interrupted By User")

    except Exception as e:

        log_error(f"Application Failed : {e}")

        raise


if __name__ == "__main__":

    main()