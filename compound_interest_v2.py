print("++++++++++++++ version_2  ++++++++++++++++++")

def get_positive_float(prompt, field_name):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value

            else:
                print(f"{field_name} must be greater than zero")
        except ValueError:
            print("Please Enter a valid name for field {field_name}")

def compound_interest(principle, rate, time):
    total_amount = principle *pow((1+rate/100), time)
    return total_amount

def main():
    principle = get_positive_float("Enter your Amount: ", "Principle")
    rate = get_positive_float("Enter your Rate: ", "Rate")
    time = get_positive_float("Enter your time: ", "Time")

    total_amount = compound_interest(principle, rate, time)

    interest_earned = total_amount - principle

    print(f"Total amount after interest: {total_amount}")
    print(f"interst earned: {interest_earned}")

if __name__=="__main__":
    main()






