class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        # Implement the logic to add a task to the todo list
        self.tasks.append(task)
        print('Task successfully added!')

    def view_tasks(self):
        if len(self.tasks) == 0:
            print('Task list is empty. Please add tasks.')
        else:
            for i, task in enumerate(self.tasks, 0):
                print(f"{i}. {task}")

    def mark_as_completed(self, task_index):
        try:
            if len(self.tasks) == 0:
                print('Task list is empty. Please add tasks.')
            else:
                completed_task = self.tasks.pop(task_index)
                print(f'Task "{completed_task}" marked as completed.')
                self.view_tasks()
        except IndexError as e:
            print("Invalid index. Please choose an index from the list.")

def main():
    todo_list = TodoList()

    while True:
        print("\nTodo List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            task_description = input("Enter the task description: ")
            todo_list.add_task(task_description)

        elif choice == '2':
            todo_list.view_tasks()

        elif choice == '3':
            task_index = int(input("Enter the index of the task to mark as completed: "))
            todo_list.mark_as_completed(task_index)

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
