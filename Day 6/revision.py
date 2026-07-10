# even or odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")
    

# vote eligiblity
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
    
    
# largest of three numbers
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
if a >= b and a >= c:
    print(f"{a} is the largest number.")
elif b >= a and b >= c:
    print(f"{b} is the largest number.")    
else:
    print(f"{c} is the largest number.")
    
    
    
#grade calculation
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A")   
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")   
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")
    
    
#leap year check
year = int(input("Enter a year: "))
if (year % 4 == 0 ):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.") 
    
    
 