food_charge = int(input("Enter the food charge: "))

tip = 0.18 * food_charge
print(f"${tip}")

sales_tax = 0.07 * food_charge
print(f"${round(sales_tax,1)}")

grand_total = food_charge + tip + sales_tax
print(f"${grand_total}")