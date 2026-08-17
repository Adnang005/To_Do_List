# To_Do_List

##  Project Overview

This project is a simple **command-line To-Do List application** developed in Python as part of the **DecodeLabs Junior Python Developer (Batch 2026)** program.

The main purpose of this project was to practice basic Python programming and Object-Oriented Programming concepts by building a small functional application.

##  What I Implemented

In this project, I implemented the following features:

### 1. Add Task

I created a feature that allows the user to enter and add a new task.

* Empty tasks are not allowed.
* Extra spaces are removed using `strip()`.
* Tasks are stored in a Python list.

### 2. View Tasks

I implemented a feature to display all saved tasks.

* Tasks are displayed with numbers.
* `enumerate()` is used for task indexing.
* If there are no tasks, the program displays a message.

### 3. Menu System

I created a simple menu where the user can choose:

```text
1. Add Task
2. View Tasks
3. Exit
```

The user's choice is processed using `if`, `elif`, and `else`.

### 4. Input Validation

I added basic validation for:

* Empty tasks
* Invalid menu choices

This makes the application more user-friendly.

### 5. Exit Functionality

I added an exit option that stops the program using `break` when the user selects option `3`.

---

##  Python Features Used

The project helped me practice:

* **Classes & Objects** — Created `ToDoList` and `ToDoApp` classes.
* **Lists** — Used a list to store tasks.
* **Methods** — Created methods such as `add_task()`, `view_tasks()`, and `run()`.
* **Loops** — Used `while` to keep the application running.
* **Conditional Statements** — Used `if`, `elif`, and `else` to handle choices.
* **User Input** — Used `input()` to interact with the user.
* **Output** — Used `print()` to display information.
* **`enumerate()`** — Used to number tasks.
* **`strip()`** — Used to remove unnecessary spaces.
* **Object-Oriented Programming** — Separated the data layer and UI layer.

##  Code Organization

The project is divided into:

```text
ToDoList
   ↓
Stores and manages tasks

ToDoApp
   ↓
Handles user interaction and menu

main()
   ↓
Starts the application
```

This separation makes the code easier to understand and maintain.

##  Current Limitation

The tasks are stored only in memory using a Python list. Therefore, tasks are lost when the program is closed.

##  Future Improvements

Possible improvements include:

* Delete tasks
* Edit tasks
* Mark tasks as completed
* Save tasks to a file
* Add task priorities and due dates

 Learning Outcome

Through this project, I practiced **Python fundamentals, Object-Oriented Programming, user input handling, lists, loops, conditional statements, and basic application structure**.

