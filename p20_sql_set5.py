import mysql.connector as s
mc=s.connect(host='localhost',user='root',passwd='',database='board_exam')
if mc.is_connected()==False:
    print("Error...")
cr=mc.cursor()

sql="""create table if not exists EMPLOYEE(
Fcode varchar(25) not null primary key,
Fname varchar(30) not null,
sex  varchar(25),
salary float,
subject varchar(56)
joindate date);"""
cr.execute(sql)
mc.commit()
print("Table Created....")

def insertion():
    Fcode=input("Enter the employee code:")
    Fname=input("Enter the employee name:")
    sex=input("Enter sex:")
    salary=float(input("Enter salary:"))
    subject=input("Enter subject name:")
    joindate=input("Enter date:")
    sql="insert into EMPLOYEE values('{}','{}','{}',{},'{}','{}')".format(Fcode,Fname,sex,salary,subject,joindate)
    cr.execute(sql)
    mc.commit()
    print("Record inserted....")
    
def query1():
    sql="Select Fcode, Fname, joindate,salary from EMPLOYEE order by salary desc;"
    cr.execute(sql)
    data=cr.fetchall()
    flag=False
    for i in data:
        print(i)
        flag=True
    if flag==False:
        print("No record found")
def query2():
    sql="Update EMPLOYEE set salary=salary + 2000 where subject =’programming’ or subject=’maths’;"
    cr.execute(sql)
    print("Record updated!")
    sql="select * from EMPLOYEE;"
    cr.execute(sql)
    data=cr.fetchall()
    flag=False
    for i in data:
        print(i)
        flag=True
    if flag==False:
        print("No record found")
def query3():
    sql="select * from EMPLOYEE where fname like “%n”;"
    cr.execute(sql)
    data=cr.fetchall()
    flag=False
    for i in data:
        print(i)
        flag=True
    if flag==False:
        print("No record found")
print("""1.insert record
2.query1
3.query2
4.query3
5.Exit""")
while True:
    ch=int(input("Enter your choice:"))
    if ch==1:
        insertion()
    elif ch==2:
        query1()
    elif ch==3:
        query2()
    elif ch==4:
        query3()
    elif ch==5:
        break
    else:
        print("Invalid choice")
print("Thank You!")
