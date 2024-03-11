user_prompt: str = "Enter a todo: "
todo1: str = input(user_prompt)
todo2: str = input(user_prompt)
todo3: str = input(user_prompt)

todos = [todo1, todo2, todo3]
print(f'Your task is "{todos}"')
print(type(todos))
