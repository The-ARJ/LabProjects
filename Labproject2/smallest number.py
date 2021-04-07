""" Given three integer . print the smallest one """
a = int(input("enter value for a:"))
b = int(input("enter value for b:"))
c = int(input("enter value for c:"))
if a < b and a < c:
    print("The smaller number is", a)
elif b < a and b < c:
    print("The smaller number is", b)
else:
    print("The smaller number is", c)
