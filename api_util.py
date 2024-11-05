import json

from dotenv import load_dotenv

import requests
import constant
import os

import misc_util


def get_headers() -> str:
    load_dotenv()

    key = os.getenv('KEY')

    headers = {
        'X-Api-Key': key
    }
    return headers


def get_paramatersl() -> str:
    return f"?name=Fox"


def get_animal_data_from_api() -> json:
    try:
        response = requests.get(constant.ANIMALS_API_URL + get_paramatersl(),
                                headers=get_headers(),
                                verify=True,
                                timeout=5)

        response.raise_for_status()

        if response.status_code == 200:
            return (misc_util.result_message
                    (True, "Animal information has been fetched successfully.",
                     response.json()))

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    except ValueError as e:
        print("Error parsing JSON response:", e)


def main():
    print(get_animal_data_from_api())


if __name__ == '__main__':
    main()
