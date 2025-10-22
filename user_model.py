import random
# Empty dictionary array for storing users
users = []
class User:
  def __init__(self,):
    pass
  def register_user(self):
    print("\n<>========<> Register <>========<>")
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
      if usr["email"] == self.email:
        print("Your already exist")
    users.append(user)
    print("Registration Successfull")
    print(f"Your account number is: {account_number}")



  def log_in():
    print("\n<>========<> Login <>========<>")
    email = input("Enter You Email")
    password = input("Enter You Password")
    for user in users:
        if email != user["email"] or password != user["password"]:
          print("Invalid email or password")
        else:
          print("Login successful")
          user["login_status"] = True
        


  def delete_user():
    print("<>========<> Delete User <>========<>")
    id = int(input("Enter User Id: "))
    found_user = None
    for user in users:
      if user["id"] == id:
        found_user = user
        break
    if found_user == None:
      print("User not found")
    else:
      users.remove(user)
      print("User deleted successfully")

  def update_user():
    print("<>======== Update Details <>========")
    id = int(input("Enter User Id: "))
    found_user = None
    for user in users:
      if user["id"] == id:
        found_user = user
        break
    if found_user == None:
      print("User not found")
    else:
      first_name = input("Enter Your FirstName: ")
      last_name = input("Enter Your LastName: ")
      email = input("Enter Your Email: ")
      phone_number = input("Enter Your PhoneNumber: ")
      user["first_name"] = first_name
      user["last_name"] = last_name
      user["email"] = email
      user["phone_number"] = phone_number
      print("User Information Updated Successfully")
  
  def get_user_by_id():
    id = int(input("Enter User Id: "))
    found_user = None
    for user in users:
      if["id"] == id:
        found_user = user
        break
    if found_user == None:
      print("User Not Found")
    else:
      print("====== User Details ======")
      user_details = f"Name:{user["full_name"]} \n Email:{user["email"]}, \n Phone Number: {user["phone_number"]} \n Account Number:{user["account_number"]} \n Balance: {user["balance"]}"
      print(user_details)

  def get_all_users():
    for user in users:
       user_details = f"Name:{user["full_name"]} \n Email:{user["email"]}, \n Phone Number: {user["phone_number"]} \n Account Number:{user["account_number"]} \n Balance: {user["balance"]}"
       print(user_details)
       print("--------------------------------------")


