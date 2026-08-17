"""
PROJECT 1: THE TO-DO LIST
DecodeLabs - Junior Python Developer (Batch 2026)
"""
# ============================================================
# DATA LAYER: In-Memory Database
# ============================================================

class ToDoList:
    def __init__(self):
        # Store multiple items in a single variable
        self.tasks = []
    
    def add_task(self, task):
        # Append operation - adding to the list
        if task and task.strip():
            self.tasks.append(task.strip())
            print(f" Task added: {task}")
        else:
            print(" Task cannot be empty!")
    
    def view_tasks(self):
        # Print loop - displaying all tasks
        if not self.tasks:
            print("\n No tasks found!")
            return
        
        print("\n" + "="*50)
        print("📋 YOUR TO-DO LIST")
        print("="*50)
        
        # enumerate() - professional indexing
        for index, task in enumerate(self.tasks, start=1):
            print(f"  {index}. {task}")
        print("="*50)

# ============================================================
# UI LAYER: User Interface
# ============================================================

class ToDoApp:
    def __init__(self):
        self.todo = ToDoList()
    
    def display_menu(self):
        print("\n" + "="*40)
        print(" TO-DO LIST MANAGER")
        print("="*40)
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Exit")
        print("="*40)
    
    def run(self):
        print("\n WELCOME TO DECODELABS TO-DO LIST\n")
        
        while True:
            self.display_menu()
            
            # INPUT: Get user choice
            choice = input("\nEnter your choice (1-3): ")
            
            # PROCESS: Handle the choice
            if choice == '1':
                # INPUT: Get task
                task = input("Enter task: ")
                # PROCESS: Add to list
                self.todo.add_task(task)
                
            elif choice == '2':
                # OUTPUT: Display tasks
                self.todo.view_tasks()
                
            elif choice == '3':
                # OUTPUT: Exit
                print("\n Thank you for using DecodeLabs To-Do List!")
                break
                
            else:
                print(" Invalid choice! Please enter 1, 2, or 3.")

# ============================================================
# MAIN ENTRY POINT
# ============================================================

def main():
    app = ToDoApp()
    app.run()

if __name__ == "__main__":
    main()