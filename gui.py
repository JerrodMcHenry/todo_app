import functions 
import FreeSimpleGUI 

layout = [
    [FreeSimpleGUI.Text("Enter a todo: ")],
    [FreeSimpleGUI.Input()],
    [FreeSimpleGUI.Button("Ok")]
]

window = FreeSimpleGUI.Window('My To-Do App', layout)
window.read()
window.close()