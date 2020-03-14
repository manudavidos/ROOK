Main_Building = 10
Paramaz_Avedissian_Building = 20
Main_Building_Floor = 6
Paramaz_Avedissian_Building_Floor = 4
Floor = 0

print("Please select the building: ")
print(Main_Building, "Main Building")
print(Paramaz_Avedissian_Building, "Paramaz Avedissian Building")
print("==========")
input_building = int(input())
if(input_building == Main_Building):
  print("You have chosen the Main Building. Please select the floor: ")
  while(Floor<=Main_Building_Floor):
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
  if(input_building==Paramaz_Avedissian_Building):
   print("You have chosen the Paramaz Avedissian Building. Please select the floor")
   while(Floor<=Paramaz_Avedissian_Building_Floor):
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
              
