#main module
import arithmetic

x="y"
while(x=="y" or x=="Y"):
    n1=int(input("Enter the first number"))
    n2=int(input("Enter the second number"))
    op=input("Enter any one of the operator(+,-,*,/,//,%)")
    if op=="+":
        print("Sum=",arithmetic.add(n1,n2))
    elif op=="-":
        print("Difference=",arithmetic.sub(n1,n2))
    elif op=="*":
        print("Product=",arithmetic.mul(n1,n2))
    elif op=="/" or op=="//" or op=="%":
        if n2==0:
            print("Please enter the value than 0")
        else:
            if op=="/":
                print("Division=",arithmetic.div(n1,n2))
            elif op=="//":
                print("Floor division=",arithmetic.f_div(n1,n2))
            else:
                print("Remainder=",arithmetic.mod(n1,n2))
    else:
        print("Invalid operator")
    x=input("Do you want to continue?[y/n] ")
else:
    print("Completed...")

