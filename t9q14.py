def calculate_electricity_bill(units):
    total_bill = 0

    if units <= 50:
        total_bill = units * 0.50
    elif units <= 150:
        total_bill = 50 * 0.50 + (units - 50) * 0.75
    elif units <= 250:
        total_bill = 50 * 0.50 + 100 * 0.75 + (units - 150) * 1.20
    else:
        total_bill = 50 * 0.50 + 100 * 0.75 + 100 * 1.20 + (units - 250) * 1.50

    total_bill *= 1.20  # Add 20% surcharge

    return total_bill


units = float(input("Enter the electricity units consumed: "))
bill = calculate_electricity_bill(units)
print("Total electricity bill: Rs.", bill)
