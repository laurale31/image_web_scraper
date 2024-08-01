import urllib.request
from http.cookiejar import CookieJar
import re
import csv
from bs4 import BeautifulSoup

# Setting up the cookie jar and opener
cj = CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
opener.addheaders = [
    ('User-agent', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17')
]

def fetch_metadata(url):
    """Fetch metadata for a given URL."""
    try:
        response = opener.open(url)
        html = response.read().decode('utf-8')
        soup = BeautifulSoup(html, 'html.parser')

        metadata = {
            'url': url,
            'title': soup.title.string if soup.title else 'No title',
            'keywords': '',
            'media_type': 'unknown'  # Default media type
        }

        for meta in soup.find_all('meta'):
            if 'name' in meta.attrs:
                if meta.attrs['name'].lower() == 'keywords':
                    metadata['keywords'] = meta.attrs['content']
            if 'property' in meta.attrs:
                if meta.attrs['property'].lower() == 'og:type':
                    og_type = meta.attrs['content'].lower()
                    if 'video' in og_type:
                        metadata['media_type'] = 'video'
                    elif 'image' in og_type:
                        metadata['media_type'] = 'image'

        # Heuristic to determine media type if not found in meta tags
        if metadata['media_type'] == 'unknown':
            if soup.find('video'):
                metadata['media_type'] = 'video'
            elif soup.find('img'):
                metadata['media_type'] = 'image'

        return metadata
    except Exception as e:
        print(f"Failed to fetch metadata for {url}: {e}")
        return None

def count_urls(urls):
    """Count the number of unique URLs."""
    return len(urls)
    
def imageLookup():
    # Define the image URL and construct the Google Lens URL
    image_path = "https://cdn.britannica.com/92/212692-050-D53981F5/labradoodle-dog-stick-running-grass.jpg"
    google_path = "https://lens.google.com/uploadbyurl?url=" + image_path

    # Retrieve the source code from the constructed URL
    sourceCode = opener.open(google_path).read().decode('utf-8')

    # Use regex to find URLs in the source code, excluding google.com and gstatic.com domains
    regex_pattern = r'https://(?:www\.(?!google\.com|gstatic\.com)[^\s"<>]*)+"'
    findLinks = re.findall(regex_pattern, sourceCode)

    # Convert the list of URLs to a set to remove duplicates
    unique_urls = set(findLinks)

    # Count the number of unique URLs
    num_urls = count_urls(unique_urls)
    print(f"Number of unique URLs: {num_urls}")

    # Store metadata for each unique URL
    url_metadata = []
    for url in unique_urls:
        url = url.rstrip('"')  # Remove the trailing quote
        metadata = fetch_metadata(url)
        if metadata:
            url_metadata.append(metadata)

    # Dump metadata to a CSV file
    with open('url_metadata.csv', 'w', newline='') as csv_file:
        fieldnames = ['url', 'title', 'keywords', 'media_type']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(url_metadata)

if __name__ == "__main__":
    imageLookup()
