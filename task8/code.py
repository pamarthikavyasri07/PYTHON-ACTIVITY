
print("HOSPITAL RESOURCE ALLOCATION SYSTEM")

wards = []
n = int(input("Enter number of wards: "))

for i in range(n):
    print("\nEnter Ward", i + 1, "Details")

    name = input("Enter ward name: ")
    beds = int(input("Enter total beds: "))
    occupied = int(input("Enter occupied beds: "))
    staff = int(input("Enter available staff: "))
    equipment = int(input("Enter available equipment: "))

    # Store ward details in nested list
    wards.append([name, beds, occupied, staff, equipment])

print("\n--- RESOURCE ANALYSIS ---")

for ward in wards:
    name, beds, occupied, staff, equipment = ward

    shortage = 0

    print("\nWard:", name)

    if occupied >= beds:
        print("Bed Shortage")
        shortage += 1
    else:
        print("Beds Available:", beds - occupied)

    if staff < 3:
        print("Staff Shortage")
        shortage += 1
    else:
        print("Staff Available")

    if equipment < 2:
        print("Equipment Shortage")
        shortage += 1
    else:
        print("Equipment Available")

    # Assign priority
    if shortage == 3:
        priority = "High Priority"
    elif shortage == 2:
        priority = "Medium Priority"
    else:
        priority = "Low Priority"

    print("Priority:", priority)

print("\nResource Analysis Completed")

