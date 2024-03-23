import functions
import PySimpleGUI as sg

# Elements for GUI
label = sg.Text("Type in a to-do:")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button('Add')

exit_button = sg.Button('Exit')

window = sg.Window(title="My To-Do App",
                   layout=[[label],
                           [input_box, add_button],
                           [exit_button]],
                   font=("Helvetica", 20))
while True:
    event, input_value = window.read()
    match event:
        case "Add":
            todos = functions.get_todos_from_file()
            todos.append(input_value['todo'] + "\n")
            functions.save_todos_to_files(todos)
        case "Exit" | sg.WIN_CLOSED:
            break


window.close()

