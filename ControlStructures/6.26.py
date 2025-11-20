pin = "0805"
for _ in range(3):
    p = input("Enter PIN: ")
    if p == pin:
        print("Correct")
        break
    else:
        print("Incorrect...")
else:
    print("Sorry, your payment card has been blocked.")
