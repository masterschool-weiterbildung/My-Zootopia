import requests
import data_fetcher


def main():
    try:
        data_fetcher.fetch_data()
    except requests.exceptions.RequestException as e:
        print("Please check if the .env file exists and if the KEY is present.")


if __name__ == '__main__':
    main()
