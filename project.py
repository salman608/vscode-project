import Pandas as pd

foods = []   # List to store food names
prices = []  # List to store food prices

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

# Convert lists to a Pandas DataFrame
if foods:
    df = pd.DataFrame({'Food': foods, 'Price ($)': prices})

    # Display the cart in table format
    print("\n----- Your Shopping Cart -----")
    print(df)

    # Data Analytics
    total_cost = df["Price ($)"].sum()
    avg_price = df["Price ($)"].mean()
    max_price = df["Price ($)"].max()
    most_expensive = df.loc[df["Price ($)"].idxmax(), "Food"]

    print(f"\nTotal Cost: ${total_cost:.2f}")
    print(f"Average Price per Item: ${avg_price:.2f}")
    print(f"Most Expensive Item: {most_expensive} (${max_price:.2f})")

    # Sort by price
    print("\nCart Sorted by Price:")
    print(df.sort_values(by="Price ($)", ascending=False))
else:
    print("\nYour cart is empty.")
