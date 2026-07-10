age=int(input("Enter your age: "))
vip=input("Are you a VIP member? (yes/no): ")
if age >= 18 and vip == "yes":
    print("You are allowed to watch movie!")
else:
    print("You are not allowed to watch movie.")
    