import json
import pprint

with open("questions.json") as file:
    contents = file.read()

data = json.loads(contents)

answers_right = 0

for question in data:
    print(question["question"])
    for index, alternative in enumerate(question["alternatives"]):
        print(f"{index + 1} - {alternative}")
    answer = int(input("Enter your answer (in numbers please): "))
    question['user_choice'] = answer

print("Let's grade your answers.")
for question in data:
    print(question["question"])
    if question['user_choice'] == question["correct_answer"]:
        print("You are a smart one.")
        answers_right += 1
    else:
        print("Man! You're a dumbass.")
        print(f"Your answer: {question['user_choice']} == {question['correct_answer']}")


print(f"You got {answers_right} out of {len(data)}")
