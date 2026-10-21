principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (%): "))
time = float(input("Enter the time in years: "))

simple_interest = principal * rate * time / 100

print(f"Simple interest: {simple_interest:.2f}")