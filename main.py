
while True:
    # Get user input and strip space chars from it
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    
    if user_action.startswith('add'):
            todo = user_action[4:]

            with open('files/subfiles/todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo + '\n')

            with open('files/subfiles/todos.txt', 'w') as file:
                file.writelines(todos)

    elif user_action.startswith('show'):
            with open('files/subfiles/todos.txt', 'r') as file:
                todos = file.readlines()
            


            for index, item in enumerate(todos):
                item = item.strip("\n")
                print(f"{index + 1}-{item}".title())
    elif user_action.startswith('edit'):
        try:
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
        except ValueError:
             print("Your command is not valid.")
             continue
        
    elif user_action.startswith('complete'):
        try:
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
        except IndexError:
            print("There is no item with that number")
            continue 
    elif user_action.startswith('exit'):
        break
    else:
         print("Comment is not valid")
    

print("Bye!")
