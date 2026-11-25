prices = {
    "rice": 75,
    "oil": 185,
    "sugar": 120,
    "milk": 95,
    "egg": 12,
    "flour": 65,
    "salt": 40,
    "lentil": 130,
    "potato": 45,
    "onion": 80,
    "tea": 250,
    "coffee": 450,
    "biscuit": 50,
    "soap": 70,
    "shampoo": 180
}

# show products
print("Available products:")
for item in prices:
    print(item, "-", prices[item], "taka")

order = {}

n = int(input("\nHow many order entries? "))

# taking the orders
for i in range(1, n + 1):
    item = input("Enter product " + str(i) + ": ")
    quantity = int(input("Enter quantity: "))

    if item not in prices:
        print(item, "is not available.")
    elif quantity <= 0:
        print("Quantity must be positive.")
    else:
        order[item] = order.get(item, 0) + quantity

print("\nFinal order:")
print(order)

# making the bill
bill = {}
for item in order:
    bill[item] = {
        "quantity": order[item],
        "unit_price": prices[item],
        "total": order[item] * prices[item]
    }

subtotal = 0
for item in bill:
    subtotal = subtotal + bill[item]["total"]

if subtotal >= 1000:
    discount = subtotal * 0.05
else:
    discount = 0

vat = 0.02 * (subtotal - discount)
final_amount = subtotal - discount + vat

# printing the bill
print("\n================ GROCERY SHOP BILL ================")
print(f"{'Item':<10}{'Quantity':>10}{'Unit Price':>15}{'Total':>15}")
print("-" * 52)
for item in bill:
    q = bill[item]["quantity"]
    u = bill[item]["unit_price"]
    t = bill[item]["total"]
    print(f"{item:<10}{q:>10}{u:>15.2f}{t:>15.2f}")
print("-" * 52)
print(f"Subtotal: Tk {subtotal:.2f}")
print(f"Discount (5%): Tk {discount:.2f}")
print(f"VAT (2%): Tk {vat:.2f}")
print("-" * 52)
print(f"Final amount: Tk {final_amount:.2f}")
print("=" * 52)