
print("MOBILE PLAN COST OPTIMIZATION")

data = float(input("Enter data usage in GB: "))
calls = int(input("Enter call minutes: "))
sms = int(input("Enter SMS usage: "))
budget = float(input("Enter your budget: "))
validity = int(input("Enter required validity in days: "))

# Mobile plan details
plans = [
    ["Plan A", 199, 2, 100, 100, 28],
    ["Plan B", 299, 3, 200, 200, 28],
    ["Plan C", 399, 5, 300, 300, 56]
]

eligible = []

for p in plans:
    name, price, d, c, s, days = p

    # Check budget and validity
    if price <= budget and days >= validity:

        # Calculate excess charges
        extra_data = max(0, data - d) * 50
        extra_calls = max(0, calls - c) * 1
        extra_sms = max(0, sms - s) * 0.50

        total = price + extra_data + extra_calls + extra_sms

        eligible.append([name, total, extra_data,
                         extra_calls, extra_sms])

# Find economical plan
print("\n--- PLAN COMPARISON ---")

if eligible:
    for p in eligible:
        print(p[0], "Total Cost:", round(p[1], 2))

    best = min(eligible, key=lambda x: x[1])

    print("\n--- BEST MOBILE PLAN ---")
    print("Plan Name:", best[0])
    print("Total Cost:", round(best[1], 2))
    print("Extra Data Charge:", best[2])
    print("Extra Call Charge:", best[3])
    print("Extra SMS Charge:", best[4])

else:
    print("No eligible mobile plan found")

