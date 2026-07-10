name=input("Enter your name: ")
age=int(input("Enter your age: "))
marks=int(input("Enter your marks: "))
percentage=int(input("enter ur perc."))
student=input("are u a principal child(yes/no):")
print("Name:",name)
if student == "no":
    if age>=18 and marks>=60 and percentage>=70:
        print("admission granted !")
    else:
        print("rejected")
else:
    print("admision granted")
    
