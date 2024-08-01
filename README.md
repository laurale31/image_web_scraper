# README for URL Metadata Fetching and Processing Script

## Overview

This script is designed to fetch and process metadata from URLs obtained by performing a Google Lens image lookup. It retrieves the source code from the constructed Google Lens URL, extracts unique URLs using regex, and collects metadata from each URL. The metadata includes the title, keywords, and media type of the content. The metadata is then saved to a CSV file.

## Prerequisites

- Python 3.x
- `urllib` library (standard library in Python)
- `http.cookiejar` library (standard library in Python)
- `re` library (standard library in Python)
- `csv` library (standard library in Python)
- `bs4` library (BeautifulSoup)

## Setup

Before running the script, ensure you have the BeautifulSoup library installed. You can install it using pip:

```bash
pip install beautifulsoup4
```

## Usage

### 1. Import Libraries

The script starts by importing necessary libraries:

```python
import urllib.request
from http.cookiejar import CookieJar
import re
import csv
from bs4 import BeautifulSoup
```

### 2. Setting Up the Cookie Jar and Opener

A cookie jar and opener are set up to handle HTTP requests with cookies and a user-agent header:

```python
cj = CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
opener.addheaders = [
    ('User-agent', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17')
]
```

### 3. Fetch Metadata Function

The `fetch_metadata` function retrieves metadata for a given URL. It extracts the title, keywords, and media type (video or image) from the HTML content:

```python
def fetch_metadata(url):
    # Function implementation
```

### 4. Count URLs Function

The `count_urls` function counts the number of unique URLs in a list:

```python
def count_urls(urls):
    return len(urls)
```

### 5. Image Lookup Function

The `imageLookup` function performs the following tasks:

1. Defines the image URL and constructs the Google Lens URL.
2. Retrieves the source code from the constructed URL.
3. Uses regex to find URLs in the source code, excluding google.com and gstatic.com domains.
4. Converts the list of URLs to a set to remove duplicates.
5. Counts the number of unique URLs.
6. Fetches metadata for each unique URL.
7. Dumps the metadata to a CSV file.

```python
def imageLookup():
    # Function implementation
```

### 6. Main Function

The main function calls the `imageLookup` function:

```python
if __name__ == "__main__":
    imageLookup()
```

## Output

The script outputs the metadata to a CSV file named `url_metadata.csv`. The CSV file contains the following columns:

- `url`: The URL of the content.
- `title`: The title of the content.
- `keywords`: The keywords associated with the content.
- `media_type`: The media type of the content (video or image).

## Example

To run the script, simply execute it in your Python environment:

```bash
python script_name.py
```

Replace `script_name.py` with the name of your script file.

## Notes

- Ensure that the image URL used in the `imageLookup` function is valid and accessible.
- The script handles exceptions and prints an error message if metadata fetching fails for any URL.

This README file provides a detailed overview of the script's functionality and usage, helping users understand and utilize the code effectively.
