
bills = []
n = int(input("Enter number of months: "))

for i in range(n):
    print("\nMonth", i + 1)
    units = float(input("Enter electricity units: "))

    # Calculate progressive slab charges
    if units <= 100:
        energy = units * 2
    elif units <= 200:
        energy = 100 * 2 + (units - 100) * 3
    else:
        energy = 100 * 2 + 100 * 3 + (units - 200) * 5

    fixed = 50
    surcharge = energy * 0.05
    rebate = 0

    if units < 100:
        rebate = (energy + fixed + surcharge) * 0.10

    total = energy + fixed + surcharge - rebate
    bills.append(total)

    print("Energy Charge:", energy)
    print("Fixed Charge:", fixed)
    print("Surcharge:", surcharge)
    print("Rebate:", rebate)
    print("Total Bill:", round(total, 2))

# Compare monthly bills
print("\n--- MONTHLY BILL COMPARISON ---")

for i in range(n):
    print("Month", i + 1, "Bill:", round(bills[i], 2))

    if i > 0:
        increase = ((bills[i] - bills[i-1]) /
                    bills[i-1]) * 100

        if increase > 30:
            print("Unusual Increase:", round(increase, 2), "%")
        else:
            print("Normal Change:", round(increase, 2), "%")

