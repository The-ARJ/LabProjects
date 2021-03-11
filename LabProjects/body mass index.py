"""6. Solve each of the following problems using Python Scripts. Make sure you use appropriate variable names and comments.
When there is a final answer have Python print it to the screen.
 A person’s body mass index (BMI) is defined as:
 BMI=mass in kg / (height in m)^2.
"""
Mass = float(input("Enter Body mass of the person in kg:"))
Height = float(input("Enter height of a person in meter:"))
BMI = Mass / (Height) **2
print("The Body mass index(BMI) is:",BMI)
