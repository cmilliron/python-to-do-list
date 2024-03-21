from functions import print_list, \
    get_todos_from_file, \
    save_todos_to_files
import time

user_prompt: str = "Type add, show, edit, delete, complete, or exit: "
# todos = ["Clean\n", "Cook\n", "Mow the lawn\n"]
now = time.strftime("%B %d, %Y %H:%M:%S")

def show_list():
    todos_list = get_todos_from_file()
    print_list(todos_list)
    return todos_list


if __name__ == "__main__":
    print(f"It is {now}.")
    while True:
        user_action = input(user_prompt).strip()
        if user_action.startswith("add"):
            todos = get_todos_from_file()
            # to do = input("Enter a to do: ")
            todo = user_action[4:]
            todos.append(todo + "\n")
            save_todos_to_files(todos)
        elif user_action.startswith('show'):
            show_list()
        elif user_action.startswith('exit'):
            break
        elif user_action.startswith('edit'):
            try:
                todos = get_todos_from_file()
                # item_number = int(input("Number of the to do to edit: "))
                item_number = int(user_action[5:])
                item_index = item_number - 1

                item_to_edit = todos[item_index]
                print(f"Item to edit: {item_to_edit}")
                todos[item_index] = input("Enter edited todo: ") + "\n"
                save_todos_to_files(todos)
            except ValueError:
                print('You must enter a item number.')
                continue
            except IndexError:
                print("You must enter a valid number.")
                continue
        elif user_action.startswith('complete'):
            try:
                todos = get_todos_from_file()
                # item_number = int(input("What task have you completed: "))
                item_number = int(user_action[9:])
                item_index = item_number - 1
                completed_item = todos.pop(item_index).strip("\n")
                print(f'You completed {completed_item}. Remaining items:')
                print_list(todos)
                save_todos_to_files(todos)
            except ValueError:
                print('You must enter a item number.')
                continue
            except IndexError:
                print("You must enter a valid number.")
                continue
        else:
            print("Hey, you entered an unknown command")

    print("Bye!")



