# Mini Project: CLI Checkout and Receipt Generator (Mini POS System)

"""
Goals:
    + Create a terminal program that acts like a tiny checkout system (think: small store / cafe).

Functions:
    + Ask users for item information
    + Applies discounts
    + Calculates totals
    + Prints a clean receipt

Core Requirements:
    Inputs (strings and numbers) ->
        + Customer name
        + Item name
        + Item price
        + Quantity
        + Member status (Y/N)
        + Coupon code

Computations:
    + Subtotal: price * quantity
    + Tax (rate = 8.75 %) = subtotal * tax_rate
    + Total before discount = subtotal + tax
    + Discounts:
        - Member + subtotal > 50 -> 15% off subtotal
        - Coupon code (SAVE5) -> $5 off subtotal
            ' subtotal should not go below 0 '

RECEIPT:
            --- RECEIPT ---
        Customer: Armando (A)
        Item: Iced Coffee
        Price: $4.25
        Qty: 3
        Subtotal: $12.75
        Tax (8.75%): $1.12
        Discount: -$0.00
        Total: $13.87

Included subjects:
   + Intro to Python
   + Variables and Expressions
   + Types
   + Branching
"""

# Ask for customer information
member_status = input("Are you a member (Y/N): ")
customer_name = input("Enter order name: ")

# Retrieve item information
item = input("Enter item: ")
item_price = float(input("Enter item price: "))
item_quantity = int(input("Enter item quantity: "))
coupon_code = input("Enter coupon code (if any): ")

# Validate price/quantity is over 0
if item_price < 0 or item_quantity <= 0:
    print("Error: Invalid price or quantity.")
else:
    subtotal = item_price * item_quantity

    tax_rate = 0.0875
    discount_amount = 0

    # Discounts
    if (member_status == 'Y') and (subtotal >= 50):
        discount_amount = subtotal * 0.15
        discount_name = "15% member discount"
    elif member_status == 'Y':
        discount_amount = subtotal * 0.10
        discount_name = "10% member discount"
    elif (coupon_code == "SAVE5") and (subtotal >= 5.00):
        discount_amount = 5
        discount_name = "$5 Coupon"
    else:
        discount_amount = 0
        discount_name = "No discount"

    discounted_subtotal = subtotal - discount_amount

    # Prevent negative subtotal (optional, but good)
    if discounted_subtotal < 0:
        discounted_subtotal = 0

    tax = discounted_subtotal * tax_rate
    total = discounted_subtotal + tax

    # Print Receipt (put it inside the valid branch)
    print("----- RECEIPT -----")
    print(f"Customer: {customer_name}")
    print(f"Item: {item}")
    print(f"Qty: {item_quantity}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Discount: {discount_name}, -${discount_amount: .2f}")
    print(f"Tax (8.75%): ${tax:.2f}")
    print(f"Total: ${total:.2f}")
    print("--------------------")
