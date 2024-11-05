import constant
import data_util


def result_message(result: bool, message: str, payload) -> dict:
    """
    Creates a structured result message as a dictionary.

    Parameters:
        result (bool): Status of the result, usually indicating
                       success or failure.
        message (str): Informative message about the result.
        payload: Additional data associated with the result.

    Returns:
        dict: A dictionary with keys for result status, message, and payload.
    """
    return {constant.RESULT: result, constant.MESSAGE: message,
            constant.PAYLOAD: payload}


def get_animals() -> str:
    """
    Retrieves animal data from a JSON file and formats it
    as a plain-text string.

    Iterates over each animal's data to retrieve and format
    attributes such as name, diet, location, and type. Skips entries
    if certain keys are missing.

    Returns:
        str: A formatted string with animal details.

    Raises:
        KeyError: Skips any iteration with missing type
    """
    output = ''
    for animal in (data_util.fetch_data_json(constant.JSON_FILE_PATH))[constant.PAYLOAD]:
        try:
            animal[constant.CHARACTERISTICS][constant.TYPE]
            output += f"Name: {animal[constant.NAME]}\n"
            output += f"Diet: {animal[constant.CHARACTERISTICS][constant.DIET]}\n"
            output += f"Location: {animal[constant.LOCATIONS][0]}\n"
            output += f"Type: {animal[constant.CHARACTERISTICS][constant.TYPE]}\n"
        except KeyError:
            continue
    return output


def get_serialize_animals() -> str:
    """
    Retrieves animal data and formats it as HTML list items with basic details.

    Returns:
        str: A string containing HTML-formatted list items with animal details.

    Raises:
        KeyError: Skips any iteration with missing type
    """
    output = ''
    for animal in data_util.fetch_data_json(constant.JSON_FILE_PATH)[constant.PAYLOAD]:
        try:
            animal[constant.CHARACTERISTICS][constant.TYPE]
            output += '<li class="cards__item">'
            output += f"Name: {animal[constant.NAME]}<br/>\n"
            output += f"Diet: {animal[constant.CHARACTERISTICS][constant.DIET]}<br/>\n"
            output += f"Location: {animal[constant.LOCATIONS][0]}<br/>\n"
            output += f"Type: {animal[constant.CHARACTERISTICS][constant.TYPE]}<br/>\n"
        except KeyError:
            continue
    return output


def get_final_serialization_animals() -> str:
    """
    Retrieves animal data and formats it as detailed HTML cards for final
    output.

    Iterates over animal data and formats each as an HTML card with title
    and details including location, type, and diet, skipping entries with
    missing data.

    Returns:
        str: A string containing HTML-formatted cards with animal details.

    Raises:
        KeyError: Skips any iteration with missing type
    """
    output = ''
    for animal in data_util.fetch_data_json(constant.JSON_FILE_PATH)[constant.PAYLOAD]:
        try:
            animal[constant.CHARACTERISTICS][constant.TYPE]
            output += '<li class="cards__item">'
            output += (f"<div class='card__title'>{animal[constant.NAME]}</div>")
            output += "<p class='card__text'>"
            output += (f"<strong>Location:</strong> "
                       f"{animal[constant.LOCATIONS][0]}<br/>")
            output += (f"<strong>Type:</strong> "
                       f"{animal[constant.CHARACTERISTICS][constant.TYPE]}<br/>")
            output += (f"<strong>Diet:</strong> "
                       f"{animal[constant.CHARACTERISTICS][constant.DIET]}<br/>")
            output += "</p'>"
            output += "</li'>"
        except KeyError:
            continue
    return output


def get_final_serialization_from_api_animals(animal) -> str:

    return_value_from_api = data_util.fetch_data_api(animal)[
        constant.PAYLOAD]

    output = ''
    for animal in return_value_from_api:
        try:
            animal[constant.CHARACTERISTICS][constant.TYPE]
            output += '<li class="cards__item">'
            output += (f"<div class='card__title'>{animal[constant.NAME]}</div>")
            output += "<p class='card__text'>"
            output += (f"<strong>Location:</strong> "
                       f"{animal[constant.LOCATIONS][0]}<br/>")
            output += (f"<strong>Type:</strong> "
                       f"{animal[constant.CHARACTERISTICS][constant.TYPE]}<br/>")
            output += (f"<strong>Diet:</strong> "
                       f"{animal[constant.CHARACTERISTICS][constant.DIET]}<br/>")
            output += "</p'>"
            output += "</li'>"
        except KeyError:
            continue
    return output


def replace_html_content() -> str:
    """
    Replaces a placeholder in an HTML template with plain-text animal data.

    Fetches HTML content and replaces the "__REPLACE_ANIMALS_INFO__"
    placeholder with the output from `get_animals`.

    Returns:
        str: The HTML content with animal data in place of the placeholder.
    """
    return_value = data_util.fetch_data_html(constant.HTML_FILE_PATH)[
        constant.PAYLOAD]
    return ''.join(return_value).replace("__REPLACE_ANIMALS_INFO__",
                                         get_animals())


def replace_html_with_serialize_items() -> str:
    """
    Replaces a placeholder in an HTML template with HTML list items of
    animal data.

    Fetches HTML content and replaces the "__REPLACE_ANIMALS_INFO__"
    placeholder with the output from `get_serialize_animals`.

    Returns:
        str: The HTML content with animal list items in place of the
             placeholder.
    """
    return_value = data_util.fetch_data_html(constant.HTML_FILE_PATH)[
        constant.PAYLOAD]
    return ''.join(return_value).replace("__REPLACE_ANIMALS_INFO__",
                                         get_serialize_animals())


def replace_html_with_final_serialize_items() -> str:
    """
    Replaces a placeholder in an HTML template with detailed HTML
    cards of animal data.

    Fetches HTML content and replaces the "__REPLACE_ANIMALS_INFO__"
    placeholder with the output from `get_final_serialization_animals`.

    Returns:
        str: The HTML content with animal cards in place of the placeholder.
    """
    return_value = data_util.fetch_data_html(constant.HTML_FILE_PATH)[
        constant.PAYLOAD]

    return ''.join(return_value).replace("__REPLACE_ANIMALS_INFO__",
                                         get_final_serialization_animals())

def replace_html_from_api_items(animal) -> str:
    return_value = data_util.fetch_data_html(constant.HTML_FILE_PATH)[
        constant.PAYLOAD]

    return ''.join(return_value).replace("__REPLACE_ANIMALS_INFO__",
                                         get_final_serialization_from_api_animals(animal))
