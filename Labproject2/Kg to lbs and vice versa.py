weight = float(input("Enter your weight:"))
SI_System = input("Your weight is in Kg or LBS? ")
kg_to_lbs = weight*2.20462
lbs_to_kg = weight/2.20462
if SI_System == "kg":
    print("Your weight in lbs is:", kg_to_lbs)
elif SI_System == "lbs" :
    print("Your weight in kg is:", lbs_to_kg)
else:
    print("enter in either kg or lbs")