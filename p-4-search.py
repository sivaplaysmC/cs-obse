def lSearch(L, key):
    i= 0
    n = len(L)
    found = False
    while (i < n) and (not found):
        if L[i] == key:
            found = True
        else:
            i = i + 1
    if found:
            print('Data',key,'found at','position',i+1)
    else:
        print('Data',key,'not found')
def bSearch(L, key):
    low = 0
    high = len(L)-1
    found = False
    while (low <= high) and (not found):
        mid = (low+high)//2

        if L[mid] == key:
            found = True
        elif L[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    if found:
        print('Data',key,'found at','position',mid+1)
    else:
        print('Data',key,'not found')
print('''1.Perform Linear Search
2.Perform Binary Search''')
ch = 'y'
while ch.lower() == 'y':
    c = int(input('Enter your choice:'))
    if c == 1:
        L = list()
        for i in range(7):
            fruit = input('Enter fruit name : ')
            L.append(fruit)
        x = input('\nEnter data to be searched : ')
        lSearch(L, x)
  
    elif c == 2:
        L = list()
        print('Ensure the input is in ascending order')
        for i in range(7):
            number = int(input('Enter number : '))
            L.append(number)
        x = int(input('\nEnter number to be searched : '))
        bSearch(L, x)    
    
    else:
        print('Enter a valid option from the menu!!! (1 or 2 )')
    ch = input('Do you want to continue ?[y/n]')
else:
    print("Completed.....")

