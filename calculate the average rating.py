#!/usr/bin/python3

n1 = float(input("write the first note"))
while n1 < 0 or n1 > 20:
    n1 = float(input("try again"))

n2 = float(input("write the second note"))
while n2 < 0 or n2 > 20:
    n2 = float(input("try again"))

n3 = float(input("write the third note"))
while n3 < 0 or n3 > 20:
    n3 = float(input("try again"))

M = (n1 + n2 + n3) / 3
print("average rating", M)

if M > 16:
    print("Excellent")
elif M >= 14 and M < 16:
    print("Very good")
elif M >= 12 and M < 14:
    print("Good")
else:
    print("Satisfactory")
