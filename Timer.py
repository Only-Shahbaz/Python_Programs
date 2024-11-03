# Timer program
import time

my_time = int (input("Enter your time in seconds: "))

for x in range(my_time,-1,-1):
  seconds = x % 60
  minutes = int((x / 60)) % 60
  hours = int((x / 3600)) % 24
  print(f"{hours:02}:{minutes:02}:{seconds:02}", end="\r")
  time.sleep(1)

print("\ntime's up! \U0001F514")
