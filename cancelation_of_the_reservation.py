import json

with open('data.json') as data_file:
    data = json.load(data_file)

user_input_room_code = input("Please enter the room number you are trying to cancel: ")
while (not(user_input_room_code in data["rooms"].keys())):
    print ("Error 004: Room is not found, please try again!")
    user_input_room_code = input("Please enter the room number you are trying to cancel: ")

print("Room Code:",data["rooms"][user_input_room_code]["room_code"])
print("Room Status:",data["rooms"][user_input_room_code]["room_status"]["name"])
print("Room Location:",data["rooms"][user_input_room_code]["room_location"]["name"])
print("Room Capacity:",data["rooms"][user_input_room_code]["room_capacity"])
print("Room Occupied Seats:",data["rooms"][user_input_room_code]["room_occupied_seats"])

user_email = "aua@aua.am" #This is the user who is canceling the room reservation
cancelation = str(input("Do you want to cancel your reservation? (yes/no): "))

if (cancelation == "yes" and data["rooms"][user_input_room_code]["room_occupied_seats"]>=1):
    print("")
    print("You have cancelled the reservation.")
    print("Room Code:",data["rooms"][user_input_room_code]["room_code"])
    print("Room Status:",data["rooms"][user_input_room_code]["room_status"]["name"])
    print("Room Location:",data["rooms"][user_input_room_code]["room_location"]["name"])
    print("Room Capacity:",data["rooms"][user_input_room_code]["room_capacity"])
    data["rooms"][user_input_room_code]["room_occupied_seats"] = int(data["rooms"][user_input_room_code]["room_occupied_seats"] -1)
    data["rooms"][user_input_room_code]["room_booked_by"].remove(user_email)
    with open('data.json', 'w') as data_file:
        json.dump(data, data_file, indent=4)
    print(("Room Occupied Seats:"), data["rooms"][user_input_room_code]["room_occupied_seats"], "/", data["rooms"][user_input_room_code]["room_capacity"])

elif (cancelation == "yes" and data["rooms"][user_input_room_code]["room_occupied_seats"]<=0):
    print("There are no bookings in the room.")

elif (cancelation == "no"):
    print("")
    print("The reservation is kept")
    print("Room Code:",data["rooms"][user_input_room_code]["room_code"])
    print("Room Status:",data["rooms"][user_input_room_code]["room_status"]["name"])
    print("Room Location:",data["rooms"][user_input_room_code]["room_location"]["name"])
    print("Room Capacity:",data["rooms"][user_input_room_code]["room_capacity"])
    print("Room Occupied Seats:",data["rooms"][user_input_room_code]["room_occupied_seats"])    
else:
    print("")
    print("Error: Only lowercase yes or no are accepted.")
