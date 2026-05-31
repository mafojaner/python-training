#It is sometimes referred to as a built-in function because Python has its
#functionality established in the language. The Python interpreter has several built
#in functions that are always available for usage. There are many kinds of built-in
#functions, and here is an example of some of those built-in functions (Table 1):

#abs(): It returns the absolute value of a numbe
#bin(): It returns the binary version of a number
#float(): It converts a number or a string to a floating-point number
#hex(): It returns the hexadecimal version of a number
#int(): It converts a number or a string to an integer
#len(): It returns the length of an object
#list(): It creates a list in Python
#max(): It returns the largest item in an iterable or the largest of two or more arguments
#min(): It returns the smallest item in an iterable or the smallest of two or more arguments
#oct(): It returns the octal version of a number
#pow(): It returns the value of a number raised to the power of another number
#print (): It prints the specified message to the screen or other standard output device
#range(): It returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number
#round(): It rounds a number to a specified number of decimal places

x1 = abs(-5)
print (x1)

x2 = bin(10)
print (x2)

x3 = float(3)
print (x3)

x4 = hex(255)
print (x4)

x5 = int(3.5)
print (x5)

x6 = len("Hello")
print (x6)

x7 = list((1, 2, 3))
print (x7)

x8 = max(1, 5, 3)
print (x8)

x9 = min(1, 5, 3)
print (x9)

x10 = oct(8)
print (x10)

x11 = pow(2, 3)
print (x11)

print ("This is a message")

x12 = range(5)
for n in x12:
    print (n)

x13 = round(3.14159, 2)
print (x13)