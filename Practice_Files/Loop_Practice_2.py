#Aight les do this loop practice

#Conditional Loops
#Ex 1: Simple Counter
count= 0
while (count<100):
    print(count,"okay")
    count+= 1

#Ex 2: Retry button based on user input
import random
answer= "YES"
while (answer == "YES" or answer=="Y"):
    ranNum=random.randint(1,7)
    print(ranNum)
    answer = input("Wanna try again? ").upper()

#For Loops (Counting)    
#Ex 3: Displays amount in range
for count in range(100):
    print(count, "cat")
    
#Ex 4: Counting Backwards loop
for count in range(100,0,-1):
    print(count, "dog")

#Ex 5: A for loop that goes through a sequence
word = input("Word here pls: ")
for i in word:
    print(i,end="!")
print()

#Ex 6: Prints all individual letters of a sentence using in range
word = input("Another word here pls: ")
length = len(word)
for i in range(length):
    print(word[i], end ="!")
print()

#Ex 7: Average Calculator ting
sum = 0
for count in range(4):
    mark= int(input("Please input marks: "))
    sum+=mark
print("Your Average is: ", round(sum//4), "quail")

#Ex 8: AEIOU
word = input("Enter a word: ")
for letter in word:
    if(letter in "aeiou"):
        print(letter, end="")
    else:
        print("_", end="")
print()

#Ex 9: LAST ONE HOOO
for row in range (10):
    for digits in range(row):
        print("*", end="")
    print("")


#Exceptional Handling
#Ex 1: Handling general exceptions using while
while True:
    try:
        num=int(input("Please enter an integer: \n"))
        break
    except:
        print("Invalid input, try again hoe")
print("Number\t\tSquared\t\tCubed")
print(num,"\t\t",num**2,"\t\t", num**3)

#Ex 2: Adding all even numbers starting from input between 1-100
while True:
    try:
        num=int(input("Please enter an integer in between 1 and 100: "))
        if (0<num<100):
                break
    except:
        print("Input number between 1-100 hoe.")
sum = 0
for i in range(num,101):
    if (i%2==0):
        sum+=i
print("Your total is:", sum/((num+100)/2))
