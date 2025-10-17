from fastapi import FastAPI , Request
import subprocess # to talk with ollama
from fastapi.responses import JSONResponse
# create our server
app = FastAPI()
# our only one end point 
@app.post("/jsonrpc")
async def handle_jsonrpc(request:Request):
    #get the data that the client sends
    data = await request.json()
    # now the task is to get the method name parameters and id that i user send us
    method = data.get("method")
    params = data.get("params",{})# parameter send by client
    id = data.get("id") # id send by client
#  now we have all info that the client sent us now its time to oerform the method that the client sent us 
    if method == "review_code":
        code = params.get("code")
        result = review_code_with_ollama(code)  # here review_code_with_ollama(code) is our helper function
        return JSONResponse({
            "jsonrpc" : "2.0",
            "result": result,
            "id": id
        })
    return JSONResponse({
        "jsonrpc":"2.0",
        "error": {
            "code": -32601,
            "message" : "Unknown method"
        },
        "id":id
    })
# now making helper function that talks with ollama
def review_code_with_ollama(code:str) ->str:
    """this fuction sends the code text to ollama and ask 
        it to review the code"""
    # if no code is given
    if not code.strip():
        return "no code is give to review"
    # prepare the question to send it ollama
    prompt = f"You are a senior software engineerReview the following code and make it better : \n\n{code}"
    result = subprocess.run(
        ["ollama", "run", "gemma2", prompt], capture_output=True, text=True
    )
    # if ollama failed to run 
    if result.returncode != 0:
        return "ollama failed to run"
    # return the result
    return result.stdout.strip() # strip is used to remove the extra spaces and new lines
    


