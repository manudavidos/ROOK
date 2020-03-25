import json

with open('data.json') as data_file:
    data = json.load(data_file)

user_input_room_code = input("Please enter the room number you are trying to book: ")
while (not(user_input_room_code in data["rooms"].keys())):
    print ("Error 004: Room is not found, please try again!")
    user_input_room_code = input("Please enter the room number you are trying to book: ")


print("Room Code:", data["rooms"][user_input_room_code]["room_code"])
print("Room Location:", data["rooms"][user_input_room_code]["room_location"]["name"])
print("Room Status:", data["rooms"][user_input_room_code]["room_status"]["name"])
print("Room Capacity:", data["rooms"][user_input_room_code]["room_capacity"])
print("Room Occupied Seats:", data["rooms"][user_input_room_code]["room_occupied_seats"])
print("")
print("Room booking details")

tries = 0
user_email = "aua@aua.am" #This is the user who is booking the room
number_of_people= 0


while(not(number_of_people<=5 and number_of_people>=1)):
  if(tries!=0):
    print("Sorry, you cannot have more than 5 people in your group")
  number_of_people = int(input("Please enter the the number of people, the maximum number can be 5: "))
  tries += 1
print("You have reserved the room for:", str(number_of_people) + " people.") 
   
print()

for option in range(len(data["hours_of_reservation"])):
    if(data["hours_of_reservation"][option]<60):
        print (str(data["hours_of_reservation"][option])+" Minute(s)")
    elif(data["hours_of_reservation"][option]>=60):
        print (str(data["hours_of_reservation"][option]/60)+" Hour(s)")
    
hours_of_reservation_answer= input(("How long do you want to reserve the room? We have " + str(len(data["hours_of_reservation"])) + " options: "))
while(hours_of_reservation_answer!="30" and hours_of_reservation_answer!="1.0" and hours_of_reservation_answer!="1.5" and hours_of_reservation_answer!="2.0"):
  print("Error. Please choose one of the options:")
  hours_of_reservation_answer= input(("How long do you want to reserve the room? We have " + str(len(data["hours_of_reservation"])) + " options: "))

if(hours_of_reservation_answer=="30"):
  data["users"][user_email]["booked_room"] = user_input_room_code
  data["users"][user_email]["booked_for"] = 30
  print("You have reserved the room for: 30 Minutes")
elif(hours_of_reservation_answer=="1.0"):
  data["users"][user_email]["booked_room"] = user_input_room_code
  data["users"][user_email]["booked_for"] = 60
  print("You have reserved the room for: 1.0 Hour")
elif(hours_of_reservation_answer=="1.5"):
  data["users"][user_email]["booked_room"] = user_input_room_code
  data["users"][user_email]["booked_for"] = 90
  print("You have reserved the room for: 1.5 Hours")
elif(hours_of_reservation_answer=="2.0"):
  data["users"][user_email]["booked_room"] = user_input_room_code
  data["users"][user_email]["booked_for"] = 120
  print("You have reserved the room for: 2.0 Hours")

with open('data.json', 'w') as data_file:
  json.dump(data, data_file, indent=4)
