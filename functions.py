FILE_PATH = "files/todos.txt"

def print_list(todo_list):
    # list_for_print = [item.strip('\n') for item in todo_list]
    for i, item in enumerate(todo_list):
        item = item.strip("\n")
        print(f"{i + 1} - {item}")
    print(f"You have {len(todo_list)} yet to do.")


def get_todos_from_file(filepath=FILE_PATH):
    with open(filepath, "r") as file:
        content = file.readlines()
    return content


def save_todos_to_files(todo_list, filepath=FILE_PATH):
    with open(filepath, "w") as file:
        file.writelines(todo_list)