balance = 100000
correct_pin = "1234"
daily_limit_used = 0
DAILY_LIMIT = 50000
TRANSACTION_LIMIT = 20000
print ("Please insert your card(type 'insert'):")
card = input(">> ").lower()
if card != "insert":
     print("Card not inserted properly,Please try again.")
else:
     for attempt in range (3):
          pin = input("Enter your 4-digit PIN number: ")
          if pin == correct_pin:
               print("PIN verified.")
               print("\n Option:\n1. Check Balance\n2. Withdraw money")
               choice = input("choose 1 or 2: ")
               if choice == "1":
                    print(f"Your current balance is : {balance} Taka.")
                    print(f"Today's used limit : {daily_limit_used}/{DAILY_LIMIT}")
               elif choice == "2":
                    try:
                         amount = int(input("Enter amount to withdraw: "))
                         if amount % 500 != 0:
                              print("You can withdraw in multiples of 500.")
                         elif amount > balance:
                              print("Insufficient balance.")
                         elif amount > TRANSACTION_LIMIT :
                              print(f"You can withdraw a maximum of {TRANSACTION_LIMIT} Taka per transaction.")
                         elif daily_limit_used + amount > DAILY_LIMIT:
                              print (f"Daily limit exceeded. You can withdraw only {DAILY_LIMIT - daily_limit_used}Taka more today.")
                         else:
                              notes = amount// 500
                              balance -= amount
                              daily_limit_used += amount
                              print(f"Please collect your cash:{notes} notes of 500 taka.")
                              print(f"Remaining balance: {balance} Taka.")
                              print(f"Total withdraw today: {daily_limit_used}/{DAILY_LIMIT}")
                    except ValueError:
                         print("Invaild amount. Please enter a number.")
               else:
                    print("Invaild option selected.")
               print("Transation complete. Please take your card.")
               break
          else:
               print("Incorrect PIN.")
               if attempt == 2:
                    print("card blocked after 3 incorrect attempts.")
                              