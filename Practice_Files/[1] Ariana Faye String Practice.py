#Welcome to String Practice
#

#Part 0: Input
strng= input("Please enter a word (min 2 such as HotCoffee): ")

#PT 1: Length
leng= len(strng)
print(leng)

#PT 2: Last 2 charcs x3
print(strng[-2:]*3)

#PT 3: First half of string
print(strng[:leng//2])

#PT 4: No first and last charcs
print(strng[1:-1])

#PT 5: First two charcs moved to the end
print(strng[2:]+strng[:2])

#PT 6: Boolean that checks for charcs
print("oy" in strng, "a" in strng)

#PT 7: lowercase all
print(strng.lower())

#PT 8: UPPERCASE ALL
print(strng.upper())

#PT 9: Checks if input is str data type (non-alphabet = false)
print (strng.isalpha())

#PT 10: Replaces letters w spaces
newstr=strng.replace("o", " ")
if not "o" in strng:
    print("No letters were replaced")
else:
    print(newstr)

#PT 11: Convert to list
newstr2= newstr.split()
print(newstr2)

#PT 12: List into new string
print("".join(newstr2))

#done, thank you!
