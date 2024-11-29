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
expression = expression.split()

print("Processing expression")
if len(expression) != 2:
    print("Invalid Expression. Program only accepts expression of the type 'command link'.")
    sys.exit("Exiting program")

command = expression[0]
link = expression[1]

if not command.casefold() == "shorten".casefold() and not command.casefold() == "expand".casefold():
    print("Invalid command: " + command)
    sys.exit("Exiting program")

if command.casefold() == "shorten".casefold():
    data = '{ "long_url": "'+ link + '" }'
    endpoint = 'https://api-ssl.bitly.com/v4/shorten'

if command.casefold() == "expand".casefold():
    data = '{ "bitlink_id": "'+ link + '" }'
    endpoint = 'https://api-ssl.bitly.com/v4/expand'

print("Sending request")
response = requests.post(endpoint, headers=headers, data=data)

if response.status_code in [200,201]:
    print("Request successful")
    print("Status Code " + str(response.status_code))
    message = response.text.split(",")

    print("----------------------------------")
    print(message[0])
    print(message[1])
    print(message[2])
    if(command.casefold() == "expand".casefold()):
        print(message[3])
    if(command.casefold() == "shorten".casefold()):
        print(message[4])
    print("----------------------------------")

if response.status_code in [400,403,404,429,500,503]:
    print("Request failed")
    print("Status Code " + response.status_code)
    message = response.text.split(",")
    print("----------------------------------")
    print(message[0])
    print(message[1])
    print(message[2])
    print("----------------------------------")

print("Exiting program.")