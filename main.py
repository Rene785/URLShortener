import requests
import sys

headers = {
    'Authorization': 'Bearer 1479c9a21b29e5b43598380543093a80ec768b09',
    'Content-Type': 'application/json',
}
print("Allowed expressions:\n")
print("     shorten urlToShorten")
print("     expand bitlinkToExpand\n")

expression = input("Enter your command:")
expression = expression.split(" ")

if expression.__len__ is not 2:
    print("Invalid Expression. Program only accepts expression of the type 'command link'.")
    sys.exit("Exiting program")

command = expression[0]
link = expression[1]

if not command.startswith("shorten") or not command.startswith("expand"):
    print("Invalid command: " + command[0])
    sys.exit("Exiting program")

if command.startswith("shorten"):
    data = '{"long_url": "'+ link + '"}'
    endpoint = 'https://api-ssl.bitly.com/v4/shorten'

if command.startswith("expand"):
    data = '{"bitlink_id": "'+ link + '"}'
    endpoint = 'https://api-ssl.bitly.com/v4/expand'

response = requests.post(endpoint, headers=headers, data=data)

print(response.text)