import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# WIFI login page URL
login_url = "http://www.testwifi.com/redirect"

# User credentials
username = "your_ID"
password = "your_password"

# Create a session object to maintain the state between requests
session = requests.Session()

# Send a GET request to the login page and retrieve the HTML response
response = session.get(login_url)
html = response.content

# Parse the HTML response using BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Extract the form data (action URL, method, input fields) from the HTML response
form = soup.find("form")
action_url = form["action"]
action_url = urljoin(login_url, action_url) # Resolve relative URL to absolute URL
method = form["method"]
input_fields = {}
for input_tag in form.find_all("input"):
    input_fields[input_tag.get("name")] = input_tag.get("value", "")

# Update the input fields with the user credentials
input_fields["username"] = username
input_fields["password"] = password

# Send a POST request to the action URL with the updated input fields
response = session.post(action_url, data=input_fields)

# Check if the login was successful
if "authentication failed" in response.text.lower():
    print("Login failed")
else:
    print("Login successful")