#Exercise 1
from dbm import error


print("--- Exercise 1: Build a list ---")

inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))




#Exercise 2
print("--- Exercise 2: INDEX PRACTICE ---")
print(inventory[0])
print(inventory[-1])

middle = len(inventory) // 2
print(inventory[middle])


#Exercise 3
print("--- Exercise 3: list slicing ---")
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

#Exercise 4
print("--- Exercise 4: list methods ---")
inventory.append("envelope")
inventory.append("tape")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)

#Exercise 5
print("--- Exercise 5: tuple comparison ---")
coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError as error:
    print(f"typeerror caught: {error}")
    print("Tuples are immutable, so you cannot change their values.")

#Exercise 6
print("--- Exercise 6: list average sales ---")

sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print(f"total sales: {total}, number of sales: {count}, average sale: {average}")
print(f"best sale: {max(sales)}, worst sale: {min(sales)}")

best = sales[0]
worst = sales[0]
for sale in sales:
    if sale > best:
        best = sale
    if sale < worst:
        worst = sale
print(f"best sale: {best}, worst sale: {worst}")

#Exercise 7
print("--- Exercise 7: accumulator pattern ---")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]

discounted = []
for price in prices:
    discounted.append(round(price * 0.9, 2))

    print(prices)
    print(discounted)


#Exercise 8
print("--- Exercise 8: filter above threshold ---")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []

for amount in sales:
    if amount > 300:
        high_sales.append(amount)
print(high_sales)
print(f"count: {len(high_sales)}")
print(f"average: {sum(high_sales) / len(high_sales)}")




