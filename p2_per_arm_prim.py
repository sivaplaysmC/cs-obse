def perfectnum(n):
    divsum = 0
    mid = int(n)//2
    for i in range(1,mid+1):
        if n%i == 0:
            divsum+=i
    if divsum == n:
        print('The number {} is a perfect number'.format(n))
    else:
         print('The number {} is not a perfect number'.format(n))
def armstrongnum(n):
    n1 = n
    cubsum = 0
    while(n1>0):
        x = n1 % 10;
        cubsum = cubsum + (x* x * x)
        n1 = int (n1/ 10)
    if cubsum == n:
        print('The number {} is an Armstrong Number'.format(n))
    else:
        print('The number {} is not an Armstrong Number'.format(n))
def primenum(n):
    mid = int(n)//2
    for i in range(2,mid+1):
        if n%i == 0:
            print('The number {} is not a prime number'.format(n))
            break
    else:
        print('The number {} is a prime number'.format(n))
print('''1.Check Perfect Number
2.Check Armstrong number
3.Check Prime Number''')
ch = 'y'
while ch.lower() == 'y':
    c = int(input('Enter your choice:'))
    if c == 1:
        num = int(input('Enter the number for checking Perfect number:'))
        perfectnum(num)        
    elif c == 2:
         num = int(input('Enter the number for checking Armstrong number:'))
         armstrongnum(num)
    elif c == 3:
        num = int(input('Enter the number for checking the Prime number:'))
        primenum(num)
    else:
        print('Enter a valid option from the menu!!! (1 or 2 or 3)')
    ch = input('Do you want to continue ?[y/n]')
else:
    print("Completed.....")
