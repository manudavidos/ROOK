room_code = "003M"
room_status = "Booked"
room_location = "Main Building"
room_capacity = 10
room_occupied_seats = 9

print("Room Code:", room_code)
print("Room Location:", room_location)
print("Number of Occupied Seats:", room_occupied_seats, "/", room_capacity)
print("Room Status:", room_status)

cancelation = str(input("Do you want to cancel your reservation? (yes/no): "))

if (cancelation == "yes"):
    print("==========")
    print("You have cencelled the reservation.")
    print("Room Code:", room_code)
    print("Room Location:", room_location)
    room_occupied_seats = room_occupied_seats - 1
    print("Number of Occupied Seats:", room_occupied_seats, "/", room_capacity)

else:
    if (cancelation == "no"):
        print("==========")
        print("The reservation is kept")
        print("Room Code:", room_code)
        print("Room Location:", room_location)
        print("Number of Occupied Seats:", room_occupied_seats, "/",
              room_capacity)
        print("Room Status:", room_status)
if (cancelation != "yes" and cancelation != "no"):
    print("Error: Only lowercase yes or no are accepted.")
