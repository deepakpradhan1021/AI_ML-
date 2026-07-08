name=input("enter ur name:")
age=int(input("enter ur age:"))
marks=int(input("enetr ur marks:"))
print(f"welcome {name}")
if age>=18:
    print("adult")
else:
    print("minor")
    

if marks>=90:
    print("A")
elif marks>=75:
    print("B")
elif marks>=60:
    print("C")
elif marks>=40:
    print("D")
else:
    print("fail")

if marks>=40:
    print("passed")
else:
    print("failed")
