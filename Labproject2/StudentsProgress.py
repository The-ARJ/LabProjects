"""2. WAP which accepts marks of four subjects and display total marks, percentage and grade."""

Sub1 = float(input("Enter the marks obtained in first subject:"))
Sub2 = float(input("Enter the marks obtained in second subject:"))
Sub3 = float(input("Enter the marks obtained in third subject:"))
Sub4 = float(input("Enter the marks obtained in forth subject:"))
total_marks = Sub1+Sub2+Sub3+Sub4
print("The total marks of student is:", total_marks)
percentage = ((Sub1+Sub2+Sub3+Sub4)/400)*100
print("The total percentage obtained is:", percentage)
if percentage>70:
    print("The student has got distinction")
elif percentage>60:
    print("The student has secured First Division")
elif percentage>40:
    print("The student has passed")
elif percentage<40:
    print("The student has failed")