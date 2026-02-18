# Mini Project: CLI Checkout and Receipt Generator (Mini POS System)

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
