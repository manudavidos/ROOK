available = 0 
booked = 1
other = 2
room_code = "003M"
room_status = int(booked)
room_location = "Main Building"
room_capacity = 10
room_occupied_seats = 0
room_booked_by = []

booking_by = "NOTANAUAEMAIL"
email_input_trial = 0

#Show basic room information without status
print("Room Code:", room_code)
print("Room Location:", room_location)
print("Number of Occupied Seats:", room_occupied_seats, "/", room_capacity)
print("Room is booked by:", room_booked_by)

if(room_status==available or room_status==booked and room_occupied_seats < room_capacity): #Check if the room is available for booking
    if (room_status==available):
        print("Room Status: Available")
    else:
        if (room_status==booked):
            print("Room Status: Booked (has additional seats)")
    answer = str(input("The room is available for booking, do you want to book it? (yes/no): ")) #Ask user if they want to book the room
    if(answer=="yes"): #Check if the answer is yes
        while (booking_by.find("@edu.aua.am") == -1 and booking_by.find("@aua.am") == -1):
            if (email_input_trial == 0):
                booking_by = str(input("Please enter your AUA email to continue booking: "))
                email_input_trial += 1
            else:
                print ("Error 002: The email entered is not valid, please try again")
                booking_by = str(input("Please enter your AUA email to continue booking: "))
                email_input_trial += 1
        room_booked_by.append(booking_by)
        room_occupied_seats += 1
        room_status=int(booked) #Change the room status
        print("==========")
        print("You have successfully booked the room") #Inform the user about the success
        print("Room Code:", room_code)
        print("Room Location:", room_location)
        print("Number of Occupied Seats:", room_occupied_seats, "/", room_capacity)
        print("Room is booked by:", room_booked_by)
        if(room_status==booked):
            print("Room Status: Booked") #Output the final room status
    else:
        if(answer=="no"): #Check if the answer is no
            print("==========")
            print("You have canceled the question, the room will stay unbooked") #Inform about the cancelation of the request
            print("Room Code:", room_code)
            print("Room Location:", room_location)
            print("Number of Occupied Seats:", room_occupied_seats, "/", room_capacity)
            print("Room is booked by:", room_booked_by)
            if(room_status==available):
                print("Room Status: Available") #Output the final room status
                print("==========")
                print("THE PROGRAM WILL EXIT NOW") #Inform about the termination of the program
            else:
                 if(room_status==booked):
                    print("Room Status: Booked") #Output the final room status
                    print("==========")
                    print("THE PROGRAM WILL EXIT NOW") #Inform about the termination of the program
        else:
            print("Error 001: Only lowercase yes or no are accepted.") #Output error if any answer is other than yes/no


else:
  if(room_status==booked and room_occupied_seats == room_capacity): #Check if the room is booked
    print("Room Status: Booked") #Output the final room status
    print("Sorry, this room is fully booked. Try later...") #Tell user to try again later
