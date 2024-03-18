user_prompt: str = "Type add, show, edit, delete, complete, or exit: "
# todos = ["Clean\n", "Cook\n", "Mow the lawn\n"]

def print_list(todo_list):
    # list_for_print = [item.strip('\n') for item in todo_list]
    for i, item in enumerate(todo_list):
        item = item.strip("\n")
        print(f"{i + 1} - {item}")
    print(f"You have {len(todo_list)} yet to do.")


def get_todos_from_file():
    with open("files/todos.txt", "r") as file:
        content = file.readlines()
    return content


def save_todos_to_files(todo_list):
    with open("files/todos.txt", "w") as file:
        file.writelines(todo_list)


def show_list():
    todos = get_todos_from_file()
    print_list(todos)
    return todos


while True:
    user_action = input(user_prompt).strip()
    if "add" in user_action[:3]:
        todos = get_todos_from_file()
        # todo = input("Enter a todo: ")
        todo = user_action[4:]
        todos.append(todo + "\n")
        save_todos_to_files(todos)
    elif 'show' in user_action[:4]:
        show_list()
    elif "exit" in user_action[:4]:
        break
    elif "edit" in user_action[:4]:
        todos = get_todos_from_file()
        # item_number = int(input("Number of the todo to edit: "))
        item_number = int(user_action[5:])
        item_index = item_number - 1

        item_to_edit = todos[item_index]
        print(f"Item to edit: {item_to_edit}")
        todos[item_index] = input("Enter edited todo: ") + "\n"
        save_todos_to_files(todos)
    elif "complete" in user_action[:8]:
        todos = get_todos_from_file()
        # item_number = int(input("What task have you completed: "))
        item_number = int(user_action[9:])
        item_index = item_number - 1
        completed_item = todos.pop(item_index).strip("\n")
        print(f'You completed {completed_item}. Remaining items:')
        print_list(todos)
        save_todos_to_files(todos)
    else:
        print("Hey, you entered an unknown command")

print("Bye!")



