balance = 100000
correct_pin = "1234"
daily_limit_used = 0
DAILY_LIMIT = 50000
TRANSAICATION_LIMIT = 20000
print("Please insert your card(type 'insert'): ")
card = input(">> ").lower()
if card != "insert":
    print("card not inserted properly,please try again.")
else:
    for attempt in range (3):
        pin = input("Enter your 4-digit PIN number: ")
        if pin == correct_pin:
            print("PIN verified successfully.")
            print("\n Options:\n1. Check Balance\n2. Withdraw money")
            choice = input("choose 1 or 2: ")
            if choice == "1":
                print(f"your current balance is:{balance} Taka")
            elif choice == "2":
                try:
                    amount = int(input("Enter the amount to withdraw: "))
                    if amount % 500 != 0:
                         print("You can only withdraw in multiples of 500.")
                    elif amount > balance:
                         print(" Insufficient balance.")
                    elif amount > TRANSAICATION_LIMIT :
                         print(f"You can withdraw  a maximum of {TRANSAICATION_LIMIT} Taka per transaction.")
                    elif daily_limit_used + amount > DAILY_LIMIT:
                         print(f"daily limit exceeded, you can withdraw only {DAILY_LIMIT - daily_limit_used} Taka today.")
                    else:
                         notes = amount // 500
                         balance -= amount
                         daily_limit_used += amount
                         print(f"Please collect your cash:{notes} notes of 500 Taka.")
                         print(f"Remaining balance: {balance} Taka.")
                except ValueError:
                    print("Invaild amount. Please enter a valid number.")
            else:
                print("Ivaild option selected.")
            print("Transaction completed. Please take your card.")
            break
        else:
            print("Incorrect PIN.")
            if attempt == 2:
                print("Too many incorrect attempts. Card blocked for security reasons.")                   


                    
