# db.py
import os
from supabase import create_client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase = create_client(url, key)


# ---------------------------
# Users Table
# ---------------------------
def create_user(id, name, email, password, created_at):
    return supabase.table("users").insert({
        "id": id,
        "name": name,
        "email": email,
        "password": password,
        "created_at": created_at
    }).execute()


def get_all_users():
    return supabase.table("users").select("*").execute()


def update_user(id, updates: dict):
    # updates should be a dictionary with only fields you want to change
    return supabase.table("users").update(updates).eq("id", id).execute()


def delete_user(id):
    return supabase.table("users").delete().eq("id", id).execute()


# ---------------------------
# Tasks Table
# ---------------------------
def create_task(id, user_id, title, description, category, priority, status, deadline, created_at):
    return supabase.table("tasks").insert({
        "id": id,
        "user_id": user_id,
        "title": title,
        "description": description,
        "category": category,
        "priority": priority,
        "status": status,
        "deadline": deadline,
        "created_at": created_at
    }).execute()


def get_all_tasks():
    return supabase.table("tasks").select("*").execute()


def update_task(id, updates: dict):
    return supabase.table("tasks").update(updates).eq("id", id).execute()


def delete_task(id):
    return supabase.table("tasks").delete().eq("id", id).execute()


# ---------------------------
# Categories Table
# ---------------------------
def create_category(id, user_id, name, color, icon, created_at):
    return supabase.table("categories").insert({
        "id": id,
        "user_id": user_id,
        "name": name,
        "color": color,
        "icon": icon,
        "created_at": created_at
    }).execute()


def get_all_categories():
    return supabase.table("categories").select("*").execute()


def update_category(id, updates: dict):
    return supabase.table("categories").update(updates).eq("id", id).execute()


def delete_category(id):
    return supabase.table("categories").delete().eq("id", id).execute()
