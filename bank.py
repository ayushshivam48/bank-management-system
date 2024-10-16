class Bank:
    def __init__(self):
        # Initialize an empty dictionary to store customer accounts
        self.accounts = {}

    def create_account(self, account_number, account_holder, balance):
        """
        Create a new bank account.
        :param account_number: Unique account number
        :param account_holder: Name of the account holder
        :param balance: Initial balance to be deposited
        """
        # Create a new account with provided details and add it to the accounts dictionary
        self.accounts[account_number] = {
            "account_holder": account_holder,
            "balance": balance
        }
        print(f"Account created successfully for {account_holder} with Account Number: {account_number}")

    def display_accounts(self):
        """
        Display all bank accounts and their details.
        """
        print("\nList of all bank accounts:")
        if not self.accounts:
            print("No accounts found.")
        for acc_num, details in self.accounts.items():
            print(f"Account Number: {acc_num}, Account Holder: {details['account_holder']}, Balance: {details['balance']}")
        print()

    def deposit(self, account_number, amount):
        """
        Deposit money into an account.
        :param account_number: Account number to deposit money into
        :param amount: Amount of money to deposit
        """
        # Check if the account exists
        if account_number in self.accounts:
            # Add the deposit amount to the existing balance
            self.accounts[account_number]['balance'] += amount
            print(f"₹{amount} deposited successfully into Account Number: {account_number}. Current Balance: ₹{self.accounts[account_number]['balance']}")
        else:
            # Handle case when account number is not found
            print(f"Account Number: {account_number} not found.")

    def withdraw(self, account_number, amount):
        """
        Withdraw money from an account.
        :param account_number: Account number to withdraw money from
        :param amount: Amount of money to withdraw
        """
        # Check if the account exists
        if account_number in self.accounts:
            if self.accounts[account_number]['balance'] >= amount:
                # Deduct the amount from the balance
                self.accounts[account_number]['balance'] -= amount
                print(f"₹{amount} withdrawn successfully from Account Number: {account_number}. Current Balance: ₹{self.accounts[account_number]['balance']}")
            else:
                # Handle case when insufficient balance
                print(f"Insufficient balance in Account Number: {account_number}. Current Balance: ₹{self.accounts[account_number]['balance']}")
        else:
            # Handle case when account number is not found
            print(f"Account Number: {account_number} not found.")

    def check_balance(self, account_number):
        """
        Check the balance of an account.
        :param account_number: Account number to check balance for
        """
        # Check if the account exists
        if account_number in self.accounts:
            print(f"Account Number: {account_number}, Balance: ₹{self.accounts[account_number]['balance']}")
        else:
            # Handle case when account number is not found
            print(f"Account Number: {account_number} not found.")

def main():
    # Create an instance of the Bank class
    bank = Bank()

    while True:
        # Display the menu of the bank management system
        print("\nBank Menu:")
        print("1. Create Account")
        print("2. Display All Accounts")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Check Balance")
        print("6. Exit")

        # Take user input for the menu option
        choice = input("Enter your choice: ")

        if choice == '1':
            # Option to create a new account
            account_number = input("Enter Account Number: ")
            account_holder = input("Enter Account Holder Name: ")
            balance = float(input("Enter Initial Balance: ₹"))
            bank.create_account(account_number, account_holder, balance)

        elif choice == '2':
            # Option to display all accounts
            bank.display_accounts()

        elif choice == '3':
            # Option to deposit money into an account
            account_number = input("Enter Account Number: ")
            amount = float(input("Enter Amount to Deposit: ₹"))
            bank.deposit(account_number, amount)

        elif choice == '4':
            # Option to withdraw money from an account
            account_number = input("Enter Account Number: ")
            amount = float(input("Enter Amount to Withdraw: ₹"))
            bank.withdraw(account_number, amount)

        elif choice == '5':
            # Option to check account balance
            account_number = input("Enter Account Number: ")
            bank.check_balance(account_number)

        elif choice == '6':
            # Exit the program
            print("Exiting the Bank Management System.")
            break

        else:
            # Handle invalid menu choices
            print("Invalid choice. Please select again.")

# Entry point of the program
if __name__ == "__main__":
    main()
