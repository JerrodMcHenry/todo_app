import FreeSimpleGUI as sg

layout_1 = [
    [sg.Text("Select files to compress: ")],
    [sg.Input()],
    [sg.FilesBrowse("Choose")],
    [sg.Text("Select destination folder: ")],
    [sg.Input()],
    [sg.FolderBrowse("Choose")],
    [sg.Button("Compress")]
    
]


window = sg.Window("File Compressor", layout_1)
window.read()
window.close()