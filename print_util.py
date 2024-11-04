import data_util
import constant


def print_animals():
    for animal in data_util.fetch_data_html(constant.JSON_FILE_PATH)[constant.PAYLOAD]:
        try:
            animal[constant.CHARACTERISTICS][constant.TYPE]
            print(f"Name: {animal[constant.NAME]}")
            print(f"Diet: {animal[constant.CHARACTERISTICS][constant.DIET]}")
            print(f"Location: {animal[constant.LOCATIONS][0]}")
            print(f"Type: {animal[constant.CHARACTERISTICS][constant.TYPE]}")
        except KeyError as e:
            continue

