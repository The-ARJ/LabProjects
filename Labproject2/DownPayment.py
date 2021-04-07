""" 3.Price of a house is $1M. If buyer has good credit, they need to put down 10% otherwise
 they need to put down 20% Print the down payment"""
price_of_house=1000000
buyer = str(input("Enter Yes/No:"))
if buyer == "yes" or "Yes":
    down_payment = (10 * price_of_house) / 100
if buyer == "no" or "No":
    down_payment = (20 * price_of_house) / 100
print("The Down payment is:",down_payment)

