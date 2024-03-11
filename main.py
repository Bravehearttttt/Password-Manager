from pathlib import Path

path = Path("passwords/passwords.log")
pwd = input("What is the master password")
# def view():
#     with open("password.txt","r") as file:


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    with open(path, "a") as file:
        file.write(f"{name}|{pwd} ")


while True:
    mode = input(
        "would you like to add new password or view existing ones(view,add or q to quit)?").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
