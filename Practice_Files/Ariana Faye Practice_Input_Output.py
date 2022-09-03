#Intro
print("Welcome to Practice 1 and 2: Input and Output!")
print()
#1
print("Part 1: Operations")
a= int(input("Please enter the first number: "))
b= int(input("Please enter the second number: " ))
print("\t", a, "+", b, "=", (a+b))
print("\t", a, "-", b, "=", (a-b))
print("\t", a, "x", b, "=", (a*b))
print("\t", a, "/", b, "=", round(a/b, 1))
print()
#2
print("Part 2: Hypotenuse")
import math
a= int(input("Please enter side a: "))
b= int(input("Please enter sibe b: "))
hyp= round((math.sqrt((a**2)+(b**2))), 2)
print("The hypotenuse is", hyp,"and the sides are", a , "and", b)
print()
#3
print("Part 3: Squares & Cubes")
num= float(input("Please enter a number: "))
num_sqr= num**2
num_cub= num**3
print("Number \t\tSquare \t\tCube")
print(str(num), "\t\t", round(float(num_sqr),1), "\t\t", round(float(num_cub),1))
print()
#4
print("Part 4: Polynomial")
num= float(input("Please enter a decimal: "))
pol= float((3*num**4)-(10*num**3)+13)
print("Number \t\tPolynomial")
print(num, "\t\t", round(float(pol)),1)
            ##No Decimal in the result?
print()
#5
print("Part 5: Average")
crs1= float(input("Please enter your first final mark: "))
crs2= float(input("Please enter your second final mark: "))
crs3= float(input("Please enter your third final mark: "))
crs4= float(input("Please enter your fourth final mark: "))
calc= (crs1+crs2+crs3+crs4)//4
print("Okay, your final average is ", math.ceil(calc),"!")
print()
#6
print("Part 6: Wages")
name= str(input("What is your Name? "))
hrs= float(input("How many hours did you work this week? "))
hwage= float(input("What is your hourly wage? "))
hsal= hwage*hrs
hsal= round(hsal, 2)
print(name, "worked", hrs, "hours, earns $",hwage,"an hour and will be paid $",hsal, "this week")
