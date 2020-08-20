import requests

response = requests.get('http://api.open-notify.org/astros.json').json()

print("People in space: ", response["number"])

for person in response["people"]:
    print(person["name"] + " is on the " + person["craft"])


