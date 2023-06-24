import datetime
import platform
import psutil


def get_performance_metrics():
    """Fetches the performance metrics of the system.

    Returns:
        dict: A dictionary containing the performance metrics.
    """
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent

    return {
        'cpu_usage': cpu_usage,
        'memory_usage': memory_usage
    }


def get_local_time_string():
    """Fetches the local time on the given machine as a formatted string.

    Returns:
        str: A string corresponding to the local time.
    """
    current_time = datetime.datetime.now()
    return current_time.strftime("%H:%M:%S")


def get_machine_details():
    """Fetches the operating system (OS) and additional machine details for the API server.

    Returns:
        dict: A dictionary containing the OS and additional machine details.
    """
    return {
        'system': platform.system(),
        'release': platform.release(),
        'version': platform.version(),
        'machine': platform.machine(),
        'processor': platform.processor()
    }
