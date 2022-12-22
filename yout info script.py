import requests
from bs4 import BeautifulSoup

# Specify the URL of the YouTuber's channel
url = "https://www.youtube.com/channel/UCXXXXXXXXXXXXXXXXX"

# Send an HTTP GET request to the website and store the response
response = requests.get(url)

# Parse the HTML content of the website
soup = BeautifulSoup(response.text, "html.parser")

# Find the element containing the YouTuber's description
description_element = soup.find("yt-formatted-string", attrs={"class": "channel-description"})

# Extract the text of the description element
description = description_element.text.strip()

# Check if the YouTuber is a technical product reviewer
is_reviewer = "technical product reviewer" in description.lower()

# Find the element containing the subscriber count
subscriber_count_element = soup.find("yt-formatted-string", attrs={"class": "subscriber-count"})

# Extract the text of the subscriber count element and convert it to an integer
subscriber_count = int(subscriber_count_element.text.strip().replace(",", ""))

# Find the element containing the contract information
contract_element = soup.find("yt-formatted-string", attrs={"class": "contract-info"})

# Extract the text of the contract element
contract = contract_element.text.strip()

# Print the results
print("Is reviewer:", is_reviewer)
print("Subscriber count:", subscriber_count)
print("Contract:", contract)
