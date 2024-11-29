import requests

headers = {
    'Authorization': 'Bearer 1479c9a21b29e5b43598380543093a80ec768b09',
    'Content-Type': 'application/json',
}

data = '{ "long_url": "https://www.youtube.com", "domain": "bit.ly"}'

response = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers, data=data)

print(response.text)