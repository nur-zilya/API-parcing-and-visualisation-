import requests
import json

url = 'https://hacker-news.firebaseio.com/v0/item/19155826.json'
r = requests.get(url)
print(f"Status: {r.status_code}")

response_dict = r.json()
readable = 'readable_hn_data.json'
with open(readable, 'w') as f:
    json.dump(response_dict, f, indent=4)
