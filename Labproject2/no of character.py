""" 4. If name is less than 3 characters long- name must be at least 3 characters
otherwise if it's more than 50 characters - name must be minimum of 50 characters
otherwise - name looks good!"""
name = str(input("Enter Your Name:"))
if len(name)<= 3:
    print("The name must be 3 character long")
elif len(name) > 50:
    print("The name must be less or equal to 50 character long")
else:
    print("The name is good")