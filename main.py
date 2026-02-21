
while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    
    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"

            with open('files/subfiles/todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('files/subfiles/todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show':
            with open('files/subfiles/todos.txt', 'r') as file:
                todos = file.readlines()
            


            for index, item in enumerate(todos):
                item = item.strip("\n")
                print(f"{index + 1}-{item}".title())
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1

            with open('files/subfiles/todos.txt', 'r') as file:
                todos = file.readlines()
            print("Here is existing", todos)

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            print("Here is the added todo", todos)

            with open('files/subfiles/todos.txt', 'w') as file:
                todos = file.writelines(todos)
        
        case 'complete':
            number = int(input("Number of the todo to complete: "))

            with open('files/subfiles/todos.txt', 'r') as file:
                todos = file.readlines()
            
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            
            with open('files/subfiles/todos.txt', 'w') as file:
                todos = file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        case 'exit':
            break
        

print("Bye!")
