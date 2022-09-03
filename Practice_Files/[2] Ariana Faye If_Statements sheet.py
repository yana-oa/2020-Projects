#Determining Grade
print("Welcome to Part 1 of If-Statements: Determining Grade")
while 1:
    mrk= float(input("Please enter a mark: "))

    if (mrk>100):
        print("Invalid mark, too high!")
        continue

    if (0>mrk):
        print("Invalid mark, too low!")
        continue
    
    if (80<=mrk<=100):
        print("It's an A!")
        redo= str(input("Would you like to try again? y/n: "))

        if (redo== "y"):
            continue
        if (redo== "n"):
            break
        else:
            print("invalid input")
            break
            
    if (mrk>=70):
        print("It's a B")
        redo= str(input("Would you like to try again? y/n: "))
                  
        if (redo== "y"):
            continue
        if (redo== "n"):
            break
        else:
            print("invalid input")
            break
            
    if (mrk>=60):
        print("It's a C")
        redo= str(input("Would you like to try again? y/n: "))
                  
        if (redo== "y"):
            continue
        if (redo== "n"):
            break
        else:
            print("invalid input")
            break

    if (mrk>=50):
        print("It's a D")
        redo= str(input("Would you like to try again? y/n: "))
               
        if (redo== "y"):
            continue
        if (redo== "n"):
            break
        else:
            print("invalid input")
            break
        
    if (0<mrk<50):
        print("It's a R")
        redo= str(input("Would you like to try again? y/n: "))

        if (redo== "y"):
            continue
        if (redo== "n"):
            break
        else:
            print("invalid input")
            break
        
    if (0==mrk):
        print(":(")
        redo= str(input("Would you like to try again? y/n: "))
       
        if (redo== "y"):
            continue
        if (redo== "n"):
            break
        else:
            print("invalid input")
            break
    
##########################
#Calculating Ticket Discount
print(" ")
import math
print("Welcome to Part 2: Pytickets")
print("Here are the costs:")
print("\bRegular ticket price \t Discount (Buy more than 5)")
print("$10.95/ea \t\t $8.95/ea")
print("note: Limit 50)")
num= (int(input("Please enter the number of tickets: ")))

if (num>5) and (num<50) :
	t= 8.95
	total= t*num
	print("Your total is $",round(total,2), "for", num, "ticket(s)")
elif (num>50):
	print("Reached ticket limit")
elif (num<=0):
	print("Invalid ticket amount")
elif (0<num<5):
	t= 10.95
	total= t*num
	print("Your total is $",round(total, 2), "for", num, "ticket(s)")

##########################
#Calculating Roots in Quadratic Formula
print(" ")
print("Welcome to Part 3: PyRoots Calculator")
print("Following the equation ax^2+bx+c=0,")
a= float(input("Please enter a value for a: "))
b= float(input("Please enter a value for b: "))
c= float(input("Please enter a value for c: "))
D= b**2-(4*a*c)
psol= round((-b + math.sqrt(D))/(2*a), 3)
nsol= round((-b - math.sqrt(D))/(2*a), 3)

if(D>0):
	print("There are two real roots:", psol, "and", nsol)
elif(D==0):
	print("There is one real root:", psol)
elif(D<0):
	print("There are no real roots")

##########################
#Calculating Water Rate Uses
print(" ")
print("Lastly, Welcome to Part 4: GetMyWaterRate")
print("We will calculate Public Use, Company, and Government Use rates")

while 1:
    use= str(input("Please state your use (P,C,G): "))
    if (use== "P"):
       break
    if (use== "p"):
       break
    if (use== "C"):
       break
    if (use== "c"):
       break
    if (use== "G"):
       break
    if (use== "g"):
       break
    else:
        print("Invalid input, please try again")
        continue

wat=float(input("How many liters have been used?: "))

if (use== "P") or (use== "p"):
    if (0<wat<=100):
        total= float(wat*0.77)
        total= total*1.13
        print("Your total Company Water Rate Charge is: $", round(total,2))
    elif (wat>100):
        total= float(wat*0.50)
        total= total*1.13
        print("Your total Personal Water Rate Charge is: $", round(total,2))
    else:
        print("Invalid Input")

if (use== "C") or (use== "c"):
    if (wat<=1000):
        total= 300.00
        total= total*1.13
        print("Your total Company Water Rate Charge is: $", round(total,2))
    elif (wat>1000):
        total= float(300.00+(wat*.75))
        total= total*1.13
        print("Your total Company Water Rate Charge is: $", round(total,2))
    else:
        print("Invalid Input")

if (use== "G") or (use== "g"):
    if (wat<=500):
        total= 500.00
        total= total*1.13
        print("Your total Government Water Rate Charge is: $", round(total,2))
    elif (wat>500):
        total= 400.00
        total= total*1.13
        print("Your total Government Water Rate Charge is: $", round(total,2))
    else:
        print("Invalid Input")

        
