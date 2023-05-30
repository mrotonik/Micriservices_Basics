import requests
import json
import uuid

# POST запит
msg = "Hello, World!"
response = requests.post("http://localhost:5000/", data=json.dumps({"msg": msg}), headers={'Content-Type': 'application/json'})
print(response.text)

# GET запит
response = requests.get("http://localhost:5000/")
print(response.text)
