""" 8. Given a three digit number.Find the sum of its digits"""


def sum(a):
    sum = int(a[0]) + int(a[1]) + int(a[2])
    return sum


a = str(int(input("Enter three digit number:")))
d = sum(a)
print(d)
