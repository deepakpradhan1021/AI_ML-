current_balance=int(input("Enter your current balance: "))
withdrawal_amount=int(input("Enter the amount to withdraw: "))
if  current_balance >= withdrawal_amount:
    current_balance -= withdrawal_amount
    print(f"Withdrawal successful. Your new balance is: {current_balance}")
else:
    print("Insufficient balance. Withdrawal failed.")
    