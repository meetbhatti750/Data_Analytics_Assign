def get_delivery_charge(amount, city="Ahmedabad"):
    if city == "Ahmedabad":
        return 30
    else:
        return 50

print("Ahmedabad:", get_delivery_charge(500))
print("Mumbai:", get_delivery_charge(500, "Mumbai"))