user_prompt: str = "Type add, show, edit, delete, complete, or exit: "
todos = ["Clean", "Cook", "Mow the lawn"]

def print_list():
    for i, item in enumerate(todos):
        print(f"{i + 1} - {item}")
    print(f"You have {len(todos)} yet to do.")


while True:
    user_action = input(user_prompt)
    match user_action.strip().lower():
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' | "display":
            print_list()
        case "exit":
            break
        case "edit":
            item_number = int(input("Number of the todo to edit: "))
            item_index = item_number - 1
            item_to_edit = todos[item_index]
            print(f"Item to edit: {item_to_edit}")
            todos[item_index] = input("Enter edited todo: ")
        case "complete":
            item_number = int(input("What task have you completed: "))
            item_index = item_number - 1
            completed_item = todos.pop(item_index)
            print(f'You completed {completed_item}. Remaining items:')
            print_list()
        case _:
            print("Hey, you entered an unknown command")

print("Bye!")



