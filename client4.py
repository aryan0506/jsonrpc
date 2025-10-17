import requests
import json
# now providing url through which i can post clients request to the json - rpc server
url = "http://localhost:8000/jsonrpc"
# now making sturctured formate to posting clients request in the form of json-rpc 2.0 version
payload = {
    "jsonrpc": "2.0",
    "method": "get_repo_files",
    "params": {"repo_url": "https://github.com/aryan0506/email-agent"},
    "id": 1,
}

# now we have an structured client input payload to post request to the server url 
response = requests.post(url , json = payload)
print(json.dumps(response.json() , indent = 4))