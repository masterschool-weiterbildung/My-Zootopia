import json
from pathlib import WindowsPath

import misc_util

cached_data_json = None
cached_data_html = None


def load_data_json(file_path: WindowsPath) -> misc_util.result_message:
    """
    Loads data from a JSON file and returns a result message with the
    file's contents.

    Parameter:
        file_path (WindowsPath): The path to the JSON file to load.

    Returns:
        misc_util.result_message: A structured message indicating
        success or failure, with the JSON payload if successful,
        or an error message if not.

    Raises:
        FileNotFoundError: If the file cannot be located.
        IOError: If there is an issue reading the file.
        Exception: For any other unexpected errors encountered.
    """
    try:
        with open(file_path, "r") as handle:
            payload = json.load(handle)
    except FileNotFoundError:
        return (misc_util.result_message
                (False,
                 "Error: The file was not found.", ""))
    except IOError:
        return (misc_util.result_message
                (False,
                 "Error: Could not read the file.", ""))
    except Exception as e:
        return (misc_util.result_message
                (False,
                 f"An unexpected error occurred: {e}",
                 ""))
    else:
        return (misc_util.result_message
                (True, "File loaded successfully.",
                 payload))


def load_data_html(file_path: WindowsPath) -> misc_util.result_message:
    """
    Loads data from an HTML file and returns a result message with the
    file's contents.

    Parameter:
        file_path (WindowsPath): The path to the HTML file to load.

    Returns:
        misc_util.result_message: A structured message indicating
        success or failure, with the HTML content as a list if successful,
        or an error message if not.

    Raises:
        FileNotFoundError: If the file cannot be located.
        IOError: If there is an issue reading the file.
        Exception: For any other unexpected errors encountered.
    """
    try:
        with open(file_path, "r") as handle:
            payload = handle.readlines()
    except FileNotFoundError:
        return (misc_util.result_message
                (False,
                 "Error: The file was not found.", ""))
    except IOError:
        return (misc_util.result_message
                (False,
                 "Error: Could not read the file.", ""))
    except Exception as e:
        return (misc_util.result_message
                (False,
                 f"An unexpected error occurred: {e}",
                 ""))
    else:
        return (misc_util.result_message
                (True, "File loaded successfully.",
                 payload))


def fetch_data_json(file_path: WindowsPath) -> misc_util.result_message:
    """
    Fetches cached JSON data if available; otherwise, loads it from file.

    Uses a cached version of the JSON data if present; if not, loads the data
    from the specified file path and caches it for future access.

    Parameter:
        file_path (WindowsPath): The path to the JSON file.

    Returns:
        misc_util.result_message: A result message containing the JSON
        data if successful, or an error message if not.
    """
    global cached_data_json
    if cached_data_json is None:
        cached_data_json = load_data_json(file_path)
    return cached_data_json


def fetch_data_html(file_path: WindowsPath) -> misc_util.result_message:
    """
    Fetches cached HTML data if available; otherwise, loads it from file.

    Uses a cached version of the HTML data if present; if not, loads the data
    from the specified file path and caches it for future access.

    Args:
        file_path (WindowsPath): The path to the HTML file.

    Returns:
        misc_util.result_message: A result message containing the HTML
        data if successful, or an error message if not.
    """
    global cached_data_html
    if cached_data_html is None:
        cached_data_html = load_data_html(file_path)
    return cached_data_html


def write_data(details: str,
               file_path: WindowsPath) -> misc_util.result_message:
    """
    Writes data to a specified file path and returns a result message.

    Parameters:
        details (str): The content to write to the file.
        file_path (WindowsPath): The path where the data should be written.

    Returns:
        misc_util.result_message: A structured message indicating
        success or failure, with a success message if written successfully
        or an error message if not.

    Raises:
        FileNotFoundError: If the file cannot be found.
        IOError: If there is an issue writing to the file.
        Exception: For any other unexpected errors encountered.
    """
    try:
        with open(file_path, 'w') as write_to_file:
            write_to_file.write(details)
    except FileNotFoundError:
        return (misc_util.result_message
                (False,
                 "Error: The file was not found.", ""))
    except IOError:
        return (misc_util.result_message
                (False,
                 "Error: Could not write to the file.",
                 ""))
    except Exception as e:
        return (misc_util.result_message
                (False,
                 f"An unexpected error occurred: {e}",
                 ""))
    else:
        return (misc_util.result_message
                (True, "File written successfully.",
                 ""))
