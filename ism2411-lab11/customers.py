#use .get when a key might be missing and bracket notation if you know its there
#It reminds me of excell pivot tables. Python is more usefull for large data sets because it can save time and takes up less space


print("--Exercise 1--")
customer = {
    "name": "Alice",
    "Name": "Not-Alice",
    "email": "alice@example.com",
    "tier": "Gold",
    "ytd_spend": 12400.
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])


print("--Exercise 2--")
customer['phone'] = '555-5555'
print(customer)
customer['tier'] = 'Platinum'
print(customer)
del customer['Name']
print(customer)

print(customer.get('ytd_spend', 0))

print("--Exercise 3--")
print(customer.get("email", "No email provided"))

print("--Exercise 4--")
for key, value in customer.items():
    print(f"{key}: {value}")

for something in customer:
    print(something, customer[something])

print("--Exercise 5--")
tier_discounts = {
    "bronze": 0,
    "silver": 0.05, 
    "gold": 0.1, 
    "platinum": 0.15
    }

purchase = 200
discount_rate = tier_discounts.get(customer['tier'], 0)
final_price = purchase * (1 - discount_rate)
print(f"tier: {customer['tier']}")
print(f"discount rate: {discount_rate * 100}%")
print(f"final price: {final_price:.2f}")

print("--Exercise 6--")
customers = [
    {"name": "Bob", "tier": "Silver", "ytd_spend": 3200.},
    {"name": "Carol", "tier": "Gold", "ytd_spend": 8750.},
    {"name": "David", "tier": "Bronze", "ytd_spend": 450.},
]

for record in customers:
    rate = tier_discounts.get(record['tier'], 0)
    discount = 300 * rate
    print(f"{record['name']} ({record['tier']}): ${discount:.2f} off a $300 purchase")

print("--Exercise 7--")
catalog = {
    "widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}
for product_name, product_details in catalog.items():
    if product_details['stock'] < 20:
        print(f"LOW STOCK: {product_name} - only {product_details['stock']} left in stock!")

print("--Exercise 8--")
transactions = [
    {"region": "South", "amount": 300.},
    {"region": "North", "amount": 150.},
    {"region": "South", "amount": 200.},
]
sales_by_region = {}
for sale in transactions:
    region = sale['region']
    amount = sale['amount']
sales_by_region[region] = sales_by_region.get(region, 0) + amount
print(sales_by_region)

