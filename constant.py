from pathlib import Path

# OTHERS CONSTANTS

JSON_FILE = "animals_data.json"
HTML_FILE = "animals_template.html"
NEW_HTML_FILE = "animals.html"
NEWLINE = "\n"

PACKAGE_REPOSITORY = "My-Zootopia"

JSON_FILE_PATH = Path(
    __file__).parent.parent / PACKAGE_REPOSITORY / JSON_FILE

HTML_FILE_PATH = Path(
    __file__).parent.parent / PACKAGE_REPOSITORY / HTML_FILE

NEW_HTML_FILE_PATH = Path(
    __file__).parent.parent / PACKAGE_REPOSITORY / NEW_HTML_FILE


# ANIMALS API

ANIMALS_API_URL = "https://api.api-ninjas.com/v1/animals"

# RETURN CONSTANT

RESULT = "result"
MESSAGE = "message"
PAYLOAD = "payload"

# KEYS TO PARSE

NAME = "name"

LOCATIONS = "locations"

# PARENT
CHARACTERISTICS = "characteristics"
# CHILD
DIET = "diet"
TYPE = "type"
