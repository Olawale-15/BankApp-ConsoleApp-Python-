import random
users = []

def register_user():
  print("\n<======> Register <======>")
  id = random.randint(1, 100)
  first_name = input("Enter Your FirstName: ")
  last_name = input("Enter Your LastName: ")
  email = input("Enter Your Email :")
  phone_number = input("Enter Your PhoneNumber: ")
  password = input("Enter Your Password: ")
  full_name = f"{first_name} {last_name}"
  account_number = random.randint(1234453345, 4544783456 )
  balance = 0
  user = {"id": id, 'full_name': full_name, 'email': email, "phone_number": phone_number, "password": password, "account_number": account_number, "balance": balance}
  users.append(user)
  print(f"Your account number is {account_number}")
  print("Registration Successfull")


def log_in():
  print("\n<======> Login <======>")
  email = input("Enter You Email")
  password = input("Enter You Password")
  for user in users:
      if email != user["email"] or password != user["password"]:
        print("Invalid email or password")
      else:
        print("Login successful")
      


def user_details():
  for user in users:
    print(user)

  
