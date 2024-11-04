import constant
import data_util


def result_message(result: bool, message: str, payload) -> dict:
    return {constant.RESULT: result, constant.MESSAGE: message,
            constant.PAYLOAD: payload}


def get_animals() -> str:
    output = ''
    for animal in data_util.fetch_data_json(constant.JSON_FILE_PATH)[
        constant.PAYLOAD]:
        try:
            animal[constant.CHARACTERISTICS][constant.TYPE]
            output += f"Name: {animal[constant.NAME]}\n"
            output += f"Diet: {animal[constant.CHARACTERISTICS][constant.DIET]}\n"
            output += f"Location: {animal[constant.LOCATIONS][0]}\n"
            output += f"Type: {animal[constant.CHARACTERISTICS][constant.TYPE]}\n"
        except KeyError as e:
            continue
    return output

def get_serialize_animals() -> str:
    output = ''
    for animal in data_util.fetch_data_json(constant.JSON_FILE_PATH)[
        constant.PAYLOAD]:
        try:
            animal[constant.CHARACTERISTICS][constant.TYPE]
            output += '<li class="cards__item">'
            output += f"Name: {animal[constant.NAME]}<br/>\n"
            output += f"Diet: {animal[constant.CHARACTERISTICS][constant.DIET]}<br/>\n"
            output += f"Location: {animal[constant.LOCATIONS][0]}<br/>\n"
            output += f"Type: {animal[constant.CHARACTERISTICS][constant.TYPE]}<br/>\n"
        except KeyError as e:
            continue
    return output


def replace_html_content() -> str:
    return_value = data_util.fetch_data_html(constant.HTML_FILE_PATH)[
        constant.PAYLOAD]
    return ''.join(return_value).replace("__REPLACE_ANIMALS_INFO__",
                                         get_animals())

def replace_html_with_serialize_items() -> str:
    return_value = data_util.fetch_data_html(constant.HTML_FILE_PATH)[
        constant.PAYLOAD]
    return ''.join(return_value).replace("__REPLACE_ANIMALS_INFO__",
                                         get_serialize_animals())