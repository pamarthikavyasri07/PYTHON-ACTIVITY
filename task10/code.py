
# Campus Resource Allocation Under Constraints

activities = ["Seminar", "Workshop", "Sports"]

requirements = [10, 15, 12]

available = 25

priority = [1, 0, 2]

allocation = [0, 0, 0]
shortages = [0, 0, 0]

# Allocate resources based on priority
for i in priority:

    if available >= requirements[i]:
        allocation[i] = requirements[i]
    else:
        allocation[i] = available

    shortages[i] = requirements[i] - allocation[i]

    available -= allocation[i]

# Display results
print("Campus Resource Allocation")

for i in range(len(activities)):
    print("\nActivity:", activities[i])
    print("Required:", requirements[i])
    print("Allocated:", allocation[i])
    print("Shortage:", shortages[i])

print("\nRemaining Resources:", available)

