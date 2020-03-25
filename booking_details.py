room_details = {
  "room_code" : "003M",
  "room_status" : "Available",
  "room_location" : "Main Building",
  "room_capacity" : 10,
  "room_occupied_seats" : 0
}
people_number = {
  "number_of_people": 0,
  "maximum_number_per_group" : 5
}

print("Room Code:", room_details["room_code"])
print("Room Location:", room_details["room_location"])
print("Room Status:", room_details["room_status"])
print("Room Capacity:", room_details["room_capacity"])
print("Room Occupied Seats:", room_details["room_occupied_seats"])
print("")
print("Room booking details")

tries = 0


while(not(people_number["number_of_people"]<=5 and people_number["number_of_people"]>=1)):
  if(tries!=0):
    print("Sorry, you cannot have more than 5 people in your group")
  people_number["number_of_people"] = int(input("Please enter the the number of people, the maximum number can be 5: "))
  tries += 1
print("You have reserved the room for:", people_number["number_of_people"])
  
print()

hours_of_reservation = [30, 60, 90, 120]
for option in range(len(hours_of_reservation)):
    if(hours_of_reservation[option]<60):
        print (str(hours_of_reservation[option])+" Minute(s)")
    elif(hours_of_reservation[option]>=60):
        print (str(hours_of_reservation[option]/60)+" Hour(s)")
    
hours_of_reservation_answer= input(("How long do you want to reserve the room? We have " + str(len(hours_of_reservation)) + " options: "))
while(hours_of_reservation_answer!="30" and hours_of_reservation_answer!="1.0" and hours_of_reservation_answer!="1.5" and hours_of_reservation_answer!="2.0"):
  print("Error. Please choose one of the options:")
  hours_of_reservation_answer= input(("How long do you want to reserve the room? We have " + str(len(hours_of_reservation)) + " options: "))

if(hours_of_reservation_answer=="30"):
    print("You have reserved the room for: 30 Minutes")
elif(hours_of_reservation_answer=="1.0"):
    print("You have reserved the room for: 1.0 Hour")
elif(hours_of_reservation_answer=="1.5"):
    print("You have reserved the room for: 1.5 Hours")
elif(hours_of_reservation_answer=="2.0"):
    print("You have reserved the room for: 2.0 Hours")
 
