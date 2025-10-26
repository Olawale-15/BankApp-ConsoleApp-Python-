import account_model
import user_model
import house
account = account_model.Account()
usr = user_model.User()
apartment = house.Apartment()

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
    print("8. Add Apartment")
    print("9. Rent Apartment")
    print("10. View Available Apartment")
    print("11. View Rented Apartment")
    print("12. View All Apartment")
    print("13. Find By Price")
    print("14. Get User By Id")
    print("15. Get All Users")
    print("16. Update Profile")
    print("17. Delete Profile")
    print("18. Exist")

    choice = input("Enter your choice: ")
    if choice == "1":
      usr.register_user()
    elif choice == "2":
      usr.log_in()
    elif choice == "3":
      account.deposit()
    elif choice == "4":
      account.withdraw()
    elif choice == "5":
      account.transfer()
    elif choice == "6":
      usr.get_all_users()
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
      apartment.add_house()
    elif choice == "9":
      apartment.rent_apartment()
    elif choice == "10":
      apartment.available_apartment()
    elif choice == "11":
      apartment.rented_apartment()
    elif choice == "12":
      apartment.view_all_apartment()
    elif choice == "13":
      apartment.find_house_by_price() 
    elif choice == "14":
      usr.get_user_by_id()
    elif choice == "15":
      usr.get_all_users()
    elif choice == "16":
      usr.update_user()
    elif choice == "17":
      usr.delete_user()
    elif choice == "18":
      print("Thanks For Using Our BankApp!")
    else:
      print("Invalid Choice")

main_menu()
