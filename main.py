user_prompt: str = "Type add, show, edit, or exit: "
todos = ["Clean", "Cook", "Mow the lawn"]

while True:
    user_action = input(user_prompt)
    match user_action.strip().lower():
        case "add":
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' | "display":
            for i, item in enumerate(todos):
                print(f"{i + 1} - {item}")
        case "exit":
            break
        case "edit":
            item_number = int(input("Number of the todo to edit: "))
            item_index = item_number - 1
            item_to_edit = todos[item_index]
            print(f"Item to edit: {item_to_edit}")
            todos[item_index] = input("Enter edited todo: ")
        case _:
            print("Hey, you entered an unknown command")

print("Bye!")



