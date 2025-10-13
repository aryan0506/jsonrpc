import requests
url = "http://localhost:8000/jsonrpc"

def send_jsonrpc_request(method , params , id):
    payload ={
        "jsonrpc":"2.0",
         "method":method,
         "params":params,
         "id":id
    }
    response = requests.post(url , json = payload)
    return response.json()
def send_batch_request(request_list):
    response = requests.post(url , json = request_list)
    return response.json()

# test: single request
print(send_jsonrpc_request("add", {"a":2, "b":4}, 1))
print(send_jsonrpc_request("subtract", {"a":10, "b":5}, 2))
 # test: batch request
batch_request = [
    {"jsonrpc":"2.0", "method":"divide", "params":{"a":2, "b":4}, "id":1},
    {"jsonrpc":"2.0", "method":"multiply", "params":{"a":10, "b":5}, "id":2}
]
print(send_batch_request(batch_request))
