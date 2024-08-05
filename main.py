import requests
from bs4 import BeautifulSoup

# Define the URL of the news site you want to scrape
url = 'https://example-news-site.com'  # Replace with the actual URL

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find and extract headlines
    # This will vary based on the structure of the website
    # For example, if headlines are in <h2> tags with a class 'headline'
    headlines = soup.find_all('h2', class_='headline')

    # Print the extracted headlines
    for index, headline in enumerate(headlines, start=1):
        print(f"Headline {index}: {headline.get_text(strip=True)}")

else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
