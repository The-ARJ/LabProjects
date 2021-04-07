""" 6. Given an integer number, print its last digit"""
num = int(input("Enter integer:"))
last_digit = num % 10
print(last_digit)

# ALSO
a = str(int(input("Enter:")))
b = len(a)
print(a[b-1])
