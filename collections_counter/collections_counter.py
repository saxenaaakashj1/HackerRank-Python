from collections import Counter


def main():
    # Read number of shoes available
    # (not used, but needed to align input in HackerRank)
    _ = int(input("Numbers of shoes available: "))

    # Read the sizes of the available shoes and count them using Counter
    sizes_available = Counter(input("Available sizes: ").split())

    # Read number of customers who want to buy shoes
    interested_buyers = int(input("Interested buyers: "))

    total_revenue = 0  # Initialize total revenue

    # Process each buyer
    for _ in range(interested_buyers):
        size, price = input("Size and price to pay: ").split()

        # Check if the requested shoe size is in stock
        if sizes_available[size] > 0:
            total_revenue += int(price)  # Add price to total revenue
            sizes_available[size] -= 1  # Decrease stock for that size

    # Print total revenue generated from all valid sales
    print(f"Total Revenue: {total_revenue}")


if __name__ == "__main__":
    main()
