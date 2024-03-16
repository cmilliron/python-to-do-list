user_prompt: str = "Type add, show, edit, delete, complete, or exit: "
# todos = ["Clean\n", "Cook\n", "Mow the lawn\n"]

def print_list(todo_list):
    for i, item in enumerate(todo_list):
        item = item.strip("\n")
        print(f"{i + 1} - {item}")
    print(f"You have {len(todo_list)} yet to do.")


def get_todos_from_file():
    file = open("files/todos.txt", "r")
    content = file.readlines()
    file.close()
    return content


def save_todos_to_files(todo_list):
    file = open("files/todos.txt", "w")
    file.writelines(todo_list)
    file.close()


def show_list():
    todos = get_todos_from_file()
    print_list(todos)
    return todos


while True:
    user_action = input(user_prompt)
    match user_action.strip().lower():
        case "add":
            todos = get_todos_from_file()
            todo = input("Enter a todo: ")
            todos.append(todo + "\n")
            save_todos_to_files(todos)
        case 'show' | "display":
            show_list()
        case "exit":
            break
        case "edit":
            todos = show_list()
            item_number = int(input("Number of the todo to edit: "))
            item_index = item_number - 1
            item_to_edit = todos[item_index]
            print(f"Item to edit: {item_to_edit}")
            todos[item_index] = input("Enter edited todo: ") + "\n"
            save_todos_to_files(todos)
        case "complete":
            todos = show_list()
            item_number = int(input("What task have you completed: "))
            item_index = item_number - 1
            completed_item = todos.pop(item_index).strip("\n")
            print(f'You completed {completed_item}. Remaining items:')
            print_list(todos)
            save_todos_to_files(todos)
        case _:
            print("Hey, you entered an unknown command")

print("Bye!")



