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
            output += (
                f"<div class='card__title'>{animal[constant.NAME]}</div>")
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


def get_final_serialization_from_api_animals(animal: str) -> str:
    """
    Fetches animal data from the API and returns a serialized HTML string.

    This function retrieves animal data using data_util.fetch_data_api(animal)`.
    If data is returned successfully, it processes the animal information and
    formats it into an HTML list item for display, showing details like
    location, type, and diet. If the data is not found, it returns an HTML
    message indicating that the animal does not exist.

    Parameter:
        animal (str): The name of the animal to fetch data for.

    Returns:
        str: A string containing HTML-formatted animal information
             or a message indicating that the animal doesn't exist.
    """
    return_value_from_api = data_util.fetch_data_api(animal)

    output = ''

    if return_value_from_api[constant.RESULT]:
        for animal in return_value_from_api[constant.PAYLOAD]:
            try:
                animal[constant.CHARACTERISTICS][constant.TYPE]
                output += '<li class="cards__item">'
                output += (
                    f"<div class='card__title'>{animal[constant.NAME]}</div>")
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

        return result_message(True,
                              "Animal information has been fetched successfully.",
                              output)

    else:
        output += '<li class="cards__item">'
        output += (" <h2 style='color: red;"
                   "width: 80%;font-weight: bold;background-color: yellow;"
                   "padding: 10px;border: 3px solid red;"
                   "border-radius: 5px;text-transform: uppercase;'>"
                   f"The animal {animal}  doesn't exist.</h2>")
        output += "</li'>"

        return result_message(False,
                              f"The animal {animal}  doesn't exist", output)


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


def replace_html_from_api_items(animal: str) -> dict:
    """
    Replaces a placeholder in an HTML template with animal data fetched from the API.

    This function loads an HTML template from a specified file path, fetches
    animal data from the API using get_final_serialization_from_api_animals(animal)`,
    and replaces the placeholder (`__REPLACE_ANIMALS_INFO__`) in the template
    with the serialized animal information. The resulting HTML string is then
    returned.

    Parameter:
        animal (str): The name of the animal whose data will be inserted
        into the HTML template.

    Returns:
        dict: The HTML content with the animal information inserted at the
        placeholder location.
    """
    return_value = data_util.fetch_data_html(constant.HTML_FILE_PATH)[
        constant.PAYLOAD]

    return_value_api = get_final_serialization_from_api_animals(
        animal)

    return result_message(return_value_api[constant.RESULT],
                          return_value_api[constant.MESSAGE],
                          ''.join(return_value).replace(
                              "__REPLACE_ANIMALS_INFO__",
                              return_value_api[constant.PAYLOAD])
                          )
