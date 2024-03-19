user_prompt: str = "Type add, show, edit, delete, complete, or exit: "
# todos = ["Clean\n", "Cook\n", "Mow the lawn\n"]
FILE_PATH = "files/todos.txt"


def print_list(todo_list):
    # list_for_print = [item.strip('\n') for item in todo_list]
    for i, item in enumerate(todo_list):
        item = item.strip("\n")
        print(f"{i + 1} - {item}")
    print(f"You have {len(todo_list)} yet to do.")


def get_todos_from_file(filepath):
    with open(filepath, "r") as file:
        content = file.readlines()
    return content


def save_todos_to_files(filepath, todo_list):
    with open(filepath, "w") as file:
        file.writelines(todo_list)


def show_list(filepath):
    todos_list = get_todos_from_file(filepath)
    print_list(todos_list)
    return todos_list


while True:
    user_action = input(user_prompt).strip()
    if user_action.startswith("add"):
        todos = get_todos_from_file(FILE_PATH)
        # todo = input("Enter a todo: ")
        todo = user_action[4:]
        todos.append(todo + "\n")
        save_todos_to_files(FILE_PATH, todos)
    elif user_action.startswith('show'):
        show_list(FILE_PATH)
    elif user_action.startswith('exit'):
        break
    elif user_action.startswith('edit'):
        try:
            todos = get_todos_from_file(FILE_PATH)
            # item_number = int(input("Number of the todo to edit: "))
            item_number = int(user_action[5:])
            item_index = item_number - 1

            item_to_edit = todos[item_index]
            print(f"Item to edit: {item_to_edit}")
            todos[item_index] = input("Enter edited todo: ") + "\n"
            save_todos_to_files(FILE_PATH, todos)
        except ValueError:
            print('You must enter a item number.')
            continue
        except IndexError:
            print("You must enter a valid number.")
            continue
    elif user_action.startswith('complete'):
        try:
            todos = get_todos_from_file(FILE_PATH)
            # item_number = int(input("What task have you completed: "))
            item_number = int(user_action[9:])
            item_index = item_number - 1
            completed_item = todos.pop(item_index).strip("\n")
            print(f'You completed {completed_item}. Remaining items:')
            print_list(todos)
            save_todos_to_files(FILE_PATH, todos)
        except ValueError:
            print('You must enter a item number.')
            continue
        except IndexError:
            print("You must enter a valid number.")
            continue
    else:
        print("Hey, you entered an unknown command")


print("Bye!")



