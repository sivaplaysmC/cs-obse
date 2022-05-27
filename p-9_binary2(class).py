#binary file operations
from os import remove,rename
file1="item.dat"
from pickle import load,dump
class item:

    #constructor called when creating an object of class
    def __init__(self,icode=0,name='',price=0.0,qty=0):
        self.icode=icode
        self.name=name
        self.price=price

    def Enteritem(self):
        self.icode=int(input("Enter item code:"))
        self.name=input("Enter name of item")
        self.price=float(input("Enter price for item"))
        self.qty=int(input("Enter the quantity:"))

    def display(self):

         print (self.icode,self.name,self.price,self.qty)

def itemsearch():
    if not file1:
        print ("FILE CONNOT BE OPENED")
    else:
        obj=open(file1,'rb')
        sitemcode=int(input("Enter the item code to search"))
    try:
        flag=0
        print("item details")
        while True:
            it=load(obj)
            icode=it.icode
            if(icode==sitemcode):
                it.display()
                flag=1
                break
    except EOFError:
        pass
    if(flag==0):
        print ("item codenot forund")
def itemupdate():
    obj=open(file1,"rb")
    temp=open("temp.dat",'wb')
    tcode=int(input("Enter the item code to be updated:"))
    flag=0
    try:
        while True:
            it=load(obj)
            if it.icode==tcode:
                print ("item details are:")
                it.display()
                it.name=input("Enter the new name:")
                it.price=int(input("Enter the new price:"))
                it.qty=int(input("Enter the new quantity"))

                dump(it,temp)
                flag=1
            else:
                dump(it,temp)
    except EOFError:
        pass

    if(flag==0):
        print ("no such item present")

    obj.close()
    temp.close()
    remove("item.dat")
    rename("temp.dat","item.dat")

#________MAIN ENVIRONMENT________

while True:
    print ("1.Enter data")
    print ("2.Display data")
    print ("3.Search data")
    print ("4.Update data")
    print ("5.Exit")
    ch=0
    ch=int(input("Enter your choice : "))
    if(ch==1):
        iobj=open(file1,'ab+')
        if not iobj:
            print ( file1,"cannot be created")
        else:
            it=item(0,None,0,0)
        ch1='y'
        while ch1=='y':
            it.Enteritem()
            dump(it,iobj)
            ch=input("Do youwant to continue:y/n")
            if(ch=='n'):
                break
        iobj.close()

    elif(ch==2):
        iobj=open(file1,'rb')
        try:
            print ("item details")
            while True:
                it=load(iobj)
                it.display()
        except EOFError:
            pass
        iobj.close()

    elif(ch==3):
        itemsearch()

    elif(ch==4):

        itemupdate()
    elif(ch==5):

        print ("Program over…!!!")
        break
    else:
        print("Invalid 


