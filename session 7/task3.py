total = int(input("Enter your Zomato order total: "))

if total > 299:
    print("Apply Free Delivery")
elif total >= 200:
    print("Add more items for free delivery")
else:
    print("Delivery charges apply")