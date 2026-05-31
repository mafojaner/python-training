#Python Program to fund the area of a triangle
a = 5
b = 6
c = 7
#calculate the semi perimeiter = s
s = (a + b + c) / 2
#calculate the area of the triangle using Heron's formula
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print ("The area of the triangle is ", "%.2f" % area)
#%.2f is used to round the area to 2 decimal places