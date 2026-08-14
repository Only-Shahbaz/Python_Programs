
principle = 0
rate = 0
time = 0

while principle <=0:
    principle = float(input("Enter your principle amount: "))
    if principle <=0:
        print("Amount must not equal to or less then zero")

while rate <=0:
    rate = float(input("Enter your rate (in %)")) 
    if rate <=0:
        print("Rate must not equal to or less then zero")

while time <=0:
    time = float(input("Enter your time (in Years)")) 
    if time <=0:
        print("Time must not equal to or less then zero")


total_amount = principle * pow((1+ rate / 100), time)

print(f"Your total amount after insteret is: {total_amount}")