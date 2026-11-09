# ISM2411 Lab 11 — Customer Dictionary & Lookup
# Name: Pedro Mortari
#
# REFLECTION
# 1. .get() vs bracket notation:
#    I'd use .get() when a key might legitimately be missing, like optional
#    customer fields (phone, email) in messy CRM data, so the program keeps
#    running with a sensible default. I'd use brackets when the key must exist,
#    like a customer ID, because a KeyError tells me right away the data is
#    broken. Rule of thumb: optional field -> .get(), required field -> [].
#
# 2. Summary dictionary pattern:
#    It's like a SUMIF or a PivotTable in Excel that totals sales by region.
#    The Python version scales to millions of rows without slowing down or
#    crashing, can be rerun automatically on new data, and is easy to extend
#    with more logic than a spreadsheet formula allows.

# ---------- Exercise 1: One customer ----------
print("=== Exercise 1 ===")
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1250.75,
}
print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)

# ---------- Exercise 2: Update and add ----------
print("\n=== Exercise 2 ===")
customer["phone"] = "813-555-0123"
print(customer)
customer["tier"] = "platinum"
print(customer)
del customer["email"]
print(customer)

# ---------- Exercise 3: Safe lookup ----------
print("\n=== Exercise 3 ===")
print(customer.get("email", "no email on file"))
try:
    print(customer["email"])
except KeyError as e:
    print(f"KeyError: {e} not found")

# ---------- Exercise 4: Iterate ----------
print("\n=== Exercise 4 ===")
for key, value in customer.items():
    print(f"{key}: {value}")

# Looping over a dict directly only gives the KEYS, not the values.
# .items() gives (key, value) pairs, so you don't need customer[key].
for key in customer:
    print(key)

# ---------- Exercise 5: Lookup table ----------
print("\n=== Exercise 5 ===")
tier_discounts = {"bronze": 0, "silver": .05, "gold": .10, "platinum": .15}
purchase = 200
rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - rate)
print(f"Tier: {customer['tier']}")
print(f"Discount: {rate:.0%}")
print(f"Final price: ${final_price:.2f}")

# ---------- Exercise 6: List of dicts ----------
print("\n=== Exercise 6 ===")
customers = [
    {"name": "Alice", "tier": "platinum", "ytd_spend": 1250.75},
    {"name": "Bruno", "tier": "silver", "ytd_spend": 430.00},
    {"name": "Carla", "tier": "bronze", "ytd_spend": 95.50},
    {"name": "Diego", "tier": "gold", "ytd_spend": 780.20},
]
purchase = 300
for c in customers:
    discount = purchase * tier_discounts.get(c["tier"], 0)
    print(f"{c['name']:<6} | {c['tier']:<8} | discount on $300: ${discount:.2f}")

# ---------- Exercise 7: Nested catalog ----------
print("\n=== Exercise 7 ===")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}
for product, info in catalog.items():
    if info["stock"] < 20:
        print(f"LOW STOCK: {product} (only {info['stock']} left)")

# ---------- Exercise 8: Sales by region ----------
print("\n=== Exercise 8 ===")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]
summary = {}
for t in transactions:
    region = t["region"]
    summary[region] = summary.get(region, 0) + t["amount"]

for region in sorted(summary):
    print(f"{region}: {summary[region]}")