import json
from pathlib import WindowsPath

import misc_util

cached_data_json = None
cached_data_html = None


def load_data_json(file_path: WindowsPath) -> misc_util.result_message:
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
    global cached_data_json
    if cached_data_json is None:
        cached_data_json = load_data_json(file_path)
    return cached_data_json


def fetch_data_html(file_path: WindowsPath) -> misc_util.result_message:
    global cached_data_html
    if cached_data_html is None:
        cached_data_html = load_data_html(file_path)
    return cached_data_html


def write_data(details: str,
               file_path: WindowsPath) -> misc_util.result_message:
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
