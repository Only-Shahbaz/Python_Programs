price = int(input("Enter the Price : "))
tax = 0.0

if price > 100000:
    tax = price * (15 / 100)
    print("Your Tax is ", tax)
    print("Your Price after tax is ", price + tax)

elif price > 80000 and price <= 100000:
    tax = price * (10 / 100)
    print("Your Tax is ", tax)
    print("Your Price after tax is ", price + tax)

elif price > 60000 and price <= 80000:
    tax = price * (5 / 100)
    print("Your Tax is ", tax)
    print("Your Price after tax is ", price + tax)
else:
    tax = price * (2.5 / 100)
    print("Your Tax is ", tax)
    print("Your Price after tax is ", price + tax)
