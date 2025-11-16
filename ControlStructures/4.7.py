###
# Calculates the sum of even numbers in the range <1,10>
#
s = 0
for i in range(1,11):
    if not i % 2 == 0:
        continue
    s += i
print(f'Sum of even numbers in the range <1,10> is {s}')
