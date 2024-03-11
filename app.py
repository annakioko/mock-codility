def Transactions(A, D):
    Annual_income = sum(amount for amount in A if amount > 0)
    Annual_expenses = sum(amount for amount in A if amount < 0)

    months = set(date.split('-')[1] for date in D)
    total_months = len(months)

    if total_months > 1:
        total_months_with_fees = total_months - 1

        monthly_fee = 5
        total_fees = total_months_with_fees * monthly_fee

        for month in months: 
            month_transactions = [A[x] for x, date in enumerate(D) if date.split('-')[1] == month]
            card_payments = sum(amount for amount in month_transactions if amount < 0)

            if card_payments <= -100:
                total_fees -= monthly_fee
    else:
        total_months_with_fees = 0
        total_fees = 0 

    final_balance = Annual_income - Annual_expenses - total_fees

    return final_balance


A = [100, 100, 100, -10]
D = ['2020-12-31', '2020-12-22', '2020-12-03', '2020-12-29']
print(Transactions(A, D))



