age = float(input("Enter dog human years: "))
if age <= 2:
    dog = age * 10.5
else:
    dog = 2*10.5 + (age-2)*4
print(f"The dog's age in dog's years is {int(dog)} years.")
