from data_util import fetch_data
import constant


def print_animals():
    for animal in fetch_data(constant.PRODUCTION_FILE_PATH)[constant.PAYLOAD]:
        try:
            print(f"Type: {animal[constant.CHARACTERISTICS][constant.TYPE]}")
            print(f"Name: {animal[constant.NAME]}")
            print(f"Diet: {animal[constant.CHARACTERISTICS][constant.DIET]}")
            print(f"Location: {animal[constant.LOCATIONS][0]}")
        except KeyError as e:
            continue
