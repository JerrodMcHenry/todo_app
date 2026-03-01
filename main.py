
while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    
    if 'add' in user_action or 'new' in user_action:
            todo = user_action[4:]

            with open('files/subfiles/todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('files/subfiles/todos.txt', 'w') as file:
                file.writelines(todos)

    elif 'show' in user_action:
            with open('files/subfiles/todos.txt', 'r') as file:
                todos = file.readlines()
            


            for index, item in enumerate(todos):
                item = item.strip("\n")
                print(f"{index + 1}-{item}".title())
    elif 'edit' in user_action:
        number = int(user_action[5:])
        print(number)
        
        number = number - 1

        with open('files/subfiles/todos.txt', 'r') as file:
            todos = file.readlines()
        print("Here is existing", todos)

        new_todo = input("Enter new todo: ")
        todos[number] = new_todo + '\n'

        print("Here is the added todo", todos)

        with open('files/subfiles/todos.txt', 'w') as file:
            todos = file.writelines(todos)
    
    elif 'complete' in user_action:
        number = int(user_action[9:])

        with open('files/subfiles/todos.txt', 'r') as file:
            todos = file.readlines()
        
        index = number - 1
        todo_to_remove = todos[index].strip('\n')
        todos.pop(index)
        
        with open('files/subfiles/todos.txt', 'w') as file:
            todos = file.writelines(todos)

        message = f"Todo {todo_to_remove} was removed from the list."
        print(message)
    elif 'exit' in user_action:
        break
    else:
         print("Comment is not valid")
    

print("Bye!")
