foods = []   # List to store food names
prices = []  # List to store food prices
total = 0    # Variable to hold the total cost

while True:
    food = input("Enter a food to buy [q to quit]: ").strip()
    if food.lower() == 'q':
        break
    try:
        price = float(input(f"Enter the price of {food} in dollars: "))
    except ValueError:
        print("Invalid price. Please enter a valid number.\n")
        continue
    foods.append(food)
    prices.append(price)

print("\n-----Your Cart-----")
for item in foods:
    print(item, end=' ')
print()  # For a new line

for cost in prices:
    total += cost

print(f"\nYour total is: ${total:.2f}")






