marks = int(input("Enter your Marks: "))

if marks > 90:
    print("Your Grade is 'A' ")
elif marks <= 90 and marks > 80:
    print("your Grade is 'B' ")
elif marks > 70 and marks <= 80:
    print("your Grade is 'C' ")
else:
    print("Your Grade is 'D' ")
