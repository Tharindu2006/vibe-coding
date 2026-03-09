# Monthly Budget Program
print("=" * 35)
print("  MONTHLY BUDGET TRACKER")
print("=" * 35)

# Get total monthly budget
total_budget = float(input("\nEnter your total monthly budget: $"))

# Get expenses in a loop
total_expenses = 0
expense_list = []
expense_count = 1

print("\nEnter your expenses (type 'done' when finished):")
while True:
    expense_input = input(f"Expense {expense_count}: $")
    
    if expense_input.lower() == "done":
        break
    
    try:
        expense = float(expense_input)
        total_expenses += expense
        expense_list.append(expense)
        expense_count += 1
    except ValueError:
        print("Invalid input. Please enter a valid number or 'done' to finish.")

# Calculate remaining balance
remaining_balance = total_budget - total_expenses

# Display results
print("\n" + "=" * 35)
print("BUDGET SUMMARY")
print("=" * 35)
print(f"Total Budget    : ${total_budget:.2f}")

# Display each expense
for i, expense in enumerate(expense_list, 1):
    print(f"Expense {i}       : ${expense:.2f}")

print("-" * 35)
print(f"Total Expenses  : ${total_expenses:.2f}")
print(f"Remaining Balance: ${remaining_balance:.2f}")
print("=" * 35)

# Display warning if budget exceeded
if remaining_balance < 0:
    print(f"\n⚠️  WARNING: You have exceeded your budget by ${abs(remaining_balance):.2f}")
elif remaining_balance < 500:
    print("\n⚠️  Warning: Low Funds")
elif remaining_balance == 0:
    print("\n✓ You have used your entire budget!")
else:
    print(f"\n✓ You have ${remaining_balance:.2f} remaining in your budget.")
