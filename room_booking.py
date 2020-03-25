import json

with open('data.json') as data_file:
    data = json.load(data_file)

answer_trial = 0
answer="NOANSWER"

user_input_room_code = input("Please enter the room number you are trying to book: ")
while (not(user_input_room_code in data["rooms"].keys())):
    print ("Error 004: Room is not found, please try again!")
    user_input_room_code = input("Please enter the room number you are trying to book: ")

#Show basic room information without status
print("Room Code:", data["rooms"][user_input_room_code]["room_code"])
print("Room Location:", data["rooms"][user_input_room_code]["room_location"]["name"])
print("Number of Occupied Seats:", data["rooms"][user_input_room_code]["room_occupied_seats"], "/", data["rooms"][user_input_room_code]["room_capacity"])
print("Room is booked by:", data["rooms"][user_input_room_code]["room_booked_by"])
print("Room Status:", data["rooms"][user_input_room_code]["room_status"]["name"])

if(data["rooms"][user_input_room_code]["room_status"]!=data["status"]["other"] and data["rooms"][user_input_room_code]["room_occupied_seats"] < data["rooms"][user_input_room_code]["room_capacity"]): #Check if the room is available for booking
    while(answer!="yes" and answer!="no"):
        if(answer_trial!=0):
            print("Error 003: Only lowercase yes or no are accepted.")
        answer = str(input("The room is available for booking, do you want to book it? (yes/no): ")) #Ask user if they want to book the room
        answer_trial += 1
    if(answer=="yes"): #Check if the answer is yes
        user_input_email = input("Please enter your AUA email: ")
        while (not(user_input_email in data["users"].keys()) or (user_input_email in data["rooms"][user_input_room_code]["room_booked_by"])):
            print ("Error 003: Email is not valid or you have already booked this room, please try again!")
            user_input_email = input("Please enter your AUA email: ")
        data["rooms"][user_input_room_code]["room_booked_by"].append(data["users"][user_input_email]["email"])
        data["users"][user_input_email]["booked_room"]=user_input_room_code
        data["rooms"][user_input_room_code]["room_occupied_seats"] += 1
        data["rooms"][user_input_room_code]["room_status"]=data["status"]["booked"] #Change the room status
        with open('data.json', 'w') as data_file:
            json.dump(data, data_file, indent=4)
        print("==========")
        print("You have successfully booked the room") #Inform the user about the success
        print("Room Code:", data["rooms"][user_input_room_code]["room_code"])
        print("Room Location:", data["rooms"][user_input_room_code]["room_location"]["name"])
        print("Number of Occupied Seats:", data["rooms"][user_input_room_code]["room_occupied_seats"], "/", data["rooms"][user_input_room_code]["room_capacity"])
        print("Room is booked by:", data["rooms"][user_input_room_code]["room_booked_by"])
        print("Room Status:", data["rooms"][user_input_room_code]["room_status"]["name"]) #Output the final room status
    elif(answer=="no"): #Check if the answer is no
        print("==========")
        print("You have canceled the question, the room will stay unbooked") #Inform about the cancelation of the request
        print("Room Code:", data["rooms"][user_input_room_code]["room_code"])
        print("Room Location:", data["rooms"][user_input_room_code]["room_location"]["name"])
        print("Number of Occupied Seats:", data["rooms"][user_input_room_code]["room_occupied_seats"], "/", data["rooms"][user_input_room_code]["room_capacity"])
        print("Room is booked by:", data["rooms"][user_input_room_code]["room_booked_by"])
        print("Room Status:", data["rooms"][user_input_room_code]["room_status"]["name"]) #Output the final room status
        print("==========")
        print("THE PROGRAM WILL EXIT NOW") #Inform about the termination of the program
    else:
        print("Error 001: Unknown Error has occured, please contact your administrator and tell them the error number") #Output error...


elif(data["rooms"][user_input_room_code]["room_status"]==data["status"]["booked"] and data["rooms"][user_input_room_code]["room_occupied_seats"] == data["rooms"][user_input_room_code]["room_capacity"]): #Check if the room is booked
    print("Sorry, this room is fully booked. Try later...") #Tell user to try again later
