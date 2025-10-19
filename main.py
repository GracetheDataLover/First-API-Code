from fastapi import FastAPI

app = FastAPI() # Creates an instance of FastAPI

@app.get("/") # A basic route get endpoint i.e a get request at the / url, which means logging to that url, is sending the app a request hence the "get request" endpoint
def read():
    return {"hello": "world"} # Return this dictionary when you get a request

if __name__ == "__main__":
    import uvicorn #a web server that lets us run the API

    uvicorn.run("main:app", host="0.0.0.0", port=8000) # app name on windows should be "main:app"