principal = float(input("Enter principal amount: "))
rate = float(input("Enter annual interest rate (%): "))
time = float(input("Enter time in years: "))

interest = (principal * rate * time) / 100
total_amount = principal + interest

print("\n===== INTEREST SUMMARY =====")
print(f"Principal: {principal:.2f}")
print(f"Interest: {interest:.2f}")
print(f"Total amount: {total_amount:.2f}")
