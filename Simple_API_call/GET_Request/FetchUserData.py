import requests

# API Url
url = 'https://reqres.in/api/users?page=2'

# Send Get request
response = requests.get(url)

# Display Response Content
print(response.content)
print(response.headers)
