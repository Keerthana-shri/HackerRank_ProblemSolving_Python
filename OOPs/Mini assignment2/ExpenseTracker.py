import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = {}

    def AddExpense(self, category, amount):
        timestamp = datetime.datetime.now()
        expense = {'amount': amount, 'timestamp': timestamp}
        
        if category in self.expenses:
            self.expenses[category].append(expense)
        else:
            self.expenses[category] = [expense]

    def ViewExpenses(self):
        for category, expenses in self.expenses.items():
            print(f"\nCategory: {category}")
            for expense in expenses:
                print(f"Amount: Rs{expense['amount']} | Date: {expense['timestamp']}")

    def TotalExpenses(self):
        total = 0
        for expenses in self.expenses.values():
            total += sum(expense['amount'] for expense in expenses)
        return total

if __name__ == "__main__":
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Expenses")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            tracker.AddExpense(category, amount)
            print("Expense added successfully!")

        elif choice == '2':
            tracker.ViewExpenses()

        elif choice == '3':
            total = tracker.TotalExpenses()
            print(f"\nTotal Expenses: Rs. {total}")

        elif choice == '4':
            print("Exiting Expense Tracker. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")