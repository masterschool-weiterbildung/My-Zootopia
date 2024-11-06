import json

from dotenv import load_dotenv

import requests
import constant
import os

import misc_util


def get_headers() -> str:
    """
    Loads environment variables and retrieves the API key from the .env file.

    Returns:
        dict: A dictionary containing the 'X-Api-Key' header with the
        API key value.
    """
    load_dotenv()

    key = os.getenv('KEY')

    headers = {
        'X-Api-Key': key
    }
    return headers


def get_paramatersl(animal: str) -> str:
    """
    Constructs the query parameter string for the given animal name.

    Paramter:
        animal (str): The name of the animal to be queried.

    Returns:
        str: A query string formatted as '?name=<animal_name>'.
    """
    return f"?name={animal}"


def get_animal_data_from_api(animal: str) -> json:
    """
    Fetches animal data from an external API.

    This function sends a GET request to the animal information API with the
    specified animal name and processes the response. It handles errors such
    as network issues or empty responses and returns a formatted result
    message containing the status, description, and the fetched data.

    Parameter:
        animal (str): The name of the animal to fetch data for.

    Returns:
        dict: A result message containing success or failure status,
              a description, and the fetched data
              (or an empty string if no data is found).

    Raises:
        requests.exceptions.RequestException: If there is an issue
        with the API request. ValueError: If the JSON response
        cannot be parsed.
    """
    try:
        response = requests.get(
            constant.ANIMALS_API_URL + get_paramatersl(animal),
            headers=get_headers(),
            verify=True,  # verify SSL Certificates
            timeout=5)  # 5 seconds timeout

        response.raise_for_status() # Raises HTTPError for bad responses

        if response.status_code == 200:
            if len(response.json()) == 0:
                return (misc_util.result_message
                        (False,
                         "No animal information was retrieved.",
                         ""))
            else:
                return (misc_util.result_message
                        (True,
                         "Animal information has been fetched"
                         "successfully.",
                         response.json()))

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    except ValueError as e:
        print("Error parsing JSON response:", e)
