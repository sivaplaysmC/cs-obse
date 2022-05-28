import mysql.connector as s
mc=s.connect(host='localhost',user='root',passwd='',database='board_exam')
if mc.is_connected()==False:
    print("Error...")
cr=mc.cursor()

sql="""create table if not exists CARDEN(
Ccode integer not null primary key,
CarName varchar(25) not null,
Make varchar(25),
Color varchar(10),
Capacity integer,
Charges integer);"""
cr.execute(sql)
mc.commit()
print("Table Created....")

def insertion():
    ccode=int(input("Enter the ccode:"))
    cname=input("Enter the car name:")
    make=input("Enter make:")
    color=input("Enter color:")
    capacity=int(input("Enter the capacity:"))
    charges=int(input("Enter the charges:"))
    sql="insert into CARDEN values({},'{}','{}','{}',{},{})".format(ccode,cname,make,color,capacity,charges)
    cr.execute(sql)
    mc.commit()
    print("Record inserted....")
    
def query1():
    sql="select CarName from CARDEN where Color='SILVER';"
    cr.execute(sql)
    data=cr.fetchall()
    flag=False
    for i in data:
        print(i)
        flag=True
    if flag==False:
        print("No record found")
def query2():
    sql="update CARDEN set charges=charges+10 where capacity>3;"
    cr.execute(sql)
    print("Record updated!")
    sql="select * from CARDEN;"
    cr.execute(sql)
    data=cr.fetchall()
    flag=False
    for i in data:
        print(i)
        flag=True
    if flag==False:
        print("No record found")
def query3():
    sql="select CarName,Capacity from CARDEN order by Capacity desc;"
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
