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
  
print()

Allow_others_to_reserve = {
    "allow others" : "yes",
    "do not allow others" : "no"
}
Allow_others_to_reserve["allow others"] =str(input("Do you want others to reserve the room as well? Answer yes/no: "))
if(Allow_others_to_reserve["allow others"] == "yes"):
    print("The room will be used only by your group. Others cannot reserve it")
if(Allow_others_to_reserve["allow others"] == "no"):
    print("Others will be able to reserve your room")
if(Allow_others_to_reserve["allow others"] != "yes"and Allow_others_to_reserve["allow others"] != "no"):
    print("Error. Only yes/no answers are accepted")

print()

Hours_of_reservation = {
    "First Option" :" 30 min",
    "Second Option" : "1 hour",
    "Third Option" : "1 hour and 30 min",
    "Forth Option" : "2 hours"
}
print("How long do you want to reserve the room? We have four options")
for key in Hours_of_reservation.keys():
    print(key, ":", Hours_of_reservation[key])
Hours_of_reservation = str(input("Please choose one of the options: "))
if(Hours_of_reservation == "First Option"):
    print("You reserved the room for 30 min")
if(Hours_of_reservation == "Second Option"):
    print("You reserved the room for 1 hour")
if(Hours_of_reservation == "Third Option"):
    print("You reserved the room for 1 hour and 30 min")
if(Hours_of_reservation == "Fourth Option"):
    print("You reserved the room for 2 hours")
if(Hours_of_reservation != "First Option" and Hours_of_reservation != "Second Option" and Hours_of_reservation != "Third Option" and Hours_of_reservation != "Fourth Option"):
    print("Error. Choose one of the options")
