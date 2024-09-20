kWh_used = int(input("Enter the KW hours used: "))

if kWh_used <= 1000:
    total_cost = kWh_used * 0.07633
else:
    total_cost = 1000 * 0.07633
    total_cost += (kWh_used - 1000) * 0.09259

print(f" Amount owed is ${total_cost:.2f}")
