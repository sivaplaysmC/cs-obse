def fact(n):
    fact = 1
    i = 1
    while i<=n:
        fact = fact*i
        i = i + 1
    return fact
def fibo(n):
    f1 = -1
    f2 = 1
    for i in range(n):
        f3=f1+f2
        print(f3)
        f1,f2=f2,f3
print("1.Factorial \n2.Fibonacii series")
ch="y"
while ch.lower()=="y":
    c=int(input("Enter your choice:"))
    if c==1:
        num = int(input("Enter the number for calculating factorial: "))
        print("The factorial of ",num,"=",fact(num))
    elif c == 2:
        num = int(input('Enter the number of terms to display the fibonacii series: '))
        print("Fibonacci series")
        fibo(num)
    else:
        print('Enter a valid option from the menu!!! (1 or 2 )')
    ch = input('Do you want to continue ?[y/n]')  
else:
    print("Completed...")
