# An API that can run different tasks, we'll represent a database and create the database in memory, instead of linking a database
# Tasks will be CREATE Tasks, DELETE Tasks, UPDATE Tasks.
# First, we create a model that represents our different tasks. TO do that, we'll import a few different libraries
# Next we create a class that represents the objects we'll be passing around in the API. We do this writing a pydantic model (a data validation and parsing tool), which Python takes and converts to JSON
# In the Pydantic Model/Class, we define the fields and the data type that enters.
# Next we create a post request endpoint, which tells the system we want to add something.
# def create_task(task: Task): - Specifies that we want to accept creating a new task using th pydantic model
# 


from fastapi import FastAPI, HTTPException
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

@app.post("/tasks", response_model=Task) # Runs the Task moodel on the post endpoint at thr /tasks url
def create_task(task: Task):
    task.id = uuid4()
    tasks.append(task)
    return task
# The code above collects valid data for task is wrapped in the class Task object and it gets a unique id, we can append it into the tasks database 


@app.get("/tasks/", response_model=List[Task]) # It's okay for the post and get endpoints url to be the same as long as the request types are different
def read_tasks():
    return tasks # A list of different "Task"

# To view/read a task based on its ID
@app.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: UUID):
    for task in tasks:
        if task.id == task_id:
            return task
        
    raise HTTPException(status_code=404, detail="Task not found")

# To update a task
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: UUID, task_update: Task):
    for idx, task in enumerate(tasks):
        if task.id == task_id:
            updated_task = task.copy(update=task_update.dict(exclude_unset=True)) #Look at the new fields for Task and updates with the dictionary representation of the entry.
            tasks[idx] = updated_task
            return updated_task
        
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: UUID):
    for idx, task in enumerate(tasks):
        if task.id == task_id:
            return tasks.pop(idx)
        
    raise HTTPException(status_code=404, detail="Task not found")

if __name__ == "__main__":
    import uvicorn #a web server that lets us run the API

    uvicorn.run("databaseRep:app", host="127.0.0.1", port=8001) # app name on windows should be "main:app"