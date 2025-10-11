#here we request to the server by jsonrpc 
import requests

url = "http://localhost:8000/jsonrpc"

# now defining the function to request to server
def send_request(method , params , req_id = 1):
    payload  = {
        "jsonrpc":"2.0",
        "method":method,
        "params" : params,
        "id": req_id
    }
    response = requests.post(url , json=payload)
    return response.json()

# calling the fuction to request the server
result = send_request("add", {"a":2 , "b":4})
print(result)
result = send_request("subtract",{"a":13 , "b":10})
print(result)
result = send_request("multiply", {"a":2, "b":4})
print(result)
result = send_request("divide", {"a":10, "b":2})
print(result)
result = send_request("greet" , {"name":"Aryan"})
print(result)