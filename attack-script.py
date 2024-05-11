import requests
import time
import random

url = "http://v1.localhost"
headers = {
    "User-Agent": "PostmanRuntime/7.38.0",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive"
}

while True:
    # Randomly changing the 'Attack' header
    headers['Attack'] = "true" if bool(random.getrandbits(1)) else "false"
   

    response = requests.get(url, headers=headers)
    
    if "HEHEHE!" in response.text:
        print("Attack")
    else:
        print("Normal Request")
    
    time.sleep(2)  # Wait for 2 seconds before sending the next request
