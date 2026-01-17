# 📝 To-Do Console Application (Python)

A fully functional **console-based To-Do application** built with Python. The system supports **user authentication**, **role-based permissions (Admin / Regular User)**, and complete **task management features** including creation, editing, deletion, searching, sorting, filtering, and deadline reminders.

---

##  Features

### Authentication System

* Register & Login using email and password
* Passwords are securely hashed using `hashlib (PBKDF2)`
* Email format validation
* Egyptian mobile number validation
* Unique National ID (14 digits)

### Roles & Permissions

#### Admin Role

* Automatically assigned to the **first registered user**
* View all users
* Activate / Deactivate users
* View all tasks
* Delete **any task**

####  Regular User Role

* Register as inactive (requires admin activation)
* Login only when status is **active**
* Manage **only their own tasks**

---

## Task Management System

Each task includes:

* Task ID
* Title
* Description (optional)
* Priority (Low / Medium / High)
* Status (To-Do / In Progress / Completed)
* Due Date (must be in the future)
* Owner (task creator)

### Available Operations

* Create new task
* View personal tasks
* Edit tasks (title, description, priority, status, due date)
* Delete tasks
* Search tasks by title
* Sort tasks by:

  * Due date
  * Priority
  * Status
* Filter tasks by:

  * Priority
  * Status
  * Due date
    
### Task Reminders & Notifications

When a user logs in, the system displays:

*  Tasks with **upcoming deadlines (within 24 hours)**
*  **Overdue tasks** 
---



---

## Data Storage

All data is stored using **CSV format** (text-based files):

* `users.txt` → User data
* `tasks.txt` → Task data

This approach ensures:

* Simple persistence
* No external libraries required
* Easy parsing and updates

---

##  Project Structure

```
├── main.py
├── Authentication.py
├── AdminPanel.py
├── TaskManagementSystem.py
├── CreateNewTask.py
├── ViewTasks.py
├── EditTask.py
├── DeleteTask.py
├── SearchTask.py
├── SortingTasks.py
├── FilterTasks.py
├── users.txt
└── tasks.txt
```

---

##  How to Run

1. Make sure Python 3 is installed
2. Run the application:

```bash
python main.py
```

3. Choose to **register** or **login**
4. Admins are redirected to the Admin Panel
5. Regular users are redirected to the Task Management Menu

---

## Technologies Used

* Python 3
* `hashlib`
* `re`
* `datetime`
* File handling (CSV format)

---

##  Notes

* Only **one admin** is allowed in the system
* Regular users must be activated by the admin before logging in
* Users can manage **only their own tasks**

---

## Future Improvements

* GUI version (Tkinter / PyQt)
* JSON-based storage
* Email notifications
* Task categories

---

## Author

**Nouran Mohammed**

---

⭐ If you like this project, feel free to star it on GitHub!
