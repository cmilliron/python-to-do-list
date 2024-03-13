password = input("Enter password: ")

while password != "pass123":
    print("We could not log you in")
    password = input("Enter password: ")

print("Logged In.")