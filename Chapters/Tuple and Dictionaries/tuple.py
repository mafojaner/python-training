#A tuple is a group of ordered, immutable items arranged in a specific way. Tuples
#are structured similarly to lists and strings. In this context, the definition of
#immutable is that the components of the tuple are not subject to change. Once a
#tuple has been generated, it is not possible to add or remove items from the tuple.
#Even we cannot change the order in which the tuple members are presented. In
#addition, the length of the tuple cannot be altered. It is necessary to generate a
#new tuple if we wish to modify an existing one by adding or taking something
#away from it. Unlike lists, tuples are denoted by parentheses and cannot be edited.
#Tuples  are  a  sort  of  sequence equivalent to strings in terms of structure. Tuples
#can hold any components, in contrast to strings, which can only store characters.
#It indicates that the tuple contains either a list of students' names or employee IDs,
#depending on which one is selected. Tuples may also be used to store varied
#elements, implying that a single tuple can contain components of several data
#formats, such as decimal formats, integers, and characters. A sequence of music
#files, picture files, and other data types can also be stored in tuples.
#To create a tuple in Python, all the elements are enclosed in () parenthesis,
#separated by a comma. A tuple can store heterogeneous data elements. Below are
#examples of creating tuples.

#Create an empty tuple
Tuple1 = ()

Tuple2 = (10,20,30,40,50)
print (Tuple2)

Tuple3 = ('X', 'Y', 'Z')
print (Tuple3)

Tuple4 = ("Python", "Programming", "Book")
print (Tuple4)

Tuple5 = (100, 20.123, "Python Programming")
print (Tuple5)

Tuple6 = ("Python Book", [10, 20, 25])
print (Tuple6)

#To create a tuple of a single element, it should be followed by a comma. The
#following example creates a tuple of a single element.
#In the above case, if we do not put a comma after 100, then Python would treat
#Tup1 as an integer rather than a tuple variable.
Tup1 = (100,)
type(Tup1)
Tup2 = (100)
type(Tup2)

#TheTuple ()Function
##Python has a built-in function called tuple() that may be used to make tuples.
#While we can build tuples without utilising this function, it offers a different
#method. The tuple() function is used to construct a tuple in the following example.

T1 = tuple()
print (T1)

T2 = tuple ([1,2,3,4,5])
print (T2)

T3 = tuple ("Python Programming")
print (T3)
