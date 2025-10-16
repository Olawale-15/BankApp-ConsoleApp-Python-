import account_model
import user_model

def main_menu():
  while True:
    print("<=====> Welcome To Bank App <=====>")
    print("1. Register")
    print("2. Login")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Transfer")
    print("6. Details")
    print("7. Check Balance")
    print("8. Exist")

    choice = input("Enter your choice: ")
    if choice == "1":
      user_model.register_user()
    elif choice == "2":
      user_model.log_in()
    elif choice == "3":
      account_model.deposit()
    elif choice == "4":
      account_model.withdraw()
    elif choice == "5":
      account_model.transfer()
    elif choice == "6":
      user_model.user_details()
    elif choice == "7":
      id =  int(input("Enter your id"))
      found_user = None
      for user in user_model.users:
        if user["id"] == id:
          found_user = user
          break
      if found_user:
        print(f"Your balance is #{found_user['balance']}")
      else:
        print("User not found")
    elif choice == "8":
      print("Thanks For Using Our BankApp!")
    else:
      print("Invalid Choice")

main_menu()
