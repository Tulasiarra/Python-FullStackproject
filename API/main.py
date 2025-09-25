# main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sys, os

# Import UserManager from src
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.logic import UserManager

# --------------------------- App Setup ---------------------------
app = FastAPI(title="Productivity Management System", version="1.0")

# Allow frontend (Streamlit/React) to call the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------------- Business Logic ---------------------------
user_manager = UserManager()  # Creating a UserManager Instance

# --------------------------- Data Models ---------------------------

# -------- User Models --------
class UserCreate(BaseModel):
    name: str
    email: str
    password: str

class UserUpdate(BaseModel):
    name: str 
    email: str 
    password: str

# -------- Task Models --------
class TaskCreate(BaseModel):
    title: str
    description: str
    status: str  # "pending" or "completed"

class TaskUpdate(BaseModel):
    status: str  # "pending" or "completed"

# -------- Category Models --------
class CategoryCreate(BaseModel):
    name: str
    color: str 
    icon: str 

class CategoryUpdate(BaseModel):
    name: str
    color: str 
    icon: str 

# --------------------------- Endpoints ---------------------------

@app.get("/")
def home():
    return {"message": "Productivity Management System API is running!"}

# --------------------------- User Endpoints ---------------------------
@app.get("/users")
def get_users():
    return user_manager.get_users()

@app.post("/users")
def create_user(user: UserCreate):
    result = user_manager.add_user(user.name, user.email, user.password)
    if not result.get("Success"):
        raise HTTPException(status_code=400, detail=result.get("message"))
    return result

@app.put("/users/{id}")
def update_user(id: int, user: UserUpdate):
    result = user_manager.update_user(id, user.name, user.email, user.password)
    if not result.get("Success"):
        raise HTTPException(status_code=400, detail=result.get("message"))
    return result

@app.delete("/users/{id}")
def delete_user(id: int):
    result = user_manager.delete_user(id)
    if not result.get("Success"):
        raise HTTPException(status_code=400, detail=result.get("message"))
    return result

# --------------------------- Task Endpoints ---------------------------
@app.get("/tasks")
def get_tasks():
    return user_manager.get_tasks()

@app.post("/tasks")
def create_task(task: TaskCreate):
    result = user_manager.add_task(task.title, task.description, task.status)
    if not result.get("Success"):
        raise HTTPException(status_code=400, detail=result.get("message"))
    return result

@app.put("/tasks/{id}")
def update_task(id: int, task: TaskUpdate):
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
    result = user_manager.delete_task(id)
    if not result.get("Success"):
        raise HTTPException(status_code=400, detail=result.get("message"))
    return result

# --------------------------- Category Endpoints ---------------------------
@app.get("/categories")
def get_categories():
    return user_manager.get_categories()

@app.post("/categories")
def create_category(category: CategoryCreate):
    result = user_manager.add_category(category.name, category.color, category.icon)
    if not result.get("Success"):
        raise HTTPException(status_code=400, detail=result.get("message"))
    return result

@app.put("/categories/{id}")
def update_category(id: int, category: CategoryUpdate):
    result = user_manager.update_category(id, category.name, category.color, category.icon)
    if not result.get("Success"):
        raise HTTPException(status_code=400, detail=result.get("message"))
    return result

@app.delete("/categories/{id}")
def delete_category(id: int):
    result = user_manager.delete_category(id)
    if not result.get("Success"):
        raise HTTPException(status_code=400, detail=result.get("message"))
    return result

# --------------------------- Run ---------------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
