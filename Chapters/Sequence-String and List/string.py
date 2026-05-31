#A series of characters is referred to as a string. Python relies heavily on this idea
#to function correctly. There are a few key aspects to consider about string.
#Krishna Kumar Mohbey & Malika Acharya
#All rights reserved-© 2023 Bentham Science Publishers
#78   
#Basics of Python Programming: A Quick Guide for Beginners
#Mohbey and Acharya
#Strings are amongst the most popular types in Python.
#It can create them simply by enclosing characters in quotes (single, double, or
#triple).
#Python treats single quotes the same as double quotes.
#A string is a sequence of Unicode characters, and a character is simply a symbol.

str = "This is a string"
print (str)
print (" ")

str1 = "Python"
print (str1[0])
print (str1[1])
print (str1[2])
print (str1[3])
print (str1[4])
print (str1[5])
print (" ")
#similar to str.length in Java
for i in "Krishima":
    print (i)
print (" ")

#Other concepts about string include the len() function for getting the length of a
#string, keyword in, and not in for checking whether the substring or character is
#present in a string.
print (len(str))

str2 = "Python is so simple"
print ("simple" in str2)

str3 = "Python is so simple"
if "simple" in str3:
    print ("Yes, 'simple' is present.")
else :
    print ("No, 'simple' is not present.")

str4 = "Python is so simple"
print ("programming" not in str4)
