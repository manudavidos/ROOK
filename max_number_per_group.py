Room_Details = {
  "Room Code:" : "003M",
  "Room Status:" : "Available",
  "Room Location:" : "Main Building",
  "Room Capacity:" : 10,
  "Room Occupied Seats:" : 0
}
People_number = {
  "Number of People": 0,
  "Maximum Number Per Group" : 5
}
for key in Room_Details.keys():
  print(key, Room_Details[key])
print("===========")
print("Room booking details")
People_number["Number of People"] = int(input("Please enter the the number of people, the maximum number can be 5: "))
if(People_number["Number of People"] <= 5 ):
  
  print("You have reserved the room for:", People_number["Number of People"])

else:
  print("Sorry, you cannot have more than 5 people in your group")
