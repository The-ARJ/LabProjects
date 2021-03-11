"""Given the integer N - the number of minutes tha is passed since midnight - how many
hours and minutes are displayed on the 24th digital clock?"""

N = int(input('enter a minute passed since midnight:'))
hours = (N//60)
minutes = (N%60)
print ("the hours is:",hours)
print ("the minute is:",minutes)
print ("Its",hours,":",minutes,"now")