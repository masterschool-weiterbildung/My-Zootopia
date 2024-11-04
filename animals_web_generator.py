from dataclasses import replace

import constant
import data_util
import print_util
from data_util import write_data
from misc_util import get_animals, replace_html_content


def main():
    write_data(replace_html_content(),constant.NEW_HTML_FILE_PATH)


if __name__ == '__main__':
    main()
