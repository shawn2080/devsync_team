balnce = 30000
correct_pin = "1234"
DAIL = "4321"
Bikas = input("Enter a dail number: ")
if Bikas != DAIL:
    print("sorry you wrong digit dail!")
else:
    print("Choice:\n1.chack balnce\n2.send money\n3.cash out\n")
    choice = input(">> ")
    if choice == "1":
        print(f"Your current balnce is {balnce} Taka")
        choice2 = input()
    elif choice == "2":
            try:
                number = input("Enter your mobile number.")
                if number == number:
                    print("Enter your amount")
                    amount = int(input())
                    if amount >= balnce:
                        print("Insufficient balnce.\nTry again!")
                    elif amount <= balnce:
                        print("send money succesfull.\nTHANK YOU!")
                        print(f"send money number:{number}")
                        minas = balnce-amount
                        print(f"tottal balnce: {minas} Taka")
            except ValueError:
                print("Inviald number")