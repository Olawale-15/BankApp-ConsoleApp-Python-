import random
import user_model
# Empty dictionary array for storing apartments
apartments = []
class Apartment:
  def __init__(self):
    pass

  def add_house():
    apartment_name = input("Enter your apartment: ")
    number_of_rooms = int(input("Enter Room Numbers: "))
    price = float(input("Enter price: "))
    id = random.randint(200, 1000)
    status = "available"
    apartment = {
        "apartment_name": apartment_name, "number_of_rooms": number_of_rooms, "price": price, "house_id": id, "status": status
   }

    apartments.append(apartment)
    print("Apartment added successfuly")

  def available_apartment():
     for available_apartments in apartments:
        if available_apartments["status"] == "available":
           print(available_apartments)
        else:
            print("No available apartment")


  def rent_apartment():
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
         #  Find the user with this id
         found_users = None
     for user in user_model.users:
         if user["login_status"] == True:
           found_users = user
           break
     if found_users == None:
         print("Login bfore you proceed")
         return
    
     if apartment["price"] > found_users["balance"]:
         print("insuficient balance")
    
     elif apartment["status"] == "rented":
         print("Apartment is rented")
     else:
        apartment["status"] = "rented"
        user["balance"] -= apartment["price"]
        print("Apartment rented successfully")    
    

  def rented_apartment():
     for rented_apartments in apartments:
         if rented_apartments["status"] == "rented":
             rented_apartments_details = f"Apartment Name: {rented_apartments["apartment_name"]} \n Price: {rented_apartments["price"] } \n Status: {rented_apartments["status"]}"
             print("<>========<> Rented Apartment <>========<>")
             print(rented_apartments_details)
             print("---------------------------------")

  def find_house_by_price():
     price = float(input("Enter price"))
     for house_price in apartments:
         if house_price["price"] == price:
             print(house_price)

  def view_all_apartment():
     for apartment in apartments:
         print(apartment)

  def delete_apartment():
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
    
  def update_apartment():
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