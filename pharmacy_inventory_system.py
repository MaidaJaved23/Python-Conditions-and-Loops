# Smart Pharmacy Inventory & Sales Management System
# Demonstrates for loops, range(), conditions, counters, and accumulators.

print("===== SMART PHARMACY INVENTORY & SALES SYSTEM =====")

# Ask for the number of different medicines and validate the input.
while True:
    try:
        total_medicines = int(input("How many different medicines will be processed? "))
        if total_medicines > 0:
            break
        print("Error: Enter at least 1 medicine.")
    except ValueError:
        print("Error: Please enter a whole number.")

# Initialize the revenue accumulator and restocking counter.
total_pharmacy_revenue = 0.0
medicines_requiring_restocking = 0

# Process each medicine separately.
for medicine_number in range(1, total_medicines + 1):
    print(f"\n----- Medicine {medicine_number} of {total_medicines} -----")

    # Validate the medicine name.
    while True:
        medicine_name = input("Enter medicine name: ")
        if medicine_name:
            break
        print("Error: Medicine name cannot be empty.")

    # Validate available stock.
    while True:
        try:
            available_stock = int(input("Enter available stock (units): "))
            if available_stock >= 0:
                break
            print("Error: Stock cannot be negative.")
        except ValueError:
            print("Error: Please enter a whole number for stock.")

    # Validate the price per unit.
    while True:
        try:
            price_per_unit = float(input("Enter price per unit (Rs.): "))
            if price_per_unit > 0:
                break
            print("Error: Price per unit must be greater than zero.")
        except ValueError:
            print("Error: Please enter a valid numeric price.")

    # Validate the requested sales quantity.
    while True:
        try:
            quantity_sold = int(input("Enter quantity to sell (units): "))
            if quantity_sold >= 0:
                break
            print("Error: Quantity sold cannot be negative.")
        except ValueError:
            print("Error: Please enter a whole number for quantity sold.")

    # Complete the sale only when the requested quantity is in stock.
    if quantity_sold <= available_stock:
        sales_amount = quantity_sold * price_per_unit
        remaining_stock = available_stock - quantity_sold
        total_pharmacy_revenue += sales_amount

        print("\nSale Status: Successful")
        print(f"Medicine: {medicine_name}")
        print(f"Quantity Sold: {quantity_sold} units")
        print(f"Sales Amount: Rs. {sales_amount:,.2f}")
        print(f"Remaining Stock: {remaining_stock} units")
    else:
        # No stock is deducted and no revenue is added for an unavailable sale.
        sales_amount = 0.0
        remaining_stock = available_stock

        print("\nSale Status: Not Completed")
        print(f"Medicine: {medicine_name}")
        print(
            f"Insufficient stock: requested {quantity_sold} units, "
            f"but only {available_stock} units are available."
        )
        print(f"Sales Amount: Rs. {sales_amount:,.2f}")
        print(f"Remaining Stock: {remaining_stock} units")

    # Count medicines whose remaining stock is below 10 units.
    if remaining_stock < 10:
        medicines_requiring_restocking += 1
        print("Low-Stock Warning: This medicine requires restocking.")

# Display the final pharmacy report.
print("\n===== DAILY PHARMACY SALES REPORT =====")
print(f"Total Medicines Processed: {total_medicines}")
print(f"Total Pharmacy Revenue: Rs. {total_pharmacy_revenue:,.2f}")
print(f"Medicines Requiring Restocking: {medicines_requiring_restocking}")
print("========================================")
