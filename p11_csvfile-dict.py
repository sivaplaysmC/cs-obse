import csv,operator
filename="testing.csv"
d=[
{"Cust_no":1,"Cust_name":"ARADHYA","Cust_Add":"26,1st street,Adambakkam"},
{"Cust_no":2,"Cust_name":"ARCHANA","Cust_Add":"17,2st street,Adambakkam"}
]
f=open(filename,'w',newline="")
my_writer=csv.DictWriter(f,fieldnames=["Cust_no","Cust_name","Cust_Add"])
my_writer.writeheader()
my_writer.writerows(d)
f.close()
def rec_search():
      cno=input("Enter customer number to be searched:")
      f=open(filename,"r")
      my_reader=csv.DictReader(f,fieldnames=["Cust_no","Cust_name","Cust_Add"])
      for rec in my_reader:
            if rec["Cust_no"]==cno:
                  print(rec)
                  break
      else:
            print ("Record not found.....")
      f.close()

def rec_add():
      f=open(filename,"r")
      my_reader=csv.DictReader(f,fieldnames=["Cust_no","Cust_name","Cust_Add"])
      cno=input("Enter the cutomer number:")
      for rec in my_reader:
            if rec["Cust_no"]==cno:
                  print("Existing record")
                  break
      else:
            cname=input("Enter the customer name:")
            cadd=input("Enter the customer address:")
            f=open(filename,"a",newline="")
            my_writer=csv.DictWriter(f,fieldnames=["Cust_no","Cust_name","Cust_Add"])
            my_writer.writerow({"Cust_no":cno,"Cust_name":cname,"Cust_Add":cadd})
            print("Record added.....")
            f.close()

def rec_update():
      cno=input("Enter the customer number to be Updated:")
      f=open(filename,"r")
      my_reader=csv.DictReader(f,fieldnames=["Cust_no","Cust_name","Cust_Add"])
      cus_list=list(my_reader)
      flag=0
      for  rec in cus_list:
            if rec["Cust_no"]==cno:
                  rec["Cust_Add"]=input("Enter the address to be updated:") 
                  print("Record Updated.....")
                  flag=1
                  break
      else:
            print ("Record not found....")          
      f.close()
      if flag==1:
            f=open(filename,"w",newline="")
            my_writer=csv.DictWriter(f,fieldnames=["Cust_no","Cust_name","Cust_Add"])
            my_writer.writerows(cus_list)
            f.close()

def rec_delete():
      cno=input("Enter the customer number to be deleted:")
      f=open(filename,"r")
      my_reader=csv.DictReader(f,fieldnames=["Cust_no","Cust_name","Cust_Add"])
      cus_list=[]
      flag=0
      for  rec in my_reader:
            if rec["Cust_no"]==cno:
                  flag=1
                  print ("Record Deleted....")
                  continue
            else:
                  cus_list.append(rec)
      f.close()
      if flag==0:
            print("Record not found....")
      else:
            f=open(filename,"w",newline="")
            my_writer=csv.DictWriter(f,fieldnames=["Cust_no","Cust_name","Cust_Add"])
            my_writer.writerows(cus_list)
            f.close()
def rec_display():
      f=open(filename,"r")
      my_reader=csv.DictReader(f,fieldnames=["Cust_no","Cust_name","Cust_Add"])
      next(my_reader)
      print("------------------customer records----------------------------------------------")
      for rec in my_reader:
            print(rec)
      print("--------------------------------------------------------------------------------")
      f.close()
      
def rec_sort():
      f=open(filename,"r")
      my_reader=csv.DictReader(f,fieldnames=["Cust_no","Cust_name","Cust_Add"])
      next(my_reader)
      sort_list=sorted(my_reader,key=operator.itemgetter("Cust_name"))
      print("The sorted records...")
      for i in sort_list:
            print(i)
      f.close()      

      
choice=1
while choice!=0:
      print( """
-----------Customer info management----------------
\t\t0-Quit
\t\t1-Search record
\t\t2-Add record
\t\t3-Modify record
\t\t4-Delete record
\t\t5-Display records
\t\t6-Sort records
---------------------------------------------------""")
      choice=int(input("Enter your choice:"))
      if choice==0:
            break
      elif choice==1:
            rec_search()  
      elif choice==2:
            rec_add()  
      elif choice==3:
            rec_update()
      elif choice==4:
            rec_delete()
      elif choice==5:
            rec_display()
      elif choice==6:
            rec_sort()
       
else:
    print ("Wrong choice")


