#!/usr/bin/python3
A = float(input("Enter the first number: "))
B = float(input("Enter the second number: "))
if (A > 0 and B > 0) or (A < 0 and B < 0) :
    print("The two numbers have the same sign.")
else :
    print("The two numbers have different signs.")