import pyodbc

from .config_reader import load_config
from .logger import log_info, log_error
from .exceptions import DatabaseConnectionError


def get_connection():

    try:

        config = load_config()

        server = config["server"]
        database = config["database"]
        driver = config["driver"]
        trusted_connection = config["trusted_connection"]

        connection_string = (
            f"DRIVER={{{driver}}};"
            f"SERVER={server};"
            f"DATABASE={database};"
            f"Trusted_Connection={trusted_connection};"
        )

        connection = pyodbc.connect(connection_string)

        log_info("Connected to SQL Server Successfully")

        return connection

    except Exception as e:

        log_error(f"Database Connection Failed : {e}")

    

        raise DatabaseConnectionError("Unble to connect SQL Server")

    from e 

