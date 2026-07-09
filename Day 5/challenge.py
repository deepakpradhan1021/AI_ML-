name=input("enter ur name:")
age=int(input("enter ur age:"))
marks=int(input("enter ur marks:"))
percentage=int(input("enter ur percentage:"))
if age>=18 and marks>=60 and percentage>=70:
    print("admission granted")
else:
    print("admission denied",)
print("name:",name)