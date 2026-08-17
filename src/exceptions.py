class ETLError(Exception):
    """Base class for ETL Exceptions"""
    pass


class DatabaseConnectionError(ETLError):
    pass


class ValidationError(ETLError):
    pass


class TransformationError(ETLError):
    pass


class LoadError(ETLError):
    pass