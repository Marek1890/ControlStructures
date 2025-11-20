### atm.py
balance = 1000
pin = "1111"  

def check_pin():
    p = input("Enter PIN: ")
    if p == pin:
        print("PIN ok")
    else:
        print("Wrong PIN")

def change_pin():
    global pin
    old = input("Enter old PIN: ")
    if old != pin:
        print("Nope.")
        return
    new = input("Enter new 4-digit PIN: ")
    if len(new) == 4 and new.isdigit():
        pin = new
        print("Changed.")
    else:
        print("Bad PIN format.")

while True:
    print()
    print("ATM Menu:")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check PIN")
    print("5. Change PIN")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")
    print()

    if choice == '1':
        print("Balance:", balance)

    elif choice == '2':
        amount = float(input("Deposit amount: "))
        balance += amount
        print("OK, new balance:", balance)

    elif choice == '3':
        amount = float(input("Withdraw amount: "))
        if amount <= balance:
            balance -= amount
            print("Done. New balance:", balance)
        else:
            print("No money buddy")

    elif choice == '4':
        check_pin()

    elif choice == '5':
        change_pin()

    elif choice == '6':
        print("Bye")
        break

    else:
        print("?? Wrong option")