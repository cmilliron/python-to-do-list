import functions
import PySimpleGUI as sg

# Elements for GUI
label = sg.Text("Type in a to-do:")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button('Add')

list_box = sg.Listbox(values=functions.get_todos_from_file(),
                      key="todo_list",
                      enable_events=True,
                      size=[45, 20])
edit_button = sg.Button('Edit')


exit_button = sg.Button('Exit')

window = sg.Window(title="My To-Do App",
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button],
                           [exit_button]],
                   font=("Helvetica", 20))
while True:
    event, input_value = window.read()
    print(event)
    print(input_value)
    match event:
        case "Add":
            todos = functions.get_todos_from_file()
            todos.append(input_value['todo'] + "\n")
            functions.save_todos_to_files(todos)
            window['todo_list'].update(values=todos)
        case "Edit":
            if len(input_value["todo_list"]) > 0:
                todo_to_edit = input_value["todo_list"][0]
                new_todo = input_value['todo'] + "\n"
                todos = functions.get_todos_from_file()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.save_todos_to_files(todos)
                window['todo_list'].update(values=todos)
            else:
                sg.Popup("You didn't pick anything to edit.")
                continue
        case "todo_list":
            window['todo'].update(value=input_value['todo_list'][0])
        case "Exit" | sg.WIN_CLOSED:
            break

window.close()

