def deposit():
    while True: #infinite loop
        amount = input("How much would you like to deposit? $")

        if amount.isdigit():
            amount = int(amount)
            if amount <= 0:
                print("Enter Number greater than 0")
            else:
                break
        else:
            print("Enter a number only")

deposit()