unit=int(input("Enter the unit of electricity : "))
if unit <= 100:
    print("Your electricity bill is : ", unit*4)
elif unit <= 200:
    print("Your electricity bill is : ", unit*7)
else:
    print("Your electricity bill is : ", unit*10)
    