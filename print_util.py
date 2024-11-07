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
    for animal in data_util.fetch_data_html(constant.JSON_FILE_PATH)[constant.PAYLOAD]:
        try:
            serialize_animal(animal)
        except KeyError:
            continue


def serialize_animal(animal: dict) -> None:
    """
    Serializes and prints information about an animal.

    This function extracts and prints the name, diet, location, and
    type of the given animal from the provided dictionary.

    Parameter:
        animal (dict): A dictionary containing animal data. Expected keys:
            - constant.NAME: The name of the animal.
            - constant.CHARACTERISTICS: A dictionary with keys like
              'DIET' and 'TYPE'.
            - constant.LOCATIONS: A list with the location of the animal.

    Returns:
        None: This function only prints the information to the console.
    """
    animal[constant.CHARACTERISTICS][constant.TYPE]
    print(f"Name: {animal[constant.NAME]}")
    print(f"Diet: {animal[constant.CHARACTERISTICS][constant.DIET]}")
    print(f"Location: {animal[constant.LOCATIONS][0]}")
    print(f"Type: {animal[constant.CHARACTERISTICS][constant.TYPE]}")


def generate_animals_web(animal: str) -> misc_util.result_message:
    """
    Generates an HTML page based on animal data fetched from the API.

    This function retrieves animal information using the
    `replace_html_from_api_items` function, which fetches animal data and
    replaces a placeholder in the HTML template. The generated HTML
    content is then written to a new HTML file. The function returns
    a result message indicating whether the page generation was successful
    or not.

    Parameter:
        animal (str): The name of the animal whose data is used to
                      generate the HTML page.

    Returns:
        misc_util.result_message: A result message object containing:
            - `RESULT` (bool): Indicates whether the page generation
                               was successful.
            - `MESSAGE` (str): A descriptive message about the status of
                               the operation.
            - `PAYLOAD` (str): The content that was written to the file,
                               if applicable.
    """
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


def print_animal_successfully_fetched() -> None:
    print("Website was successfully generated to the file animals.html.")


def print_animal_un_successfully_fetched() -> None:
    print("No animal information was retrieved.")
