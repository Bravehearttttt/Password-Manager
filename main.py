from pathlib import Path
from cryptography.fernet import Fernet
path = Path("passwords/passwords.log")


def view():
    with open(path, "r") as file:
        for line in file.readlines():
            data = line.rsplit()
            user, passw = line.split("|")
            print(f"UserName:= {user} , Password:= {passw}")


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    with open(path, "a") as file:
        file.write(f"{name}|{pwd} \n")


while True:
    mode = input(
        "would you like to add new password or view existing ones(view,add or q to quit)?").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
