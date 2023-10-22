
for i in range(1,4):
    print("enter the name of the customer n'",i,":")
    a = input()
    b = int(input("Give the price of the item :"))
    if i == 1 :
        c = b + b * 0.15 - b * 0.02 
        x = a
    if i == 2 :
        d = b + b * 0.15 - b * 0.02
        y = a
    if i == 3 :
        e = b + b * 0.15 - b * 0.02
        z = a
print("The Total to be paid for the customer",x,":",c,"DH")
print("The Total to be paid for the customer",y,":",d,"DH")
print("The Total to be paid for the customer",z,":",e,"DH")