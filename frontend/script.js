// frontend/script.js

const taskForm = document.getElementById("task-form");
const taskList = document.getElementById("task-list");

const apiUrl = "http://127.0.0.1:8000/tasks/";

// Function to fetch all tasks and display them
async function fetchTasks() {
    const response = await fetch(apiUrl);
    const tasks = await response.json();
    taskList.innerHTML = "";
    tasks.forEach(task => {
        const li = document.createElement("li");
        li.innerHTML = `
            <span>${task.title} - ${task.completed ? "Completed" : "Pending"}</span>
            <button class="delete" onclick="deleteTask(${task.id})">Delete</button>
        `;
        taskList.appendChild(li);
    });
}

// Function to create a new task
taskForm.addEventListener("submit", async (e) => {
    e.preventDefault();
    const taskId = document.getElementById("task-id").value;
    const taskTitle = document.getElementById("task-title").value;
    const taskDescription = document.getElementById("task-description").value;

    const newTask = {
        id: parseInt(taskId),
        title: taskTitle,
        description: taskDescription,
        completed: false,
    };

    await fetch(apiUrl, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(newTask),
    });

    taskForm.reset();
    fetchTasks(); // Refresh the task list
});

// Function to delete a task
async function deleteTask(taskId) {
    await fetch(`${apiUrl}${taskId}`, {
        method: "DELETE",
    });
    fetchTasks(); // Refresh the task list
}

// Initial fetch of tasks
fetchTasks();
