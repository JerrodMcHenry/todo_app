
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
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            todos.pop(number - 1)
            
        case 'exit':
            break
        

print("Bye!")
