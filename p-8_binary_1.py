import pickle
def insert_rec():
    rno=int(input("Enter the roll number:"))
    name=input("Enter the name:")
    mark=int(input("Enter the mark:"))
    rec={"Rollno":rno,"Name":name,"Mark":mark}
    f=open("student.dat","ab")
    pickle.dump(rec,f)
    print("Record inserted.....")
    f.close()
def read_rec():
    f=open("student.dat","rb")
    while True:
        try:
            rec=pickle.load(f)
            print(rec)
            print("Roll no:",rec["Rollno"])
            print("Name   :",rec["Name"])
            print("Marks  :",rec["Mark"])
        except EOFError:
            break
    f.close()
def search_rec():
    n=int(input("Enter the roll no to be searched"))
    f=open("student.dat","rb")
    flag=False
    while True:
        try:
            rec=pickle.load(f)
            if rec["Rollno"]==n:
                print("Roll no:",rec["Rollno"])
                print("Name   :",rec["Name"])
                print("Marks  :",rec["Mark"])
                flag=True
        except EOFError:
            break
    if flag==False:
        print("Record not found.....")
    f.close()
def update_rec():
    r=int(input("Enter the roll no to be searched for updation:"))
    m=int(input("Enter the mark to be updated:"))
    f=open("student.dat","rb")
    temp_list=[]
    while True:
        try:
            rec=pickle.load(f)
            temp_list.append(rec)
        except EOFError:
            break
    f.close()
    flag=False
    for rec in temp_list:
        if rec["Rollno"]==r:
            rec["Mark"]=m
            print("Record updated.....")
            flag=True
    if flag==False:
        print("Record not found....")
    f=open("student.dat","wb")
    for rec in temp_list:
        pickle.dump(rec,f)
    f.close()
def delete_rec():
    r=int(input("Enter the roll o to be deleted:"))
    f=open("student.dat","rb")
    temp_list=[]
    while True:
        try:
            rec=pickle.load(f)
            temp_list.append(rec)
        except EOFError:
            break
    f.close()
    flag=False
    f=open("student.dat","wb")
    for rec in temp_list:
        if rec["Rollno"]==r:
            print("Record deleted....")
            flag=True
            continue
        pickle.dump(rec,f)
    if flag==False:
        print("Record not found.....")
    f.close()

    
while True:
    print("-----------------------------------------")
    print(" 1.Insert record")
    print(" 2.Display record")
    print(" 3.Search record")
    print(" 4.Update record")
    print(" 5.Delete record")
    print(" 6.Exit")
    print("-----------------------------------------")
    ch=0
    ch=int(input("Enter your choice : "))
    if(ch==1):
        insert_rec()            
    elif(ch==2):
        read_rec()
    elif(ch==3):
        search_rec()
    elif(ch==4):
        update_rec()      
    elif(ch==5):
        delete_rec()
    elif(ch==6):
        print("Thank You.....")
        break
    else:
        print ("Invalid option.....")
        break


