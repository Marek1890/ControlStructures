###
# Checking if both people are adults
#
p1 = input("Enter first name: ")
a1 = int(input("Enter first age: "))
p2 = input("Enter second name: ")
a2 = int(input("Enter second age: "))
if a1 >= 18 and a2 >= 18:
    print(f'Both {p1} and {p2} are adults')
else:
    print(f'Either {p1} or {p2} is not an adult')
