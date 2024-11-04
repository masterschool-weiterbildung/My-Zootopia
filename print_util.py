import data_util
import constant
import misc_util


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
        except KeyError as e:
            continue


def serialize_animal(animal: dict) -> None:
    """
    Serializes and prints details of a single animal.

    Given a dictionary representing an animal, this function formats and prints
    its name, diet, primary location, and type based on predefined keys.

    Parameter:
        animal (dict): A dictionary containing details about a single animal.
        Expected keys include constant.NAME, constant.CHARACTERISTICS,
        constant.LOCATIONS, and within CHARACTERISTICS,
        keys for constant.DIET and constant.TYPE.

    Raises:
        KeyError: If any expected keys are missing from the animal dictionary.
    """
    var = animal[constant.CHARACTERISTICS][constant.TYPE]
    print(f"Name: {animal[constant.NAME]}")
    print(f"Diet: {animal[constant.CHARACTERISTICS][constant.DIET]}")
    print(f"Location: {animal[constant.LOCATIONS][0]}")
    print(f"Type: {animal[constant.CHARACTERISTICS][constant.TYPE]}")


def generate_animals_web() -> None:
    """
    Generates an HTML file with serialized animal data by processing
    and formatting raw HTML content.

    Returns:
        None

    Raises:
        IOError: If the file at the specified path cannot be written to.
    """
    data_util.write_data(misc_util.replace_html_with_final_serialize_items(),
                         constant.NEW_HTML_FILE_PATH)
