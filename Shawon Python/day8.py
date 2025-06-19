try:
    age = int(input("Enter your age: "))
    if age >= 18:
        print("You are adult.")
        print("WELCOME")
    elif age >= 14:
        print("You are an teenger.")
    else:
        print("You are a kid.")
except ValueError:
    print("Invaild number.Please Enter your age.")