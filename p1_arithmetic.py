n1=int(input("Enter the first number"))
n2=int(input("Enter the second number"))
x="y"
while(x=="y" or x=="Y"):
    op=input("Enter any one of the operator(+,-,*,/,//,%)")
    if op=="+":
        print("Sum=",n1+n2)
    elif op=="-":
        print("Difference=",n1-n2)
    elif op=="*":
        print("Product=",n1*n2)
    elif op=="/" or op=="//" or op=="%":
        if n2==0:
            print("Please enter the value than 0")
        else:
            if op=="/":
                print("Division=",n1/n2)
            elif op=="//":
                print("Floor division=",n1//n2)
            else:
                print("Remainder=",n1%n2)
    else:
        print("Invalid operator")
    x=input("Do you want to continue?[y/n] ")
else:
    print("Completed...")
