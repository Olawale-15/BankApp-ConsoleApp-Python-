import random
import user_model
import json
import os

APARTMENT_FILE = "apartment.json"
# Empty dictionary array for storing apartments
apartments = []
class Apartment:
  def __init__(self):
    pass

  def add_house(self):
    print("<>==========<> Add Apartment <>==========<>")
    if os.path.exists(APARTMENT_FILE):
      with open(APARTMENT_FILE, "r") as f:
            try:
               apartments = json.load(f)
            except json.JSONDecodeError:
               apartments = []
    else:
      apartments = []
    
    apartment_name = input("Enter your apartment: ")
    number_of_rooms = int(input("Enter Room Numbers: "))
    price = float(input("Enter price: "))
    id = random.randint(200, 1000)
    status = "available"
    apartment = {
        "apartment_name": apartment_name, "number_of_rooms": number_of_rooms, "price": price, "house_id": id, "status": status
   }

    apartments.append(apartment)
    with open(APARTMENT_FILE, "w") as f:
       json.dump(apartments, f, indent=4)
    print("Apartment added successfuly")

  def available_apartment():
     for available_apartments in apartments:
        if available_apartments["status"] == "available":
           print(available_apartments)
        else:
            print("No available apartment")


  def rent_apartment(self):
     print("<>==========<> Rent Apartment <>==========<>")
     if not os.path.exists(APARTMENT_FILE):
        print("Server not available")
      
     with open(APARTMENT_FILE, "r") as f:
        apartments = json.load(f)
     #  Find the user with this id
     house_id = int(input("Enter House Id: "))
     found_apartment = None
     for apartment in apartments:
       if apartment["house_id"] == house_id:
             found_apartment = apartment
             break
     if found_apartment == None:
        print("House not found")    
     else:
         if not os.path.exists(user_model.USER_FILE):
            print("Server not found")
         
         with open(user_model.USER_FILE, "r") as a:
            users = json.load(a)
         #  Find the user with this id
         found_users = None
     for user in users:
         if user["login_status"] == True:
           found_users = user
           break
     if found_users == None:
         print("Login bfore you proceed")
         return
    
     if found_apartment["price"] > found_users["balance"]:
         print("insuficient balance")
    
     elif found_apartment["status"] == "rented":
         print("Apartment is rented")
     else:
        found_apartment["status"] = "rented"
        found_users["balance"] -= found_apartment["price"]
        with open(APARTMENT_FILE, "w") as f:
           json.dump(apartments, f, indent=4)
        with open(user_model.USER_FILE, "w") as d:
           json.dump(users, d, indent=4)
        print("Apartment rented successfully")    
    

  def rented_apartment(self):
     print("<>==========<> Available Apartment <>==========<>")
     if not os.path.exists(APARTMENT_FILE):
        print("Server not found")
      
     with open(APARTMENT_FILE, "r") as f:
        apartments = json.load(f)
     for rented_apartments in apartments:
         if rented_apartments["status"] == "rented":
             rented_apartments_details = f"Apartment Name: {rented_apartments["apartment_name"]} \n Price: {rented_apartments["price"] } \n Status: {rented_apartments["status"]}"
             print("<>========<> Rented Apartment <>========<>")
             print(rented_apartments_details)
             print("---------------------------------")

  def find_house_by_price(self):
     print("<>==========<> Search By Price <>==========<>")
     if not os.path.exists(APARTMENT_FILE):
        print("Server not found")
      
     with open(APARTMENT_FILE, "r") as f:
        apartments = json.load(f)
     price = float(input("Enter price"))
     for house_price in apartments:
         if house_price["price"] == price:
             print(house_price)

  def view_all_apartment(self):
     if os.path.exists(APARTMENT_FILE):
         print("Server not found")
      
     with open(APARTMENT_FILE, "r") as f:
        apartments = json.load(f)
        
     for apartment in apartments:
         print(apartment)

  def delete_apartment(self):
     id = int(input("Enter Apartment Id: "))
     found_apartment = None
     for apartment in apartments:
        if apartment["house_id"] == id:
           found_apartment = apartment
           break
     if found_apartment == None:
        print("Apartment Not Found")
     else:
        apartments.remove(apartment)
        print("Apartment Deleted Successfully")
    
  def update_apartment(self):
     id = int(input("Enter Your Id: "))
     found_apartment = None
     for apartment in apartments:
        if apartment["house_id"] == id:
           found_apartment = apartment
           break
     if found_apartment == None:
        print("Apartment Not Found")
     else:
        apartment_name = input("Enter Apartment Name: ")
        number_of_rooms = int(input("Enter Number Of Rooms: "))
        price = float(input("Enter Price: "))
        apartment["apartment_name"] = apartment_name 
        apartment["number_of_rooms"] = number_of_rooms
        apartment["price"] = price 
        print("Apartment Updated Successfully")