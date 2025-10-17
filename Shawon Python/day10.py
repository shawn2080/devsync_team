try:
    age = int(input("Enter your age: "))
    if age >= 18:
        print("you are an adult")
    else:
        print("you are kid")
except ValueError:
    print("Invaild number!.Please inter your age.")            

hello 