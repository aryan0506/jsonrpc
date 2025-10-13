# here we again making server but this time we use logging , and batch of method processing this is practice no 3
from fastapi import FastAPI , Request
from fastapi.responses import JSONResponse
import datetime
app = FastAPI()
def add(a,b):   #method 1
    return a+b
def subtract(a, b): #method 2
    return a-b
def multiply(a,b): #method 3
    return a*b
def divide(a , b): #method 4
    if b == 0:
        raise ValueError("cannot divisble by zero")
    else:
        return a/b
def greet(name): #method 5
    return f"hello {name}"

#listing all the methods
methods = {
    "add": add,
    "subtract": subtract,
    "multiply":multiply,
    "divide": divide,
    "greet": greet
}    
# looging function:
def log_requests(method , params , result=None , error=None):
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if error:
        print(f"[{time}] METHOD : {method} , params : {params} , error : {error}")
    else:
        print(f"[{time}] METHOD : {method}, params : {params}, result : {result}")

@app.post("/jsonrpc")
async def handle_jsonrpc(request:Request):
    try:
        data = await request.json() # here we parse json body
        # ------handle Batch requests ------
        if isinstance(data , list):
            response = [] # here we store all the response in dictionry formate
            for req in data:
                response.append(await process_single_request(req))
            return JSONResponse(response)
            # ------handle single requests ------
       
        response = await process_single_request(data)
        return JSONResponse(response)
        
    except Exception as e:
        return JSONResponse({
            "jsonrpc":"2.0",
            "error":{
                "code":-32603,
                "message":str(e)
            },
            "id":id
        })
    
    #now we have to make function to handle single data request
async def process_single_request(data):
        try:
            
            #check validation for correct json -rpc
            if data.get("jsonrpc")!= "2.0":
                raise ValueError("Invalid JSON-RPC verson")
            else:
                method = data.get("method")
                params = data.get("params" , {})
                id = data.get("id")

                #check if method is exist or not 
                if method not in methods:
                    raise ValueError(f"Method : {method} not found ")
                
                result = methods[method](**params)

                #log request 
                log_requests(method , params , result = result)
                
                # return success reponse
                return {
                    "jsonrpc":"2.0",
                     "result": result,
                     "id": id
                }
            
        except Exception as e:
            # handle error 
            return {
                "jsonrpc":"2.0",
                 "error":{
                     "code": -32603,
                     "message": str(e)
                 },
                 "id": data.get("id", None)
            }


        
        





