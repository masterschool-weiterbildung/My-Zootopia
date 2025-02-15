# Animal Data Fetcher

## Overview
This Python project fetches animal data from an external API. It retrieves information based on user input and handles errors gracefully. The project utilizes environment variables for API key security and includes caching mechanisms for efficiency.

## Features
- Fetch animal data from an API using an animal name.
- Caches previously fetched data to optimize performance.
- Handles errors, including network issues and missing API keys.
- Uses structured result messages for better error reporting.

## Requirements
- Python 3.7+
- `requests` library
- `python-dotenv` library

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/masterschool-weiterbildung/My-Zootopia/tree/zootopia-with-api
   cd animal-data-fetcher
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Create a `.env` file and add your API key:
   ```sh
   echo "KEY=your_api_key_here" > .env
   ```

## Usage
```python
from fetch_data import fetch_data
fetch_data()
```

## Code Overview
### `get_headers()`
Loads the API key from `.env` and returns authentication headers.

### `get_parameters(animal: str)`
Formats the query parameter string for API requests.

### `get_animal_data_from_api(animal: str)`
Fetches animal data from the API and returns structured result messages.

## Error Handling
- **Missing API Key:** Raises an error if the API key is missing.
- **Network Issues:** Handles request failures and provides meaningful error messages.
- **Empty Response:** Notifies users when no data is found for an animal.
