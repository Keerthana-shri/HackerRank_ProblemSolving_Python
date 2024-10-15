class BankAccount:

    def __init__(self, account_number, date_of_opening, balance, customer_name):
        self.account_number = account_number
        self.date_of_opening = date_of_opening
        self.balance = balance
        self.customer_name = customer_name
 
    def deposit(self, amount):
        self.balance += amount
        print(f"${amount:.2f} has been deposited in your account.")
 
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"${amount:.2f} has been withdrawn from your account.")
 
    def check_balance(self):
        print(f"Current balance is ${self.balance:.2f}.")
 
    def print_customer_details(self):
        print("Name:", self.customer_name)
        print("Account Number:", self.account_number)
        print("Date of Opening:", self.date_of_opening)
        print(f"Balance: ${self.balance:.2f}\n")
 
if __name__ == '__main__':
    account_number = input("Enter Account Number: ")
    date_of_opening = input("Enter Date of Opening (YYYY-MM-DD): ")
    initial_balance = float(input("Enter Initial Balance: "))
    customer_name = input("Enter Customer Name: ")

    account = BankAccount(account_number, date_of_opening, initial_balance, customer_name)
 
    while True:
        print("\nChoose an operation:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Print Customer Details")
        print("5. Exit")
 
        choice = input("Enter your choice (1-5): ")
 
        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == '3':
            account.check_balance()
        elif choice == '4':
            account.print_customer_details()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

 