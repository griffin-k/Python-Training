print("Day-01 Unit Converter")

print("Select an option:")
print("1 Distance kilometer - meter ")
print("2 Weight kilograms - grams")

choice = int(input("Enter 1 or 2: "))

if choice == 1:
    km = float(input("Enter distance in kilometers: "))
    meter = km * 1000
    print(f"{km} km is equal to {meter} meters")

elif choice == 2:
    kg = float(input("Enter weight in kilograms: "))
    grams = kg * 1000
    print(f"{kg} kg is equal to {grams} grams")

else:
    print("Invalid option Please enter 1 or 2.")
