###
# Calculates and prints the total washing time.
#
# A washing machine allows you to wash a jacket, which takes
# 40 minutes, wash underwear, which takes 70 minutes, and wash shoes,
# which takes 20 minutes. In addition, it is possible to program
# an additional rinse (15 minutes) and an additional spin (9 minutes).
#
program = input("(j)acket, (u)nderwear, (s)hoes: ")
extra_rinse = input("Extra rinse? (y/n): ")
extra_spin = input("Extra spin? (y/n): ")

total = 0
if program == "j":
    total += 40
elif program == "u":
    total += 70
else:
    total += 20
if extra_rinse == "y":
    total += 15
if extra_spin == "y":
    total += 9
print(f"Total washing time: {total} minutes")
