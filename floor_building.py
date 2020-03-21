buildings = {
  "Main Building" : 10,
  "Paramaz Avedissian Building" : 20
}

floors = {
  "Main Building Floors:" : 6,
  "Paramaz Avedissian Building Floors:" : 4
}
Floor = 0 #Ask the instructor if it is correct to write like this.

print("Please select the building: ")
for key in buildings.keys():
  print(buildings[key],key)
print("==========")
input_building = int(input())
if(input_building == buildings["Main Building"]):
  print("You have chosen the Main Building. Please select the floor:")
  while(Floor<= floors["Main Building Floors:"]):
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
  if(input_building == buildings["Paramaz Avedissian Building"]):
   print("You have chosen the Paramaz Avedissian Building. Please select the floor.")
   while(Floor<=floors["Paramaz Avedissian Building Floors:"]):
    print(Floor)
    Floor = Floor+1
  print("==========")
  input_floor = int(input())

  if(input_floor == 1):
    print(" ")
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
            print("ERR001: Input error")
              
