while True:
    f= float(input("Enter 1 to add, 2 to subtract, 3 to multiply, 4 to divide, or 0 to exit:"))
    if(f<0 or f>4):
        print("Invalid input! Please enter a valid option.")
        continue

    num1= float(input("Enter your first number:"))
    num2= float(input("Enter your second number:"))
    if(f==0):
        print("You have successfully exited the calculator")
        break
    if(f==1):
        print("Addition is:",num1+num2)
    elif(f==2):
        print("Difference is:",num1-num2)
    elif(f==3):
        print("Product is:",num1*num2)
    elif(f==4):
        if (num2==0):
            print("Cannot be divided by zero")
        else:
            print("Divided value is:",num1/num2)    
    