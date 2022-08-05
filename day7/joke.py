from distutils.log import error
import requests

url = "https://v2.jokeapi.dev/joke/Programming?blacklistFlags=religious,racist,sexist&idRange=0-185"



response = requests.get(url)
receive_data=response.json()

# print(receive_data)
# print(type(receive_data))
# print(receive_data["category"])

for x in receive_data.keys():
    if x== "id" or x=="type" or x=="flags" or x=="error":
        continue
    print("{} : {}".format(x,receive_data[x]))
