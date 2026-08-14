price = input("Enter the price of your zomato order: ")

price = float(price)

gst = price * 0.18
final_bill = price + gst

print("===================")
print("      Zomato Bill       ")
print("===================")
print(f"food amount      :₹{price:.2f}")
print(f"GST (18%)        :₹{gst:.2f}")

print(f"Total Amount     :₹{final_bill:.2f}")
print("===================")
print("      Thenk you for ordering!     ")
print("===================")
