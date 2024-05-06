import random

# Define the symbols and their frequencies
SYMBOLS = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

# Define the maximum and minimum bet amounts
MAX_BET = 10
MIN_BET = 1

# Define the number of rows and columns for the slot machine display
ROWS = 3
COLS = 3

def spin_slot_machine():
    """Spin the slot machine and return the result."""
    result = []
    for _ in range(COLS):
        column = []
        for _ in range(ROWS):
            symbol = random.choices(list(SYMBOLS.keys()), weights=SYMBOLS.values())[0]
            column.append(symbol)
        result.append(column)
    return result

def display_slot_machine(result):
    """Display the slot machine result."""
    for row in zip(*result):
        print(" | ".join(row))
    print("=" * (4 * COLS - 1))

def get_bet_amount():
    """Prompt the player for their bet amount."""
    while True:
        bet = input(f"Enter your bet amount (${MIN_BET}-${MAX_BET}): ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                return bet
        print(f"Invalid bet amount. Please enter a number between ${MIN_BET} and ${MAX_BET}.")

def play_slot_machine():
    """Play the slot machine game."""
    balance = 100  # Starting balance
    while balance > 0:
        print(f"\nYour current balance: ${balance}")
        bet = get_bet_amount()
        if bet > balance:
            print("Insufficient balance. Please place a lower bet.")
            continue
        
        result = spin_slot_machine()
        display_slot_machine(result)

        # Calculate the payout
        payout = 0
        for column in result:
            if len(set(column)) == 1:  # All symbols in a column are the same
                symbol = column[0]
                payout += SYMBOLS[symbol] * bet

        # Update balance
        balance += payout - bet

        if payout > 0:
            print(f"Congratulations! You won ${payout}.")
        else:
            print("Sorry, you didn't win anything.")

    print("Game over. You ran out of balance.")

# Main function to start the game
if __name__ == "__main__":
    play_slot_machine()
