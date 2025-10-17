blance= 100000
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
            print("\n Options:\n1. Chack Blance\n2. Withdeaw money")
            choice = input("choose 1 or 2 : ")
            if choice == "1":
                print(f"your current balance is:{blance} Taka")
            elif choice == "2":
                try:
                    amount = int(input("Enter the amount to withdraw: "))
                    if amount % 500 != 0:
                        print("You can only withdraw in multipels of 500.")
                    elif amount > blance:
                        print("Insufficient  blance.")
                    elif amount > TRANSAICATION_LIMIT:
                        print(f"you can withdraw a maximum of {TRANSAICATION_LIMIT} Taka per transacion.")
                    elif daily_limit_used+ amount > DAILY_LIMIT:
                        print(f"daily limit exceded, you can withdeaw only {DAILY_LIMIT - daily_limit_used} Taka today.")
                    else:
                        notes = amount // 500
                        blance -= amount
                        daily_limit_used += amount
                        print(f"please collect your cash:{notes} notes of 500 Taka.")
                        print(f"Remaining balnce: {blance} Taka.")
                except ValueError:
                    print("Invaild amount . Please enter a vaild number.")
            else:
                print("Invaild option selected.")
            print("Transaction compleate. Please take your card.")
            break
        else:
            print("Incorrect PIN.")
            if attempt == 2:
                print("Too many incorrect attempt. card blocked for security reasons.")                            