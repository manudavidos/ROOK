import json

with open('data.json') as data_file:
    data = json.load(data_file)

user_input_room_code = input("Please enter the room number you are trying to book: ")
while (not(user_input_room_code in data["rooms"].keys())):
    print ("Error 004: Room is not found, please try again!")
    user_input_room_code = input("Please enter the room number you are trying to book: ")

print("Room Code:", data["rooms"][user_input_room_code]["room_code"])
print("Room Location:", data["rooms"][user_input_room_code]["room_location"]["name"])


if(data["rooms"][user_input_room_code]["room_status"]==data["status"]["other"]):
  print("Room Status:", data["rooms"][user_input_room_code]["room_status"]["name"])
  print("")
  answer = str(input("The room is reserved for another purpose. Are particpant? (yes/no) "))
  print("")
  if(answer == "yes"):
    
   while True:
    password = input("Please enter the password: ")
    if(password == data["rooms"][user_input_room_code]["room_password"]):
      print("Your password is correct, you can enter the room")
      break
    else:
      print("Your password is incorrect")
    

  elif(answer == "no"):
   print("The room is unavailable for you, please try booking another room")
  else:
   print("Error. Only lowercase yes or no answers are accepted")

if(data["rooms"][user_input_room_code]["room_status"]==data["status"]["available"]):
  print("Room Status:", data["rooms"][user_input_room_code]["room_status"]["name"])
  print("")
  answer = str(input("The room is available for booking, do you want to book it? (yes/no): "))
  if(answer=="yes"):
    print("")
    print("You have successfully booked the room.")
    print("Room Code:", data["rooms"][user_input_room_code]["room_code"])
    print("Room Location:", data["rooms"][user_input_room_code]["room_location"]["name"])
    data["rooms"][user_input_room_code]["room_status"]=data["status"]["booked"]
    print("Room Status:", data["rooms"][user_input_room_code]["room_status"]["name"])
  elif(answer=="no"):
    print("")
    print("You have canceled the question, the room will stay available")
    print("Room Code:", data["rooms"][user_input_room_code]["room_code"])
    print("Room Location:", data["rooms"][user_input_room_code]["room_location"]["name"])
    print("Room Status:", data["rooms"][user_input_room_code]["room_status"]["name"])
  else:
    print("Error. Only lowercase yes or no answers are accepted.") 

elif(data["rooms"][user_input_room_code]["room_status"]==data["status"]["booked"]):
  print("Room Status:", data["rooms"][user_input_room_code]["room_status"]["name"])
  print("Sorry, this room is unavailable. Try later...")
