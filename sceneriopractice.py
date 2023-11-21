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


class calculator:
    
    def add(self,num1,num2):
        num1=float(num1)
        num2=float(num2)

        print(f'the addition of {num1} and {num2} is  ',num1+num2)
    
    def subt(self,num1,num2):
        print(f'the subtracton of {num1} and {num2} is  ',num1-num2)
    
    def product(self,num1,num2):
        print(f'the product of {num1} and {num2} is  ',num1*num2)
    
    def division(self,num1,num2):
        num1=float(num1)
        num2=float(num2)
        try:
            print(f'the division of {num1} and {num2} is  ',num1/num2)
        
        except ZeroDivisionError as e:
            print(f' {num1} is not divisible by {num2}')



cal=calculator()

def main():

    while True:
        print('Welcome to the calculator    !!')
        print('Enter your Choice + - * /')
        print('Press q for exit  !')
        choice=input()

        if choice == '+':
            a=float(input('Enter 1st number'))
            b=float(input('Enter 2nd number'))
            cal.add(a,b)
        elif choice == '-':
            a=float(input('Enter 1st number'))
            b=float(input('Enter 2nd number'))
            cal.subt(a,b)
        elif choice == '*':
            a=float(input('Enter 1st number'))
            b=float(input('Enter 2nd number'))
            cal.product(a,b)
        elif choice == '/':
            a=float(input('Enter 1st number'))
            b=float(input('Enter 2nd number'))
            cal.division(a,b)
        elif choice == 'q':
            print('Thank you !')
            break
        else:
            print(f'You entered wrong choice {choice} , Try again ')
        

if __name__=="__main__":
    main()
