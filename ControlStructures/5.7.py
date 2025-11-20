### timer.py
import time

countdown = int(input("Enter the number of seconds to count down: "))

words = ["zero", "one", "two", "three", "four", "five"]

while countdown > 0:
    if countdown <= 5:
        print(words[countdown])
    else:
        print(countdown)
    countdown -= 1
    time.sleep(1)

print("Time's up!")