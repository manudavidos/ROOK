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
    "room_status":status["available"],
    "room_location":location["main_building"],
    "room_capacity":10,
    "room_occupied_seats":0,
    "room_booked_by":[]
}
user_details = {
    "id":0,
    "first_name":"",
    "last_name":"",
    "email":"aua@aua.am"
}

email_input_trial = 0
answer_trial = 0
answer="NOANSWER"

#Show basic room information without status
print("Room Code:", room_details["room_code"])
print("Room Location:", room_details["room_location"]["name"])
print("Number of Occupied Seats:", room_details["room_occupied_seats"], "/", room_details["room_capacity"])
print("Room is booked by:", room_details["room_booked_by"])
print("Room Status:", room_details["room_status"]["name"])

if(room_details["room_status"]!=status["other"] and room_details["room_occupied_seats"] < room_details["room_capacity"]): #Check if the room is available for booking
    while(answer!="yes" and answer!="no"):
        if(answer_trial!=0):
            print("Error 003: Only lowercase yes or no are accepted.")
        answer = str(input("The room is available for booking, do you want to book it? (yes/no): ")) #Ask user if they want to book the room
        answer_trial += 1
    if(answer=="yes"): #Check if the answer is yes
        while (user_details["email"].find("@edu.aua.am") == -1 and user_details["email"].find("@aua.am") == -1):
            if (email_input_trial == 0):
                user_details["email"] = str(input("Please enter your AUA email to continue booking: "))
                email_input_trial += 1
            else:
                print ("Error 002: The email entered is not valid, please try again")
                user_details["email"] = str(input("Please enter your AUA email to continue booking: "))
                email_input_trial += 1
        room_details["room_booked_by"].append(user_details["email"])
        room_details["room_occupied_seats"] += 1
        room_details["room_status"]=status["booked"] #Change the room status
        print("==========")
        print("You have successfully booked the room") #Inform the user about the success
        print("Room Code:", room_details["room_code"])
        print("Room Location:", room_details["room_location"]["name"])
        print("Number of Occupied Seats:", room_details["room_occupied_seats"], "/", room_details["room_capacity"])
        print("Room is booked by:", room_details["room_booked_by"])
        print("Room Status:", room_details["room_status"]["name"]) #Output the final room status
    elif(answer=="no"): #Check if the answer is no
        print("==========")
        print("You have canceled the question, the room will stay unbooked") #Inform about the cancelation of the request
        print("Room Code:", room_details["room_code"])
        print("Room Location:", room_details["room_location"]["name"])
        print("Number of Occupied Seats:", room_details["room_occupied_seats"], "/", room_details["room_capacity"])
        print("Room is booked by:", room_details["room_booked_by"])
        print("Room Status:", room_details["room_status"]["name"]) #Output the final room status
        print("==========")
        print("THE PROGRAM WILL EXIT NOW") #Inform about the termination of the program
    else:
        print("Error 001: Unknown Error has occured, please contact your administrator and tell them the error number") #Output error...


elif(room_details["room_status"]==status["booked"] and room_details["room_occupied_seats"] == room_details["room_capacity"]): #Check if the room is booked
    print("Sorry, this room is fully booked. Try later...") #Tell user to try again later
