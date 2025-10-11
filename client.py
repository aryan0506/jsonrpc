# here we connect our jsonrpc server with our client 
import requests

url = "http://localhost:8000/jsonrpc"#this is the url where our json-rpc server is running

#2 create a JSON-RPC request message
# here client ask for addintion
'''payload = {
    "jsonrpc":"2.0",  
    "method":"add",
    "params":{
        "a":10,
        "b":20
    },
     "id":1
}'''
# here client ask for multiplication
'''payload = {
    "jsonrpc":"2.0",
    "method":"multiply",
    "params":{
        "a":10,
        "b":20
    },
    "id":2
}'''
# here client ask for prediction of sentiment in the text by using server
payload = {
    "jsonrpc":"2.0",
    "method" : "predict",
    "params" : {
        "text": "i love python"
    },
    "id":3
}
#3. send  this payload to the server
response = requests.post(url,json=payload)

print(response.json())
