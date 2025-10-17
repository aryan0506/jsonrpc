from fastapi import FastAPI , Request
from fastapi.responses import JSONResponse
import requests

# step 1st is to make instance of FASTAPI
app = FastAPI()
# step 2 :making post route to handle clients request
@app.post("/jsonrpc")
async def handle_jsonrpc(request:Request):
    # step 3 : read the data send by client
    data = await request.json()
    
    method_name = data.get("method")
    params = data.get("params" , {})
    id = data.get("id")

    # step 2 : hendle the method the client asked for
    if method_name == "get_repo_info":
        repo_url = params.get("repo_url")
        result = get_repo_info(repo_url)  # here we call our own helper fumction
        #method 2 : get_repo_files
    elif method_name == "get_repo_files":
        repo_url = params.get("repo_url")
        result = get_repo_files(repo_url)


        # step 3: send response back to the client
        return JSONResponse({
            "jsonrpc":"2.0",
            "result":result,
            "id":id
        })
    # else condition when method not found 
    else:
        return JSONResponse({
            "jsonrpc":"2.0",
            "error":{
                "code":-32601,
                "message":"Method not found"
            },
            "id":id
        })
    

    
    # step 4: now we have to build the helper function through which we get the data from gitub 
def get_repo_info(repo_url):
        # Example: https://github.com/fastapi/fastapi
        # we only need owner ans repo name from the url which is in the last two part
    parts = repo_url.split("github.com/")[-1].strip("/")
    api_url = f"https://api.github.com/repos/{parts}"

    # call github api to get repo info
    response = requests.get(api_url)
    if response.status_code != 200:
        return {"error":"Failed to fetch repo info from github"}
    data = response.json()
   # return only usefull fields
    return {
        "name":data["name"],
        "owner":data["owner"]["login"],
        "stars":data["stargazers_count"],
        "forks":data["forks_count"],
        "description":data["description"]
    }

#  fuction for the method 2
def get_repo_files(repo_url):
    parts = repo_url.split("github.com/")[-1].strip("/")
    api_url = f"https://api.github.com/repos/{parts}/contents"
    r = requests.get(api_url)
    if r.status_code != 200:
        return {"error":"Failed to fetch repo files from github"}   
    data = r.json()
    # return only name or files
    files = []
    for item in data:
        files.append({
            "name":item["name"],
            "type":item["type"],
            "size":item["size"],
            "url":item["url"],
            "download_url":item.get("download_url",None)
        })
    return {"total_items": len(files) , "files":files}
     



