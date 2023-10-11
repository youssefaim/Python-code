#!/usr/bin/python3

childage = int(input("Enter the age of your child: "))

if childage == 6 or childage == 7 :
    print("Youngster")
elif childage == 8 or childage == 9 :
    print("Pupil")
elif childage == 10 or childage == 11 :
    print("Junior")
elif childage >= 12 :
    print("Cadet")
else :
    print("This child doesn't belong to any category.")