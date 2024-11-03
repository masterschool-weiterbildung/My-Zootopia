from pathlib import Path

# OTHERS CONSTANTS

PRODUCTION_FILE = "animals_data.json"

PACKAGE_REPOSITORY = "My-Zootopia"

PRODUCTION_FILE_PATH = Path(
    __file__).parent.parent / PACKAGE_REPOSITORY / PRODUCTION_FILE

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
