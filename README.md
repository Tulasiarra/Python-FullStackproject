# Productivity Management System

## Description

The **Productivity Management System** is a Python-based application designed to help users efficiently manage their daily tasks and improve overall productivity. It provides a structured and user-friendly way to organize tasks, track progress, and prioritize activities based on urgency and importance.

Users can create tasks with detailed descriptions, categorize them (e.g., Work, Personal, Study), set priority levels (Low, Normal, High), define deadlines, and track their completion status. Tasks can be updated, marked as completed, or deleted when no longer needed. The system also allows searching and filtering tasks for quick access.

The backend is powered by **Supabase**, which handles database storage and user authentication securely. Each user's data is stored safely in the cloud, enabling seamless access and data integrity across devices.

The system is modular, with separate components for business logic, database operations, API endpoints, and frontend interface, making it easy to maintain, extend, or integrate with other tools. This system is ideal for managing personal, academic, or professional tasks in an organized manner.

## Features

- **User Authentication**: Secure sign-up and login using Supabase Auth.
- **Task Management**: Create, read, update, and delete tasks.
- **Categorization & Priority**: Assign tasks to categories and set priority levels.
- **Deadline Tracking**: Monitor deadlines and task completion status.
- **Search & Filter**: Quickly find tasks based on category, priority, or status.
- **Cloud Storage**: All data is stored securely in Supabase.

## Project Structure
Productivity Management System/
|
|---src/             # core application logic
|     |---logic.py   #Business logic and task
operations
|     |__db.py       #Database operations
|
|----API/            #Backend API
|     |__main.py     #FastAPI endpoints
|
|----Frontend/       #Frontend application
|      |__app.py     #Streamlit web interface
|
|_requirements.txt  #Python Dependencies
|
|_README.md        #Project decumentation
|
|_.env             #Python Variables


## Quick start

## prerequisites


  -Python 3.8 or higher
  -A Supabase account
  -Git(push,cloning)

### 1.clone or Download the project
# option 1:clone with Git
git clone https://github.com/Tulasiarra/Python-FullStackproject.git

# option 2:Download and extract the ZIP file
### 2.Install Dependencies

# Install all required python packages
pip install -r requirements.txt

### 3.Set Up Supabase Database

  1.Create a Supabase Project:
  2.Create the Task Table:

  -Go to the SQL Edition in your Supabase dashboard
  -Run this SQL command:
  ```sql
  CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE tasks (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    title TEXT NOT NULL,
    description TEXT,
    category TEXT,
    priority TEXT CHECK (priority IN ('Low', 'Normal', 'High')),
    status TEXT CHECK (status IN ('Pending', 'Completed')),
    deadline DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE categories (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    name TEXT NOT NULL,
    color TEXT,         
    icon TEXT,          
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
3. **Get your Creadentials:

### 4. Configure Environment variables

1. Create a `.env` file in the project root

2. Add your Supabase credentials to `.env`
SUPABASE_URL=your_project_url_here
SUPABSE_KEY=your_anon_key_here


**Example:**
SUPABASE_URL="https://kwabjxhjzngdrymabnxc.supabase.co"
SUPABASE_KEY="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imt3YWJqeGhqem5nZHJ5bWFibnhjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTg2OTU5NDgsImV4cCI6MjA3NDI3MTk0OH0.dWSnB82h4oE1UADN1uEwQZ3uYSU4NTmeCIZlr8GvJ7Q"

### 5.Run the application

## streamlit Frontend
streamlit run forward/app.py

The app will open in your browser at `http://localhost:3000`

## FASTAPI Backend

cd API
python main.py

The App will be available at `http://localhost:8000`
   

# How to Use
## Technical Details


### Technologies used


-**Frontend**:Streamlit(python web frameork)
-**Backend**:FASTAPI(python REST API framework)
-**Database**:supabase(postgreSQL-based backend-as-a-service)
-**Language**:python 3.8+

### key components

1. **`src/db.py`**:Database operations
    -Handles all CRUD opeartions with supabase

2. **`src/logic.py`**:Business logic
    -Task validation and processing


## TroubleShooting

## Common Issues

1. **"Module not Found" errors**
     -Make sure you've installed all dependencies:`pip install -r requirements.txt`
     -Check that you're running commands from the correct directory

## Future Enhancements

Ideas for extending this project:

- **Notifications**: Send email or push reminders for upcoming deadlines.  
- **File Attachments**: Attach files or images to tasks.  
- **Recurring Tasks**: Support daily, weekly, or monthly repeating tasks.  
- **Task Progress**: Track progress with percentages or status updates.  
- **Analytics Dashboard**: Visualize completed and pending tasks.  
- **Collaboration**: Share tasks with other users for teamwork.  


# support

If you encounter any issues or have questions:
Mail Id:tulasiarra16@gmail.com
phone:6305781701
