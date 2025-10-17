age = int(input("Enter your age: "))
if age >= 18:
    print("You are adult")
elif age >= 14:
    print("You are teenger")
else:
    print("You are an kid")


# try:
#     taka = int(input("Enter your amount: "))
#     if taka >= 10000:
#         print("You are very rich and you can withdrow.")
#     elif taka >= 1000:
#         print("You are mini rich and you can withdrow.")
#     elif taka >= 500:
#         print("alert withdrow.")
#     else:
#         print("please deposit money.")
# except ValueError:
#     print("Invalid input ,please enter your valid number.")



# try:
#     taka = int(input("Enter your amount: "))
#     if taka % 500 != 0 :
#         print("You can't withdraw.")
#     else:
#         print("Enter your pin.")
# except ValueError:
#     print("Invaild number.")
