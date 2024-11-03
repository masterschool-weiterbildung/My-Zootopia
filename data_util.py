import json
from pathlib import WindowsPath

import misc_util

cached_data = None


def load_data(file_path: WindowsPath) -> misc_util.result_message:
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


def fetch_data(file_path: WindowsPath) -> misc_util.result_message:
    global cached_data

    if cached_data is None:
        cached_data = load_data(file_path)
    return cached_data
