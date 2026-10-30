
# Multi-Branch Expense Matrix Analysis

branches = ["Vijayawada", "Hyderabad", "Chennai"]

expenses = [
    [10000, 15000, 12000],
    [18000, 20000, 15000],
    [12000, 10000, 14000]
]

categories = ["Rent", "Salary", "Transport"]

# Calculate branch-wise expenses
for i in range(len(branches)):
    total = sum(expenses[i])
    average = total / len(categories)

    print("\nBranch:", branches[i])
    print("Total Expense:", total)
    print("Average Expense:", average)

# Find highest expense category
totals = []

for j in range(len(categories)):
    total = 0
    for i in range(len(branches)):
        total += expenses[i][j]
    totals.append(total)

print("\nCategory-wise Expenses:")

for j in range(len(categories)):
    print(categories[j], ":", totals[j])

# Identify largest contributor
max_index = totals.index(max(totals))

print("\nLargest Expense Contributor:", categories[max_index])
print("Highest Total:", max(totals))

