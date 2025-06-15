import sys
import os
from bank_account import BankAccount

BALANCE_FILE = "balance.txt"

def load_balance():
    if os.path.exists(BALANCE_FILE):
        try:
            with open(BALANCE_FILE, "r") as f:
                return float(f.read())
        except ValueError:
            return 0.0
    return 0.0

def save_balance(balance):
    with open(BALANCE_FILE, "w") as f:
        f.write(str(balance))

def main():
    balance = load_balance()
    account = BankAccount(balance)

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    parts = sys.argv[1].split(":")
    command = parts[0].lower()
    amount = float(parts[1]) if len(parts) > 1 else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount:.2f}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        print(account.display_balance())
    else:
        print("Invalid command.")

    save_balance(account.get_balance())

if __name__ == "__main__":
    main()
