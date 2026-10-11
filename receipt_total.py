item = input("Enter item name: ")
price = float(input("Enter price per item: "))
quantity = int(input("Enter quantity: "))

total = price * quantity

print("\n===== RECEIPT =====")
print(f"Item: {item}")
print(f"Price per item: {price:.2f}")
print(f"Quantity: {quantity}")
print(f"Total: {total:.2f}")
