import mysql.connector as s
mc=s.connect(host='localhost',user='root',passwd='',database='board_exam')
if mc.is_connected()==False:
    print("Error...")
cr=mc.cursor()

sql="""create table if not exists STUDENTS(
RollNo integer not null primary key,
Name varchar(25) not null,
Class varchar(25),
DOB date,
Gender char,
City varchar(25),
Marks integer);"""
cr.execute(sql)
mc.commit()
print("Table Created....")

def insertion():
    rno=int(input("Enter the roll no:"))
    name=input("Enter the student name:")
    cl=input("Enter the class:")
    dob=input("Enter date of birth:")
    gender=input("Enter the gender:")
    city=input("Enter the city:")
    marks=int(input("enter the marks:"))
    sql="insert into STUDENTS values({},'{}','{}','{}','{}','{}',{})".format(rno,name,cl,dob,gender,city,marks)
    cr.execute(sql)
    mc.commit()
    print("Record inserted....")
    
def query1():
    sql="select * from STUDENTS  order by Name;"
    cr.execute(sql)
    data=cr.fetchall()
    flag=False
    for i in data:
        print(i)
        flag=True
    if flag==False:
        print("No record found")
def query2():
    sql="select Name,Class,DOB,City from STUDENTS where Marks between 450 and 551;"
    cr.execute(sql)
    data=cr.fetchall()
    flag=False
    for i in data:
        print(i)
        flag=True
    if flag==False:
        print("No record found")
def query3():
    sql="select max(Marks) from STUDENTS;"
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
