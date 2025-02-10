import pandas as pd
import argparse

def calculate_auto_loan(loan_balance, months, interest_rate, additional_payment=0, extra_monthly_payment=0):
    monthly_interest_rate = (interest_rate / 100) / 12
    monthly_payment = (loan_balance * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -months)
    
    total_interest_paid = 0
    total_principal_paid = 0
    amortization_schedule = []
    
    for month in range(1, months + 1):
        interest_payment = loan_balance * monthly_interest_rate
        principal_payment = monthly_payment - interest_payment
        
        if month == 2 and additional_payment > 0:
            principal_payment += additional_payment
        
        principal_payment += extra_monthly_payment
        
        loan_balance -= principal_payment
        total_interest_paid += interest_payment
        total_principal_paid += principal_payment
        
        amortization_schedule.append({
            "Month": month,
            "Payment": round(monthly_payment + extra_monthly_payment, 2),
            "Principal Paid": round(principal_payment, 2),
            "Interest Paid": round(interest_payment, 2),
            "Remaining Balance": round(loan_balance, 2)
        })
        
        if loan_balance <= 0:
            break
    
    return total_principal_paid, total_interest_paid, pd.DataFrame(amortization_schedule)

def main():
    parser = argparse.ArgumentParser(description="Auto Loan Calculator")
    parser.add_argument("--loan_balance", type=float, required=True, help="Specify the starting loan balance.")
    parser.add_argument("--months", type=int, required=True, help="Enter the loan term in months.")
    parser.add_argument("--interest_rate", type=float, required=True, help="Provide the annual interest rate as a percentage.")
    parser.add_argument("--additional_payment", type=float, default=0, help="Extra lump sum payment applied after the first month.")
    parser.add_argument("--extra_monthly_payment", type=float, default=0, help="Extra amount added to each monthly payment.")
    
    args = parser.parse_args()
    
    total_principal, total_interest, schedule = calculate_auto_loan(
        args.loan_balance, args.months, args.interest_rate, args.additional_payment, args.extra_monthly_payment)
    
    print(f"Total Principal Paid: ${total_principal:.2f}")
    print(f"Total Interest Paid: ${total_interest:.2f}")
    print("\nAmortization Schedule:")
    print(schedule)

if __name__ == "__main__":
    main()
