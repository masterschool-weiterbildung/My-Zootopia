from dataclasses import replace

import constant
import data_util
import print_util
from data_util import write_data
from misc_util import get_animals, replace_html_content, \
    replace_html_with_serialize_items


def main():
    write_data(replace_html_with_serialize_items(),constant.NEW_HTML_FILE_PATH)


if __name__ == '__main__':
    main()
