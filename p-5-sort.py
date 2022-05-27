def bSort(L):
    n = len(L)
    for i in range(0, n-1):
        for j in range(0, n-i-1):
            if L[j] < L[j+1]:
                L[j], L[j+1] = L[j+1],L[j]

def sSort(L):
    n = len(L)
    for i in range(0, n-1):
        for j in range(i+1, n):
            if L[i].upper() > L[j].upper():
                L[i], L[j] = L[j], L[i]
def iSort(L):
    n = len(L)
    for k in range(1, n):
        temp = L[k]
        locp = k - 1
        while L[locp]>temp and locp>=0:
            L[locp+1] = L[locp]
            locp = locp - 1
            L[locp+1]=temp

#	--------------------- main environment -------------------------
print('''1.Bubble Sort
2.Selection Sort
3.Insertion Sort''')
ch = 'y'
while ch.lower() == 'y':
    c = int(input('Enter your choice:'))
    if c == 1:
        L = list()
        for i in range(7):
            number = int(input('Enter number : '))
            L.append(number)
        bSort(L)
        print("***Descending order of numbers using bubble sort with python***")
        print('Sorted list:',L)
    elif c == 2:
        L = list()
        for i in range(7):
            name =input('Enter name : ')
            L.append(name)
        sSort(L)
        print("***Ascending order of names using selection sort with python***")
        print('Sorted list:',L)
    elif c == 3:
        L=[]
        for i in range(7):
            number = int(input('Enter number : '))
            L.append(number)
        iSort(L)
        print("***Ascending order of numbers using insertion sort with python***")
        print('Sorted list:',L)
    else:
        print('Enter a valid option from the menu!!! (1 or 2 or 3)')
    ch = input('Do you want to continue ?[y/n]')
else:
    print("Completed.....")
