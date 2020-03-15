available = 0 
booked = 1
other = 2
room_code = "003M"
room_status = int(booked)
room_location = "Main Building"
room_capacity = 10
room_occupied_seats = 0
max_number_per_group = 5
people_number = 0


print("Room Code:", room_code)
print("Room Location:", room_location)
print("Number of Occupied Seats:", room_occupied_seats, "/", room_capacity)
print("===========")
print("Room booking details")

people_number = int(input("Please enter the the number of people, the maximum number can be 5: "))
if(people_number <= 5 ):
  print("You have reserved the room for:", people_number)

else:
  print("Sorry, you cannot have more than 5 people in your group")
