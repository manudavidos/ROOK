available = 0 
booked = 1
other = 2
room_code = "003M"
room_status = int(other)
room_location = "Main Building"

#Show basic room information without status
print("Room Code:", room_code)
print("Room Location:", room_location)

if(room_status == other): #check if the room is booked for another purpose, e.g. meeting, exam
  print("Room Status: Other")
  answer = str(input("The room is reserved for another purpose. Are particpant? (yes/no) ")) #ask the user if he/she is participant and wants to enter the room
  print("==========")
  if(answer == "yes"):
    
    while True:
      password = input("Please enter the password: ") #if the user is participant he/she will have password to enter the room
      if(password == "123456"):
       print("Your password is correct, you can enter the room")
       break
      
      else:
       print("Your password is incorrect")
  if(answer == "no"):
     print("The room is unavailable for you, please try booking another room")
       
if(room_status==available): #Check if the room is available
  print("Room Status: Available")
  answer = str(input("The room is available for booking, do you want to book it? (yes/no): ")) #Ask user if they want to book the room
  if(answer=="yes"): #Check if the answer is yes
    room_status=int(booked) #Change the room status
    print("==========")
    print("You have successfully booked the room") #Inform the user about the success
    print("Room Code:", room_code)
    print("Room Location:", room_location)
    if(room_status==booked):
      print("Room Status: Booked") #Output the final room status
  else:
    if(answer=="no"): #Check if the answer is no
      print("==========")
      print("You have canceled the question, the room will stay unbooked") #Inform about the cancelation of the request
      print("Room Code:", room_code)
      print("Room Location:", room_location)
      if(room_status==available):
        print("Room Status: Available") #Output the final room status
        print("==========")
        print("THE PROGRAM WILL EXIT NOW") #Inform about the termination of the program
    else:
      print("Error 001: Only lowercase yes or no are accepted.") #Output error if any answer is other than yes/no


else:
  if(room_status==booked): #Check if the room is booked
    print("Room Status: Booked") #Output the final room status
    print("Sorry, this room is unavailable. Try later...") #Tell user to try again later
    
