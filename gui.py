import functions 
import FreeSimpleGUI 
import time
FreeSimpleGUI.theme("NeonGreen1")

clock = FreeSimpleGUI.Text("", key="clock")
label = FreeSimpleGUI.Text("Enter a todo: ")
input_box = FreeSimpleGUI.Input(key="todo")
add_button = FreeSimpleGUI.Button("Add")
list_box = FreeSimpleGUI.Listbox(values=functions.get_todos(), key="todos", 
                                 enable_events=True, size=[45, 10])
edit_button = FreeSimpleGUI.Button("Edit")
complete_button = FreeSimpleGUI.Button("Complete")
exit_button = FreeSimpleGUI.Button("Exit")


window = FreeSimpleGUI.Window('My To-Do App', 
                              layout=[[clock],
                                      [label], 
                                      [input_box, add_button], 
                                      [list_box, edit_button, complete_button],
                                      [exit_button]], 
                              font=('Helvetica', 20))
while True:
    event, values = window.read(timeout=10)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                FreeSimpleGUI.popup("Please select an item first.", font=("Helvetica", 20))

        case "Complete":
            try:

                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                FreeSimpleGUI.popup("Please select an item first.", font=("Helvetica", 20))

        case "Exit":
            break
        case 'todos':
            window['todo'].update(values['todos'][0])

        case FreeSimpleGUI.WIN_CLOSED:
            break
window.close()