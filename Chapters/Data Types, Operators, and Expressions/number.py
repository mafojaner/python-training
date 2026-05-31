#-The number is responsible for storing numerical values. A Python Numbers data
#type is responsible for storing all integer, float, and complex values. To check the
#data type of a variable, Python has a function called type(). It also has the
#isinstance() function that checks whether or not an object belongs to a specific
#class. When a number is assigned to a variable in Python, Number objects are
#created automatically. A number data type can store int, float, and complex type
#values.
#The integer value can be any length. There is no limitation on the length of an
#integer in Python.
#Float is used to store floating-point numbers which is accurate up to 15 decimal
#points.
#A complex number is specified in the form of a + ib, where a and b stand for the
#real and imaginary components of the number, respectively 

a = 10
print ("The type of a is ", type (a))
print ("a is an integer: ", isinstance (a, int))

b = 10.15
print ("The type of b is ", type (b))
print ("b is a float: ", isinstance (b, float))

c = 2 + 4j
print ("The type of c is ", type (c))
print ("c is a complex number: ", isinstance (c, complex))