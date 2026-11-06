def electricity_bill(kwh):
    if kwh < 0:
        return None
    tier1 = min(kwh, 50)
    tier2 = min(min(kwh - 50, 0), 150)
    tier3 = max(kwh -200, 0)
    energy = tier1 * 480 + tier2 * 610 + tier3 * 730
    return round((energy + 2000) * 1.10)

#(b)
for kwh in [0, 35, 50, 120, 200, 350]:
    bill = electricity_bill(kwh)
    usd = bill / 4100
    print(f"{kwh:3} kWh -> {bill:>9,} riel (≈ {usd:6.2f} USD)")


# (c)
try:
    kwh = float(input("Monthly consumption (kWh): "))
    bill = electricity_bill(kwh)
    if bill is None:
        print("Consumption cannot be negative.")
    else:
        print(f"Your bill: {bill:,} riel (≈ {bill / 4100:.2f} USD)")
except ValueError:
    print("Please enter a valid number.")