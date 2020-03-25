import json

with open('data.json') as data_file:
    data = json.load(data_file)

floor = 0 #Ask the instructor if it is correct to write like this.

print("Please select the building:")
for building in data["location"]:
    print(data["location"][building]["name"])
print("=====")
input_building = input("")
if(input_building != data["location"]["main_building"]["name"] and input_building!=data["location"]["pab"]["name"]):
  print("Error: Input error")
if(input_building == data["location"]["main_building"]["name"]): 
  print("You have chosen the Main Building. Please select the floor:")
  while(floor<= data["location"]["main_building"]["number_of_floors"]):
    print(floor)
    floor = floor+1
  print("=====")
  input_floor = int(input())
  if(input_floor<=6):
    if(input_floor == 0):
      print("=====")
      print("You have selected the ground floor of the  Main Building!")
    elif(input_floor == 1):
      print(" ")
      print("You have selected the first floor of the  Main Building!")
    elif(input_floor == 2):
        print(" ")
        print("You have selected the second floor of the  Main Building!")
    elif(input_floor == 3):
        print(" ")
        print("You have selected the third floor of the  Main Building!")
    elif(input_floor == 4):
        print(" ")
        print("You have selected the fourth floor of the  Main Building!")
    elif(input_floor == 5):
        print(" ")
        print("You have selected the fifth floor of the  Main Building!")
    elif(input_floor == 6):
        print(" ")
        print("You have selected the sixth floor of the  Main Building!")
  else:
    print("ERR001: Input error")

else:
  floor=1
  if(input_building == data["location"]["pab"]["name"]):
   print("You have chosen the Paramaz Avedissian Building. Please select the floor.")
   while(floor<=data["location"]["pab"]["number_of_floors"]):
    print(floor)
    floor = floor+1
  print("=====")
  input_floor = int(input())
  
  if(input_floor == 1):
    print("You have selected the first floor of the Paramaz Avedissian Building!")
  elif(input_floor == 2):
    print(" ")
    print("You have selected the second floor of the Paramaz Avedissian Building!")
  elif(input_floor == 3):
    print(" ")
    print("You have selected the third floor of the Paramaz Avedissian Building!")
  elif(input_floor == 4):
    print(" ")
    print("You have selected the fourth floor of the Paramaz Avedissian Building!")
  else:
    print("ERR00: Input error")
  print("=====")
  while(input_floor<=4 and input_floor>=1):
    print("Choose one of the wings: E/W")
    input_wing= str(input())
    if(input_wing==data["location"]["pab"]["code"][0] or input_wing==data["location"]["pab"]["code"][1]):
      print("You have chosen the",input_wing,"wing!")
      break
    else:
      print("Error: Input error")
      break
  
