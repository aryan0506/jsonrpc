import requests
import json
url = "http://localhost:8000/jsonrpc"
# the code we want to check''
my_code = '''
          def add(a , b):
            return a+b'''
#the message we want to send to the server
payload = {
    "jsonrpc": "2.0",
    "method": "review_code",
    "params": {"code": my_code},
    "id": 1,
}
# send this to the server
response = requests.post(url , json = payload)
# print what the server replied
print(json.dumps(response.json() , indent = 4))

