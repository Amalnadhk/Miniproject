class BankAccount:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def login(self, entered_pin):
        return entered_pin == self.pin

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited Rs{amount}. New balance: Rs{self.balance}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrew Rs{amount}. New balance: Rs{self.balance}"
        else:
            return "Insufficient funds. Withdrawal failed."

def main():
    # Creating a sample account
    account_number = "6381139767"
    pin = "8754"
    initial_balance = 1000

    user_account = BankAccount(account_number, pin, initial_balance)

    # Login
    entered_pin = input("Enter your PIN: ")
    if user_account.login(entered_pin):
        print("Login successful!")
    else:
        print("Incorrect PIN. Exiting...")
        return

    # Perform transactions
    while True:
        print("\nChoose an option:")
        print("a. Deposit")
        print("b. Withdraw")
        print("c. Exit")

        choice = input("Enter your choice (a/b/c): ")

        if choice == "a":
            deposit_amount = float(input("Enter the deposit amount: "))
            print(user_account.deposit(deposit_amount))
        elif choice == "b":
            withdraw_amount = float(input("Enter the withdrawal amount: "))
            print(user_account.withdraw(withdraw_amount))
        elif choice == "c":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a, b, or c"
                  ".")

if __name__ == "__main__":
    main()
