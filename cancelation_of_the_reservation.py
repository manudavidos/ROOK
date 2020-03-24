room_data = {
  "room_code" : "003M",
  "room_status" : "Booked",
  "room_location" : "Main Building",
  "room_capacity" : 10,
  "room_occupied_seats" : 1
}
print("Room Code:",room_data["room_code"])
print("Room Status:",room_data["room_status"])
print("Room Location:",room_data["room_location"])
print("Room Capacity:",room_data["room_capacity"])
print("Room Occupied Seats:",room_data["room_occupied_seats"])

cancelation = str(input("Do you want to cancel your reservation? (yes/no): "))

if (cancelation == "yes"):
    print("==========")
    print("You have cencelled the reservation.")
    print("Room Code:",room_data["room_code"])
    print("Room Status:",room_data["room_status"])
    print("Room Location:",room_data["room_location"])
    print("Room Capacity:",room_data["room_capacity"])
    room_data ["room_occupied_seats"] = int(room_data["room_occupied_seats"] -1)
    print(("Room Occupied Seats:"), room_data["room_occupied_seats"], "/", room_data["room_capacity"])

else:
    if (cancelation == "no"):
        print("==========")
        print("The reservation is kept")
        print("Room Code:",room_data["room_code"])
        print("Room Status:",room_data["room_status"])
        print("Room Location:",room_data["room_location"])
        print("Room Capacity:",room_data["room_capacity"])
        print("Room Occupied Seats:",room_data["room_occupied_seats"])
if (cancelation != "yes" and cancelation != "no"):
    print(" ")
    print("Error: Only lowercase yes or no are accepted.")
