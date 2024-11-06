import data_util
import constant
import misc_util
from misc_util import result_message


def print_animals() -> None:
    """
    Prints details of each animal by fetching and serializing data.


    Raises:
        KeyError: Skips any animal entry with missing expected keys.
    """
    for animal in data_util.fetch_data_html(constant.JSON_FILE_PATH)[
        constant.PAYLOAD]:
        try:
            serialize_animal(animal)
        except KeyError:
            continue


def serialize_animal(animal: dict) -> None:
    animal[constant.CHARACTERISTICS][constant.TYPE]
    print(f"Name: {animal[constant.NAME]}")
    print(f"Diet: {animal[constant.CHARACTERISTICS][constant.DIET]}")
    print(f"Location: {animal[constant.LOCATIONS][0]}")
    print(f"Type: {animal[constant.CHARACTERISTICS][constant.TYPE]}")


def generate_animals_web(animal) -> misc_util.result_message:
    result = misc_util.replace_html_from_api_items(animal)

    if result[constant.RESULT]:

        return data_util.write_data(
            result[constant.PAYLOAD],
            constant.NEW_HTML_FILE_PATH)
    else:

        data_util.write_data(result[constant.PAYLOAD],
                             constant.NEW_HTML_FILE_PATH)

        return result_message(result[constant.RESULT],
                              result[constant.MESSAGE],
                              "")


def print_animal_successfully_fetched():
    print("Website was successfully generated to the file animals.html.")


def print_animal_un_successfully_fetched():
    print("No animal information was retrieved.")
