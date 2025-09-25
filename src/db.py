# Frontend ---> API ---> logic ---> db ---> Response
# API/main.py

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sys, os

# Import UserManager from src
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.logic import UserManager

# --------------------------- App Setup ---------------------------
app = FastAPI(title="Productivity Management System", version="1.0")

# --------------------------- Allow frontend (Streamlit/React) to call the API ---------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins (frontend apps)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Creating a UserManager Instance (business logic)
user_manager = UserManager()

# --------------------------- Data Models ---------------------------
class TaskCreate(BaseModel):
    """
    Schema for creating a task
    """
    title: str
    description: str
    status: str  # e.g., "pending", "completed"

class TaskUpdate(BaseModel):
    """
    Schema to update a task
    """
    status: str  # e.g., "pending" or "completed"

# --------------------------- Endpoints ---------------------------
@app.get("/")
def home():
    """
    Check if the API is running
    """
    return {"message": "Productivity Management System API is running!"}

@app.get("/tasks")
def get_tasks():
    """
    Get all tasks
    """
    return user_manager.get_tasks()

@app.post("/tasks")
def create_task(task: TaskCreate):
    """
    Add a new task
    """
    result = user_manager.add_task(task.title, task.description, task.status)
    if not result.get("Success"):
        raise HTTPException(status_code=400, detail=result.get("message"))
    return result

@app.put("/tasks/{id}")
def update_task(id: int, task: TaskUpdate):
    """
    Update task status (completed or pending)
    """
    result = (
        user_manager.mark_complete(id)
        if task.status.lower() == "completed"
        else user_manager.mark_pending(id)
    )
    if not result.get("Success"):
        raise HTTPException(status_code=400, detail=result.get("message"))
    return result

@app.delete("/tasks/{id}")
def delete_task(id: int):
    """
    Delete a task
    """
    result = user_manager.delete_task(id)
    if not result.get("Success"):
        raise HTTPException(status_code=400, detail=result.get("message"))
    return result



#-------Run------

if _name=="main_":
    import uvicorn
    uvicorn.run("main:app",host="0.0.0.0",port=8000,reload=True)