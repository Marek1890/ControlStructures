n = int(input("Enter decimal: "))
orig = n
bits = ""
while n > 0:
    bits = str(n % 2) + bits
    n //= 2
print(f"{orig}(10) = {bits}(2)")
