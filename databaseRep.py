# An API that can run different tasks, we'll represent a database and create the database in memory, instead of linking a database
# Tasks will be CREATE Tasks, DELETE Tasks, UPDATE Tasks.
# First, we create a model that represents our different tasks. TO do that, we'll import a few different libraries
# Next we create a class that represents the objects we'll be passing around in the API. We do this writing a pydantic model, which Python takes and converts to JSON
# In the Class, we define the fields and the data type that enters

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from uuid import UUID, uuid4 # A python function that always guarantees a unique id.

app = FastAPI() # Creates an instance of FastAPI

class Task(BaseModel):
    id: Optional[UUID] = None #Ensures the id is unique
    title: str #Data type should be a string
    description: Optional[str] = None #Filling the description is optional
    completed: bool = False

tasks = []

@app.get("/") # A basic route get endpoint i.e a get request at the / url, which means logging to that url, is sending the app a request hence the "get request" endpoint
def read():
    return {"hello": "world"} # Return this dictionary when you get a request

if __name__ == "__databaseRep__":
    import uvicorn #a web server that lets us run the API

    uvicorn.run("databaseRep:app", host="0.0.0.0", port=8000) # app name on windows should be "main:app"