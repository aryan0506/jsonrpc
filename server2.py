#here acctual code how we define available method 
from fastapi import FastAPI , Request
from fastapi.responses import JSONResponse

app = FastAPI()

# now we define avilable method to the sever this is acctually a a function
def add(a,b):  #method 1.
    return a+b

def subtract(a,b):  # method 2.
    return a-b

def multiply(a, b):  # method 3.
    return a*b

def divide(a, b):  # method 4.
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a/b
def greet(name):  # method 5.
    return f"Hello, {name}! "

#here we are making list of methods
methods = {
    "add":add,
    "subtract":subtract,
    "multiply": multiply,
    "divide" : divide,
    "greet" : greet
}

# defining post method 
@app.post("/jsonrpc")
async def handle_jsonrpc(request:Request):
    try:
        #1. parse JSON body
        data = await request.json()
        #2. validate json-prc structure
        if data.get("jsonrpc")!= "2.0":
            raise ValueError("invalid JSON-RPC")
        method_name = data.get("method")
        params = data.get("params" , {})
        req_id = data.get("id")

        #3. check if method exist or not
        if method_name not in methods:
            raise ValueError("Method not found")
        
        #4. call the method
        result = methods[method_name](**params)

        # return success response
        return JSONResponse({
            "jsonrpc":"2.0",
            "result":result,
            "id":req_id
        })
    
    except Exception as e:
        #6. Handle errors
        return JSONResponse({
            "jsonrpc":"2.0",
            "error":{
                "code":-32603 , 
                "message":str(e)
            },
            "id":data.get("id",None)
        })



        


 