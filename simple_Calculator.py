num1 = float(input("Enter Fist Number : "))

num2 = float(input("Enter Second Number : "))

ops = input("Enter your Operation: ")

if ops == '+':
    print("Addition of Two Numbers is: ")
    print(num1+num2)

elif ops == '-':
    print("Subtraction of Two Numbers is: ")
    print(num1 - num2)

elif ops == '*':
    print("Multiplication of Two Numbers is: ")
    print(num1 * num2)

elif ops == '/':
    print("Division of Two Numbers is: ")
    print(num1 / num2)

else:
    print("Invalid Operation")
