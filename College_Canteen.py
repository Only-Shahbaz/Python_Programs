menu = {
          "fries" : 150,
          "coke" : 50,
          "samosa": 60,
          "popcorns":70,
          "lays" : 100
        }
cart = []
total =0

print ("-------menu-------")
for key, values in menu.items():
  print(f"{key:10} = {values}")
print ("------------------")

while True:
  food = input("Enter Food Item From Meun (q to quit)").lower()
  if food=='q':
    break
  elif menu.get(food) is not None:
    cart.append(food)

for price in cart:
  total = total + menu.get(price)

print ("\nThank You for Ordering")
print("-------------------------")
print(f"Your Order is {cart}")
print(f"Your Total Bill is Rs.{total}")