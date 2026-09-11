MAX_LINES = 3 #Screaming shows CONSTANT
MAX_BET = 100
MIN_BET = 1

def deposit():
    while True:
        amount = input("Enter the amount to deposit: ")
        if amount.isdigit():
            amount = int(amount)
            if amount<=0:
                print("Enter a number greater than 0")
            else:
                print("You deposited "+ str(amount) + "$")
                break
        else:
            print("Enter a number fool!")

    return amount

def getNumberOfLines():
    while True:
        line = input(f"Enter the number of lines to bet on (1 - {MAX_LINES}) ")
        if line.isdigit():
            line = int(line)
            if 1 <= line <= MAX_LINES:
                print(f"You selected {line} lines to bet on!")
                break
            else:
                print(f"Enter a number between 1-{MAX_LINES}")
        else:
            print("Enter a number BRO!")
    return line

def getBet():
    while True:
        bet = input(f"Enter Amount to bet on (${MIN_BET} - ${MAX_BET}) :")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Enter a number between {MIN_BET} - {MAX_BET}")
        else:
            print("Enter a number BRO!")
    return bet

def main():
    balance = deposit()
    lines = getNumberOfLines()
    while True:
        bet = getBet()
        total_bet = bet * lines
        if total_bet > balance:
            print("Insufficient Balance ({balance}) for betting {total_bet}!")
        else:
            break
    print(f"You are betting ${total_bet} on {lines} lines")

main()