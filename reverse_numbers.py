num = 123456

# write a funtion to reverse the num using while loop
def reverse_num(num):

    # Check if the number is negative
    if num < 0:
        num = -num

    # Initialize the variable to store the reversed number
    rev = 0

    # Reverse the number
    while num > 0:

        # Get the last digit of the number
        rem = num % 10

        # Append the last digit to the reversed number
        rev = rev * 10 + rem

        # Remove the last digit from the original number
        num = num // 10

    return rev

print(reverse_num(num))

