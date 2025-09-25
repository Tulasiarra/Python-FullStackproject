# src/logic.py

from db_manager import DatabaseManager
import uuid
from datetime import datetime


# ---------------------------
# User Manager
# ---------------------------
class UserManager:
    def __init__(self):
        self.db = DatabaseManager()

    def add_user(self, name, email, password):
        if not name or not email or not password:
            return {"Success": False, "Message": "Name, email, and password are required"}

        user_id = str(uuid.uuid4())
        created_at = datetime.now().isoformat()

        result = self.db.create_user(user_id, name, email, password, created_at)
        if result.get("data"):
            return {"Success": True, "Message": "User added successfully"}
        else:
            return {"Success": False, "Message": f"Error: {result.get('error')}"}

    def get_all_users(self):
        return self.db.get_all_users()

    def update_user(self, user_id, updates: dict):
        result = self.db.update_user(user_id, updates)
        if result.get("data"):
            return {"Success": True, "Message": "User updated successfully"}
        else:
            return {"Success": False, "Message": f"Error: {result.get('error')}"}

    def delete_user(self, user_id):
        result = self.db.delete_user(user_id)
        if result.get("data"):
            return {"Success": True, "Message": "User deleted successfully"}
        else:
            return {"Success": False, "Message": f"Error: {result.get('error')}"}


# ---------------------------
# Task Manager
# ---------------------------
class TaskManager:
    def __init__(self):
        self.db = DatabaseManager()

    def add_task(self, user_id, title, description="", category="", priority="Normal", status="Pending", deadline=None):
        if not user_id or not title:
            return {"Success": False, "Message": "User ID and title are required"}

        task_id = str(uuid.uuid4())
        created_at = datetime.now().isoformat()

        result = self.db.create_task(task_id, user_id, title, description, category, priority, status, deadline, created_at)
        if result.get("data"):
            return {"Success": True, "Message": "Task added successfully"}
        else:
            return {"Success": False, "Message": f"Error: {result.get('error')}"}

    def get_all_tasks(self):
        return self.db.get_all_tasks()

    def update_task(self, task_id, updates: dict):
        result = self.db.update_task(task_id, updates)
        if result.get("data"):
            return {"Success": True, "Message": "Task updated successfully"}
        else:
            return {"Success": False, "Message": f"Error: {result.get('error')}"}

    def mark_complete(self, task_id):
        return self.update_task(task_id, {"status": "Completed"})

    def mark_pending(self, task_id):
        return self.update_task(task_id, {"status": "Pending"})

    def delete_task(self, task_id):
        result = self.db.delete_task(task_id)
        if result.get("data"):
            return {"Success": True, "Message": "Task deleted successfully"}
        else:
            return {"Success": False, "Message": f"Error: {result.get('error')}"}


# ---------------------------
# Category Manager
# ---------------------------
class CategoryManager:
    def __init__(self):
        self.db = DatabaseManager()

    def add_category(self, user_id, name, color="", icon=""):
        if not user_id or not name:
            return {"Success": False, "Message": "User ID and name are required"}

        category_id = str(uuid.uuid4())
        created_at = datetime.now().isoformat()

        result = self.db.create_category(category_id, user_id, name, color, icon, created_at)
        if result.get("data"):
            return {"Success": True, "Message": "Category added successfully"}
        else:
            return {"Success": False, "Message": f"Error: {result.get('error')}"}

    def get_all_categories(self):
        return self.db.get_all_categories()

    def update_category(self, category_id, updates: dict):
        result = self.db.update_category(category_id, updates)
        if result.get("data"):
            return {"Success": True, "Message": "Category updated successfully"}
        else:
            return {"Success": False, "Message": f"Error: {result.get('error')}"}

    def delete_category(self, category_id):
        result = self.db.delete_category(category_id)
        if result.get("data"):
            return {"Success": True, "Message": "Category deleted successfully"}
        else:
            return {"Success": False, "Message": f"Error: {result.get('error')}"}
