# main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse  # Add this import

app = FastAPI()
app.mount("/static", StaticFiles(directory="frontend"), name="static")


# Define the data model for a task
class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

# In-memory storage for tasks
tasks = []

@app.get("/", response_class=HTMLResponse)
async def root():
    with open("frontend/index.html", "r") as file:
        return file.read()

# Create a new task
@app.post("/tasks/", response_model=Task)
async def create_task(task: Task):
    # Check if the task ID already exists
    if any(existing_task.id == task.id for existing_task in tasks):
        raise HTTPException(status_code=400, detail="Task ID already exists.")
    
    tasks.append(task)
    return task

# Retrieve all tasks
@app.get("/tasks/", response_model=List[Task])
async def get_tasks():
    return tasks

# Retrieve a task by ID
@app.get("/tasks/{task_id}", response_model=Task)
async def get_task(task_id: int):
    task = next((task for task in tasks if task.id == task_id), None)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# Update a task by ID
@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, updated_task: Task):
    for task in tasks:
        if task.id == task_id:
            task.title = updated_task.title
            task.description = updated_task.description
            task.completed = updated_task.completed
            return task  # Return the updated task
    raise HTTPException(status_code=404, detail="Task not found")


# Delete a task by ID
@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            return {"message": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")

@app.patch("/tasks/{task_id}/toggle", response_model=Task)
async def toggle_task_completion(task_id: int):
    for task in tasks:
        if task.id == task_id:
            task.completed = not task.completed  # Toggle the completed status
            return task
    raise HTTPException(status_code=404, detail="Task not found")
