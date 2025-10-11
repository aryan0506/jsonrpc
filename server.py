from fastapi import FastAPI , Request
from fastapi.responses import JSONResponse

app=FastAPI()

# this end point will going to handle all Json-RPC messages
@app.post("/jsonrpc")
async def handle_jsonrpc(request:Request):
    #1. Get JSON body
    data = await request.json()

    #2. extract method ,parameters and and id 
    method = data.get("method")
    params =data.get("params",{})
    id_ = data.get("id")
    
    #3. handle only one method for now:add
    if method == "add":
        a =params.get("a")
        b= params.get("b")
        result = a+b

     #4. return json-rpc style result
        return JSONResponse({
            "jsonrpc": "2.0",
            "result":result,
            "id": id_
       })
    # here we add new maethod in server by using jsonrpc
    elif method == "multiply":
        a = params.get("a")
        b = params.get("b")
        result = a*b 
        return JSONResponse(
            {"jsonrpc":"2.0",
             "result":result,
             "id":id_
             })
    # here we add another Ai type conditional predictor method in our server by using jsonrpc.
    elif method =="predict":
        text = params.get("text", "").lower()
        if "good" in text or "love" in text:
            result = "positive"
        elif "bad" in text or "hate" in text:
            result = "negative"
        else:
            result = "neutral"
        return JSONResponse({
            "jsonrpc": "2.0",
            "result":result,
            "id": id_
        })                
    else:
        #unknown method 
        return JSONResponse({
            "jsonrpc": "2.0",
            "error":{
                "code":-32601,
                "message":"Method not found"
            },
            "id": id_
        })
    
   

