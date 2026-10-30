
print("BUS PASSENGER OCCUPANCY SIMULATION")

capacity = int(input("Enter bus capacity: "))
passengers = int(input("Enter initial passengers: "))
stops = int(input("Enter number of stops: "))

# Validate initial details
if capacity <= 0 or passengers < 0 or passengers > capacity or stops < 0:
    print("Invalid Input")

else:
    for i in range(stops):
        print("\nStop", i + 1)

        boarding = int(input("Enter boarding passengers: "))
        alighting = int(input("Enter alighting passengers: "))

        if boarding < 0 or alighting < 0 or alighting > passengers:
            print("Invalid Passenger Count")
            break

        passengers = passengers + boarding - alighting

        print("Current Passengers:", passengers)

        if passengers > capacity:
            print("CAPACITY VIOLATION!")
        else:
            print("Within Bus Capacity")

    print("\n--- FINAL BUS STATUS ---")
    print("Total Passengers:", passengers)
    print("Bus Capacity:", capacity)

