import random
import json
import os
#File to store user info
USER_FILE = "user.json"

# Empty dictionary array for storing users
users = []
class User:
  def __init__(self,):
    pass
  def register_user(self):
    print("\n<>========<> Register <>========<>")
    if os.path.exists(USER_FILE):
      with open(USER_FILE, "r") as f:
        try:
          users = json.load(f)
        except json.JSONDecodeError:
          users = []
    else:
      users = []
    id = random.randint(1, 1000)
    first_name = input("Enter your FirstName: ")
    last_name = input("Enter Your LastName: ")
    email = input("Enter Your Email: ")
    phone_number = input("Enter Your Phone Number: ")
    password = input("Enter Your Password: ")
    account_number =  random.randint(1234453345, 4544783456 )
    balance = 0
    is_logged_in = False
    full_name = f"{first_name} {last_name}"
    user = {"id": id, "full_name": full_name, "email": email, "phone_number": phone_number, "password": password, "account_number": account_number, "balance": balance, "login_status": is_logged_in}
    for usr in users:
      if usr["email"] == email:
        print("Your already exist")
    users.append(user)
    with open(USER_FILE, "w") as f:
      json.dump(users, f, indent=4)
    print("Registration Successfull")
    print(f"Your account number is: {account_number}")



  def log_in(self):
    if not os.path.exists(USER_FILE):
      print("File not exist")
      return
    
    with open(USER_FILE, "r") as f:
      users = json.load(f)
    
    email = input("Enter Your Email: ")
    password = input("Enter Your Password: ")

    for user in users:
      if email == user["email"] or password == user["password"]:
        user["login_status"] = True
        print("Login SUccessful")

        with open(USER_FILE, "w")as f:
          json.dump(users, f, indent=4)
        return
    
    print("\nInvalid Email or Password ")
        

  def delete_user(self):
    print("<>========<> Delete User <>========<>")
    if not os.path.exists(USER_FILE):
      print("Server Not Found")
    
    with open(USER_FILE, "r") as f:
      users = json.load(f)

    id = int(input("Enter User Id: "))
    found_user = None
    for user in users:
      if user["id"] == id:
        found_user = user
        break
    if found_user == None:
      print("User not found")
    else:
      users.remove(found_user)
      with open(USER_FILE, "w") as f:
        json.dump(users, f, indent=4)
      print("User deleted successfully")

  def update_user(self):
    print("<>======== Update Details <>========")

    if not os.path.exists(USER_FILE):
        print("Server not found")
        return

    with open(USER_FILE, "r") as f:
        users = json.load(f)

    id = int(input("Enter User Id: "))
    found_user = None

    for user in users:
        if user["id"] == id:
            found_user = user
            break

    if found_user is None:
        print("User not found")
        return

    # Get new info
    full_name = input("Enter Your Name: ")
    email = input("Enter Your Email: ")
    phone_number = input("Enter Your Phone Number: ")

    # Update the found user
    found_user["full_name"] = full_name
    found_user["email"] = email
    found_user["phone_number"] = phone_number

    # Write the entire list of users back to file
    with open(USER_FILE, "w") as f:
        json.dump(users, f, indent=4)

    print("User Information Updated Successfully")

  
  def get_user_by_id(self):
    if not os.path.exists(USER_FILE):
      print("Server not exist")
      return None
    
    with open(USER_FILE, "r")as f:
      users = json.load(f)

    id = int(input("Enter User Id: "))
    found_user = None
    for user in users:
      if user["id"] == id:
        found_user = user
        break
    if found_user == None:
      print("User Not Found")
    else:
      print("====== User Details ======")
      user_details = f"Name:{user["full_name"]} \n Email:{user["email"]}, \n Phone Number: {user["phone_number"]} \n Account Number:{user["account_number"]} \n Balance: {user["balance"]}"
      print(user_details)

  def get_all_users(self):
    if not os.path.exists(USER_FILE):
      print("Server not available")
      return None
    
    with open(USER_FILE, "r") as f:
      users = json.load(f)
    for user in users:
       user_details = f"Name:{user["full_name"]} \n Email:{user["email"]}, \n Phone Number: {user["phone_number"]} \n Account Number:{user["account_number"]} \n Balance: {user["balance"]}"
       print(user_details)
       print("--------------------------------------")