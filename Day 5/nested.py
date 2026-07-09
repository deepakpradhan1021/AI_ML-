amount=int(input("enter the amount:"))
withdraw=int(input("enter the withdraw amount:"))
if amount>=withdraw:
    print("withdraw successful")
else:
    print("insufficient balance")
    
    
    
    
    
purchase = int(input("Enter purchase amount: "))
member = input("Are you a premium member? (yes/no): ")

if member == "yes" or purchase >= 1000:
    print("Free Delivery")
else:
    print("Delivery Charges Apply")
    
    
    
age=int(input("Enter your age: "))
person=input("Are you a vip? (yes/no): ")
if person=="yes":
    print("allowed for movie")
else:
    if age>=18:
        print("allowed for movie")
    else:
        print("not allowed for movie")
        
        
        

marks=int(input("Enter your marks: "))
person=input("Are you a principal child? (yes/no): ")
if person=="yes":
    print("admission granted")
else:
    if marks>=80:
        print("admission granted")
    else:
        print("admission denied")
    