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


def replace_html_content() -> str:
    return_value = data_util.fetch_data_html(constant.HTML_FILE_PATH)[
        constant.PAYLOAD]
    return ''.join(return_value).replace("__REPLACE_ANIMALS_INFO__",
                                         get_animals())