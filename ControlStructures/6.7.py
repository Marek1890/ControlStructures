age = int(input("Age: "))
if age < 13:
    print("Child")
elif age <= 19:
    print("Teen")
elif age <= 64:
    print("Adult")
else:
    print("Senior")
