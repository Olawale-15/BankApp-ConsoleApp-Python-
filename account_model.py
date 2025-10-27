import user_model
import json
import os
class Account:
    def __init__(self):
        pass
    def deposit(self):
        if not os.path.exists(user_model.USER_FILE):
            print("Server not found")
        with open(user_model.USER_FILE, "r") as f:
            users = json.load(f)
        account_number = int(input("Enter your account number: "))
        # find user
        found_user = None
        for user in users:
            if user["account_number"] == account_number:
                found_user = user
                break

        if found_user is None:
            print("Account does not exist")
        else:
            amount = float(input("Enter amount: "))
            found_user["balance"] += amount
            with open(user_model.USER_FILE, "w") as f:
                json.dump(users, f, indent=4)
            print(f"You have successfully deposited #{amount}. New balance is #{found_user['balance']}")


    def withdraw(self):
        if not os.path.exists(user_model.USER_FILE):
            print("Server not found")
        with open(user_model.USER_FILE, "r") as f:
            users = json.load(f)

        id = int(input("Enter your id: "))

        # Find the user with this id
        found_user = None
        for user in users:
            if user["id"] == id:
                found_user = user
                break

        if found_user is None:
            print("You are not registered")
        else:
            amount = float(input("Enter amount: "))
            if amount > found_user["balance"]:
                print("Insufficient balance")
            else:
                found_user["balance"] -= amount
                with open(user_model.USER_FILE, "w") as d:
                    json.dump(users, d, indent=4)
                print(f"#{amount} was debi+ted f+rom your account. New balance is #{found_user['balance']}")


    def transfer(self):
        if not os.path.exists(user_model.USER_FILE):
            print("Server not found")
        
        with open(user_model.USER_FILE, "r") as f:
            users = json.load(f)
        recipient_account_number = input("Enter account number you want to transfer to: ")
        sender_id = int(input("Enter your ID: "))

        sender = None
        recipient = None

        # Find both sender and recipient
        for user in users:
            if user["id"] == sender_id:
                sender = user
            if str(user["account_number"]) == recipient_account_number:
                recipient = user

        if sender is None:
            print("You are not registered")
        elif recipient is None:
            print("Invalid Account Number")
        else:
            amount = float(input("Enter amount: "))
            if amount > sender["balance"]:
                print("Insufficient funds")
            else:
                sender["balance"] -= amount
                recipient["balance"] += amount
                with open(user_model.USER_FILE, "w") as f:
                    json.dump(users, f, indent=4)
                print(f"You have successfully transferred ₦{amount} to account {recipient['account_number']} ({recipient['full_name']})")
