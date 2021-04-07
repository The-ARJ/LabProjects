""" 5.weight converter:
input the weight of a person in either kg or lbs.
if the person provides his/her
weight in kg then convert it into lbs
else convert it to kg"""
weight = float(input("Enter your weight:"))
SI_System = input("Your weight is in Kg or LBS? ")
kg_to_lbs = weight*2.20462
lbs_to_kg = weight/2.20462
if SI_System == "kg" or "Kg" or "KG":
    print("Your weight in lbs is:", kg_to_lbs)
elif SI_System == "lbs" or "LBS" or "Lbs":
    print("Your weight in kg is:", lbs_to_kg)
else:
    print("enter in either kg or lbs")

