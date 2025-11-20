curr = float(input("Current price: "))
prev = float(input("Previous price: "))
drop = (prev - curr) / prev * 100
if drop >= 10:
    print("Buy the product!!")
print(f"Product price reduced by {int(drop)}%")
