""" 10. Write a python program to sum of three given integer.
 However,if two values are equal sum will be zero."""
a = int(input("Enter value for a:"))
b = int(input("Enter value for b:"))
c = int(input("Enter value for c:"))
d = a + b + c
if a == b or b == c or a == c:
    print("The sum is Zero")
else:
    print("The sum is",d)
