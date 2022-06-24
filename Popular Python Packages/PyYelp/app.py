import requests

# What are APIS
# Application programming interfaces, publicy available
# Methods: GET POST PUT DELETE
# REST = Representational state transfer = conventions and rules of apis

# client id is like a username
# api key is kinda like a password

# Needed for when we talk to api server

url = "https://api.yelp.com/v3/businesses/search"
api_key = "jzxYj529w_l1T6f6MavEieW2rXsh1WaJwIpN4-dgbcw1MDNSxZqJj0KDjD6wE80YsP1M56gLDLHitWMiKXxntUWXNPsfhH8-jYW9Eulz9bUpghwWRNb56dKd30G0YnYx"


headers = {
    "Authorization": "Bearer " + api_key
}

params = {
    "term": "burger",
    "location": "92503"
}
response = requests.get(url, headers=headers, params=params)
businesses = response.json()["businesses"]
# print(businesses)
names = [business["name"]
         for business in businesses if business["rating"] > 4]
print(names)

# for business in businesses:
# print(business["name"])
