import functions
import PySimpleGUI as sg
import time

sg.theme('DarkPurple4')

# Elements for GUI
date_label = sg.Text('', key='clock')
label = sg.Text("Type in a to-do:")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
# add_button = sg.Button('Add')
add_button = sg.Button(size=3,
                       tooltip='Add todo',
                       image_source="assets/add.png",
                       mouseover_colors="green")


list_box = sg.Listbox(values=functions.get_todos_from_file(),
                      key="todo_list",
                      enable_events=True,
                      size=[45, 20])
edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete')


exit_button = sg.Button('Exit')

window = sg.Window(title="My To-Do App",
                   layout=[[date_label],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Helvetica", 20))
while True:
    event, input_value = window.read(timeout=1000)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    # print(event)
    # print(input_value)

    match event:
        case "Add":
            todos = functions.get_todos_from_file()
            todos.append(input_value['todo'] + "\n")
            functions.save_todos_to_files(todos)
            window['todo_list'].update(values=todos)
            window['todo'].update('')
        case "Edit":
            try:
                todo_to_edit = input_value["todo_list"][0]
                new_todo = input_value['todo'] + "\n"
                todos = functions.get_todos_from_file()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.save_todos_to_files(todos)
                window['todo_list'].update(values=todos)
                window['todo'].update('')
            except IndexError:
                sg.Popup("You didn't a todo to complete.", font=("Helvetica", 20))
                continue
        case "todo_list":
            window['todo'].update(value=input_value['todo_list'][0])
        case "Complete":
            try:
                todo_to_complete = input_value["todo_list"][0]
                todos = functions.get_todos_from_file()
                todos.remove(todo_to_complete)
                functions.save_todos_to_files(todos)
                window['todo_list'].update(values=todos)
                window['todo'].update('')
            except IndexError:
                sg.Popup("You didn't a todo to complete.", font=("Helvetica", 20))
                continue
        case "Exit" | sg.WIN_CLOSED:
            break


window.close()

