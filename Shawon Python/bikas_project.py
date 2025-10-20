balnce = 20000
DAIL = "4321"
correct_pin = "1234"
bikas = input("Enter Your Dail Number: ")
if bikas != DAIL:
    print("Sorry You Are Wrong Digit Dail.\nPlease Try Again.")
else:
    while True:
        print("Chose Option\n1.Chack Balnce\n2.Send Money\n3.Withdraw Money\n0.Back")
        chose = input("Enter Your Chose Option: ")
        if chose == "0":
            print("Thank You!")
            break
        elif chose == "1":
             pin = input("Enter Your PIN: ")
             if pin != correct_pin:
                  print("Incorrect PIN!")
             elif pin == correct_pin:    
                print(f"Your Corrent Balnce is {balnce} Taka.")
                print("0.Back")
                back = input("Dail 0 To Back: ")
                if back == "0":
                    continue
                else:
                    print("Incorrect.Thank You!")
                    break
        elif chose == "2":
                send = input("Enter Your Mobile Number: ")
                if send == send:
                    amount = int(input("Enter Your Amount: "))
                    if amount >= balnce:
                        print("Insufficient Balnce!")
                    elif amount <= balnce:
                         pin2 = input("Enter Your PIN: ")
                         if pin2 != correct_pin:
                              print("Incorrect Password!")
                         elif pin2 == correct_pin:
                              print("Send Money Succesfull.")
                              print(f"Send Money Number: {send}")
                              tottal = balnce - amount
                              print(f"Your Tottal Balnce Is:{tottal}")
                              print("THANK YOU!")
                              
                       
