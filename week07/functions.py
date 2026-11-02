#1.The first bug in excersise 5 was that the total was not being calculated correctly. The line "total = sale" was replaced with "total += sale" to correctly accumulate the total sales.
#2. the apply discounts function takes two inputs, price and tier. It applies a discount based on the tier provided. The function checks the tier and applies the corresponding discount percentage to the price. If the tier is not recognized, it returns the original price without any discount.
#3. I used AI to identify bugs in excersise 5, The AI built on my understanding.



#Excersise 1 
def calculate_tax(price, rate):
    return price * rate

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax for $100 at 7%: ${tax1}")
print(f"Tax for $250 at 8%: ${tax2}")
print(f"Tax for $350 at 5%: ${calculate_tax(350, 0.05):.2f}")

#Excersise 2
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    if tier == "silver":
            return price * 0.90
    if tier == "bronze":
            return price * 0.95
    else:
          return price


original_price = 200
for tier in ["gold", "silver", "bronze", "none"]:
      print(f"{tier}: ${apply_discount(original_price, tier):.2f}")

#Excersise 3
def final_price(price, tax_rate, discount_tier):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

print(f"final_price(200, 0.07, 'gold') = ${final_price(200, 0.07, 'gold'):.2f}")

#Excersise 4
orders = [(200, ' gold'), (150, 'silver'), (80, 'bronze'), (500, 'none')]
rate = 0.07
for price, tier in orders:
    total = final_price(price, rate, tier)
    print(f"Price: ${price}, Tier: {tier}, Total: ${total:.2f}")

#Excersise 5
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale # adding the + makes it print the correct
print(f"Total: ${total}")

count = 0
for sale in sales: #fixed missing colon
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):
    print(sales[i])
    i += 1

#Excersise 6
x = 100
def double_it():
     x = 999
     return x * 2

print(x)
print(double_it())
print(x)

# 100, 1998, 100 this is because of global and local x

