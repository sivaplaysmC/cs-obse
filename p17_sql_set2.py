import mysql.connector as s
mc=s.connect(host='localhost',user='root',passwd='',database='board_exam')
if mc.is_connected()==False:
    print("Error...")
cr=mc.cursor()

sql="""create table if not exists SPORTS(
Stud_no int not null primary key,
Class int not null,
name varchar(25),
game1 varchar(30),
grade1 varchar(5));"""
cr.execute(sql)
mc.commit()
print("Table Created....")

def insertion():
    Stud_no=int(input("Enter the student no:"))
    Class=int(input("Enter the class:"))
    name=input("Enter name:")
    game1=input("Enter game name:")
    grade1=input("Enter grade:")
    sql="insert into SPORTS values({},{},'{}','{}','{}')".format(Stud_no,Class,name,game1,grade1)
    cr.execute(sql)
    mc.commit()
    print("Record inserted....")
    
def query1():
    sql="Select name from SPORTS where game1='swimming';"
    cr.execute(sql)
    data=cr.fetchall()
    flag=False
    for i in data:
        print(i)
        flag=True
    if flag==False:
        print("No record found")
def query2():
    sql="Delete from SPORTS where class=10;"
    cr.execute(sql)
    print("The new record is:")
    sql="select * from SPORTS;"
    cr.execute(sql)
    data=cr.fetchall()
    flag=False
    for i in data:
        print(i)
        flag=True
    if flag==False:
        print("No record found")
def query3():
    sql="Select count(*) , class from SPORTS group by class;"
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
