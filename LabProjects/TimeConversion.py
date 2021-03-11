"""10.	Write a Python program to convert seconds to day, hour, minutes and seconds. """
time_in_seconds = int(input("Enter time in Seconds:"))
day = time_in_seconds/(60*60*24)
hours = time_in_seconds/(60*60)
minutes = time_in_seconds/60
seconds = time_in_seconds
print("The day is:", day)
print("The hour is:", hours)
print("The minute is:", minutes)
print("The seconds is:", seconds)