new_member = input("Add a new member: ")

file = open('members.txt', "a")

file.write(new_member + "\n")