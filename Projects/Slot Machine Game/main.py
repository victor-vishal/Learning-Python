import random

MAX_LINES = 3 #Screaming shows CONSTANT
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count ={
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

symbol_value ={
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winnings_lines=[]
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(line + 1)
    return winnings, winnings_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = [] # A,A, B,B,B,B
    for symbol, symbolCount in symbols.items(): # items() returns dictionary key value pairs as tuples
        for _ in range(symbolCount):    # _ is called throwaway/dummy variable, we use it show that we dont care about the variable, we just use it as a iterator 
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:] #copies list
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value) # prevents same symbol occurence in a column
            column.append(value)
        columns.append(column)

    return columns

def print_slot_machine(columns): #transposes matrix
    for row in range(len(columns[0])): # 0 assumes that we have at least one column
        for i, column in enumerate(columns):#returns i, sublist
            if i != len(column)-1:
                print(column[row], end=" | ")
            else:
                print(column[row])

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

def spin(balance):
    lines = getNumberOfLines()
    while True:
        bet = getBet()
        total_bet = bet * lines
    
        if total_bet > balance:
            print("Insufficient Balance ({balance}) for betting {total_bet}!")
        else:
            break
    
    print(f"You are betting ${total_bet} on {lines} lines")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winnings_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}")
    print(f"You won on ", *winnings_lines) # * unpacks the list and prints each element

    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press Enter to play, q to quit: ")
        if answer == "q":
            break
        balance +=spin(balance) 
    print(f"You left with ${balance}")
main()