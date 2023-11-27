class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "complete": False})
        print(f'Task "{task}" added successfully.')

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            deleted_task = self.tasks.pop(task_index)
            print(f'Task "{deleted_task["task"]}" deleted successfully.')
        else:
            print('Invalid task index. Please try again.')

    def display_tasks(self):
        if not self.tasks:
            print('No tasks found.')
        else:
            print("To-Do List:")
            for index, task in enumerate(self.tasks):
                status = "Done" if task["complete"] else "Not Done"
                print(f'{index + 1}. {task["task"]} - {status}')

    def mark_as_complete(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["complete"] = True
            print(f'Task "{self.tasks[task_index]["task"]}" marked as complete.')
        else:
            print('Invalid task index. Please try again.')


def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Display Tasks")
        print("4. Mark Task as Complete")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.display_tasks()
            task_index = int(input("Enter the task index to delete: ")) - 1
            todo_list.delete_task(task_index)
        elif choice == "3":
            todo_list.display_tasks()
        elif choice == "4":
            todo_list.display_tasks()
            task_index = int(input("Enter the task index to mark as complete: ")) - 1
            todo_list.mark_as_complete(task_index)
        elif choice == "5":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
