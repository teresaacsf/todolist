# To-Do List Application

This is a simple To-Do List application built using FastAPI for the backend and vanilla JavaScript, HTML, and CSS for the frontend. The application allows users to create, update, delete, and toggle the completion status of tasks.

## Features

- **Create a Task:** Add a new task with a title, optional description, and a unique ID.
- **View Tasks:** View a list of all tasks, including their status (completed or not).
- **Update a Task:** Modify the title, description, and completion status of an existing task.
- **Delete a Task:** Remove a task from the list.
- **Toggle Task Completion:** Quickly mark tasks as completed or not completed.

## Project Structure

todolist/
├── frontend/
│ ├── index.html # Main HTML file for the frontend
│ ├── script.js # JavaScript file for frontend logic
│ └── styles.css # CSS file for styling the frontend
├── main.py # FastAPI backend implementation
├── requirements.txt # Python dependencies
└── README.md # Project documentation

markdown

## Setup and Installation

### Prerequisites

- Python 3.8+
- pip (Python package installer)
- Git

### Installation Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/teresaacsf/todolist.git
   cd todolist
Create a virtual environment:


python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install dependencies:


pip install -r requirements.txt
Run the FastAPI server:


uvicorn main:app --reload
Open the application in your browser:

Navigate to http://127.0.0.1:8000/static/index.html to view the To-Do List application.

### Usage
Add a Task: Fill in the task ID, title, and optionally the description in the form, then click "Add Task."
Update a Task: Click on the task in the list, modify its details, and submit.
Delete a Task: Click on the delete button next to a task to remove it from the list.
Toggle Completion: Click on a task's checkbox to mark it as complete or incomplete.
API Endpoints
The FastAPI backend provides the following API endpoints:

POST /tasks/: Create a new task.
GET /tasks/: Retrieve all tasks.
GET /tasks/{task_id}: Retrieve a task by its ID.
PUT /tasks/{task_id}: Update a task by its ID.
DELETE /tasks/{task_id}: Delete a task by its ID.
PATCH /tasks/{task_id}/toggle: Toggle the completion status of a task.

