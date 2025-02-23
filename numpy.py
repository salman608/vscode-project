import requests
from bs4 import BeautifulSoup

# URL of the GeeksforGeeks website
url = "https://www.geeksforgeeks.org/"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all article sections (adjust based on the website's structure)
    articles = soup.find_all('div', class_='head')

    # Loop through and extract titles and links
    for i, article in enumerate(articles, 1):
        title = article.text.strip()
        link = article.find('a')['href']
        print(f"{i}. {title} - {link}")
else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")



