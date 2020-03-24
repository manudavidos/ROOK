buildings = {
  "main_building" : 10,
  "paramaz_avedissian_building" : 20
}

floors = {
  "MB_floors" : 6,
  "PAB_floors" : 4
}
Wings = {
  "E" : "East",
  "W" : "West"

}
Floor = 0 #Ask the instructor if it is correct to write like this.

print("Please select the building: ")
print(buildings["main_building"], "Main Building")
print(buildings["paramaz_avedissian_building"], "Paramaz Avedissian Building")
print("==========")
input_building = int(input())
if(input_building == buildings["main_building"]):
  print("You have chosen the Main Building. Please select the floor:")
  while(Floor<= floors["MB_floors"]):
    print(Floor)
    Floor = Floor+1
  print("==========")
  input_floor = int(input())
  if(input_floor == 0):
    print(" ")
    print("You have selected the ground floor of the  Main Building!")
  if(input_floor == 1):
    print(" ")
    print("You have selected the first floor of the  Main Building!")
  else:
    if(input_floor == 2):
      print(" ")
      print("You have selected the second floor of the  Main Building!")
    else:
      if(input_floor == 3):
        print(" ")
        print("You have selected the third floor of the  Main Building!")
      else:
        if(input_floor == 4):
          print(" ")
          print("You have selected the fourth floor of the  Main Building!")
        else:
          if(input_floor == 5):
            print(" ")
            print("You have selected the fifth floor of the  Main Building!")
          else:
            if(input_floor == 6):
              print(" ")
              print("You have selected the sixth floor of the  Main Building!")
            else:
              print("ERR001: Input error")



else:
  Floor=1
  if(input_building == buildings["paramaz_avedissian_building"]):
   print("You have chosen the Paramaz Avedissian Building. Please select the floor.")
   while(Floor<=floors["PAB_floors"]):
    print(Floor)
    Floor = Floor+1
  print("==========")
  input_floor = int(input())
  
  if(input_floor == 1):

    print("You have selected the first floor of the Paramaz Avedissian Building!")
  else:
    if(input_floor == 2):
      print(" ")
      print("You have selected the second floor of the Paramaz Avedissian Building!")
    else:
      if(input_floor == 3):
        print(" ")
        print("You have selected the third floor of the Paramaz Avedissian Building!")
      else:
        if(input_floor == 4):
          print(" ")
          print("You have selected the fourth floor of the Paramaz Avedissian Building!")
        else:
            print("ERR00: Input error")
  print("==========")
  while(input_floor<=4):
    print("Choose one of the wings: East/West")
    input_wing= str(input())
    if(input_wing==Wings["E"] or input_wing==Wings["W"]):
      print("You have chosen the",input_wing,"wing!")
      break
    else:
      print("Error: Input error")
      break
  
