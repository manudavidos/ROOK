status = {
    "available":{
    "name":"Available",
    "code":0
                },
    "booked":{
    "name":"Booked",
    "code":1
            },
    "other":{
    "name":"Other",
    "code":2
            }
        }
location = {
    "main_building":{
    "name":"Main Building",
    "code":["M"],
    "number_of_floors":7
                },
    "pab":{
    "name":"Parmaz Avetisian Building",
    "code":["E","W"],
    "number_of_floors":4
            }
        }
room_details = {
    "room_code":"003M",
    "room_status":status["other"],
    "room_location":location["main_building"]
}

print("Room Code:", room_details["room_code"])
print("Room Location:", room_details["room_location"]["name"])


if(room_details["room_status"]==status["other"]):
  print("Room Status:", room_details["room_status"]["name"])
  print("")
  answer = str(input("The room is reserved for another purpose. Are particpant? (yes/no) "))
  print("")
  if(answer == "yes"):
    
   while True:
    password = input("Please enter the password: ")
    if(password == "123456"):
      print("Your password is correct, you can enter the room")
      break
    else:
      print("Your password is incorrect")
    

  elif(answer == "no"):
   print("The room is unavailable for you, please try booking another room")
  else:
   print("Error. Only lowercase yes or no answers are accepted")

if(room_details["room_status"]==status["available"]):
  print("Room Status:", room_details["room_status"]["name"])
  print("")
  answer = str(input("The room is available for booking, do you want to book it? (yes/no): "))
  if(answer=="yes"):
    print("")
    print("You have successfully booked the room.")
    print("Room Code:", room_details["room_code"])
    print("Room Location:", room_details["room_location"]["name"])
    room_details["room_status"]=status["booked"]
    print("Room Status:", room_details["room_status"]["name"])
  elif(answer=="no"):
    print("")
    print("You have canceled the question, the room will stay available")
    print("Room Code:", room_details["room_code"])
    print("Room Location:", room_details["room_location"]["name"])
    print("Room Status:", room_details["room_status"]["name"])
  else:
    print("Error. Only lowercase yes or no answers are accepted.") 

elif(room_details["room_status"]==status["booked"]):
  print("Room Status:", room_details["room_status"]["name"])
  print("Sorry, this room is unavailable. Try later...")
