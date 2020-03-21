room_data = {
  "Room Code: " : "003M",
  "Room Status: " : "Booked",
  "Room Location: " : "Main Building",
  "Room Capacity: " : 10,
  "Room Occupied Seats: " : 7
}

for key in room_data.keys():
  print(key,room_data[key])

cancelation = str(input("Do you want to cancel your reservation? (yes/no): "))

if (cancelation == "yes"):
    print("==========")
    print("You have cencelled the reservation.")
    print("Room Code:",room_data["Room Code: "])
    print("Room Status:",room_data["Room Status: "])
    print("Room Location:",room_data["Room Location: "])
    print("Room Capacity:",room_data["Room Capacity: "])
    room_data ["Room Occupied Seats: "] = int(room_data["Room Occupied Seats: "] -1)
    print(("Room Occupied Seats:"), room_data["Room Occupied Seats: "], "/", room_data["Room Capacity: "])

else:
    if (cancelation == "no"):
        print("==========")
        print("The reservation is kept")
        print("Room Code:",room_data["Room Code: "])
        print("Room Status:",room_data["Room Status: "])
        print("Room Location:",room_data["Room Location: "])
        print("Room Capacity:",room_data["Room Capacity: "])
        print("Room Occupied Seats:",room_data["Room Occupied Seats: "])
if (cancelation != "yes" and cancelation != "no"):
    print(" ")
    print("Error: Only lowercase yes or no are accepted.")
