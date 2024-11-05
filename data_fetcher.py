import constant
import input_util
import print_util


def fetch_data():
    result = print_util.generate_animals_web(input_util.input_animal_name())
    if result[constant.RESULT]:
        print_util.print_animal_successfully_fetched()
    else:
        print_util.print_animal_un_successfully_fetched()