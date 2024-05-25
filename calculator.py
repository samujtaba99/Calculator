while True:
    operation= int(input("Enter 1 to add, 2 to subtract, 3 to multiply, 4 to divide, or 0 to exit : "))
    
    if(operation<0 or operation>4):
        print("Invalid input! Please enter a valid option.")
        continue

    num1= float(input("Enter your first number : "))
    num2= float(input("Enter your second number : "))
    if(operation==0):
        print("You have successfully exited the calculator")
        break
    if(operation==1):
        print("Addition is : ",num1+num2)
    elif(operation==2):
        print("Difference is : ",num1-num2)
    elif(operation==3):
        print("Product is : ",num1*num2)
    elif(operation==4):
        if (num2==0):
            while (num2==0):
                print("Cannot be divided by zero")
                num2= float(input("Enter second number again : "))
                if (num2>0):
                    print("Divided value is:",num1/num2)     
        elif num2>0:
            print("Divided value is:",num1/num2)    
    