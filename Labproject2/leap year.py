""" Check whether the given year is leap year or not.If year is leap print
LEAP YEAR else print COMMON YEAR"""
year = int(input("Enter the year:"))
a = year % 4
if a == 0:
    print("LEAP YEAR")
else:
    print("COMMON YEAR")