class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        if self.tasks:
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("No tasks in the to-do list.")

    def mark_task_completed(self, index):
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1] += " - Completed"
            print("Task marked as completed.")
        else:
            print("Invalid task index.")

    def delete_task(self, index):
        if 1 <= index <= len(self.tasks):
            del self.tasks[index - 1]
            print("Task deleted successfully.")
        else:
            print("Invalid task index.")

def main():
    todo_list = TodoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
            print("Task added successfully!")

        elif choice == "2":
            print("\nTasks:")
            todo_list.view_tasks()

        elif choice == "3":
            index = int(input("Enter the task number to mark as completed: "))
            todo_list.mark_task_completed(index)

        elif choice == "4":
            index = int(input("Enter the task number to delete: "))
            todo_list.delete_task(index)

        elif choice == "5":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
