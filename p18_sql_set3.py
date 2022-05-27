import mysql.connector as s
mc=s.connect(host='localhost',user='root',passwd='',database='board_exam')
if mc.is_connected()==False:
    print("Error...")
cr=mc.cursor()

sql="""create table if not exists ORDERS(
OderId integer not null primary key,
PName varchar(25) not null,
Quantity integer,
Rate integer,
Sale_Date date,
Discount integer);"""
cr.execute(sql)
mc.commit()
print("Table Created....")

def insertion():
    oderid=int(input("Enter the order id:"))
    pname=input("Enter the product name:")
    qty=int(input("Enter the quantity:"))
    rate=int(input("Enter rate:"))
    sd=input("Enter the sale date:")
    dis=int(input("Enter discount amount:"))
    sql="insert into ORDERS values({},'{}',{},{},'{}',{})".format(oderid,pname,qty,rate,sd,dis)
    cr.execute(sql)
    mc.commit()
    print("Record inserted....")
    
def query1():
    sql="select PName,Quantity,Rate from ORDERS where PName in ('Pen','Pencil');"
    cr.execute(sql)
    data=cr.fetchall()
    flag=False
    for i in data:
        print(i)
        flag=True
    if flag==False:
        print("No record found")
def query2():
    sql="select * from ORDERS where Discount IS NULL;"
    cr.execute(sql)
    data=cr.fetchall()
    flag=False
    for i in data:
        print(i)
        flag=True
    if flag==False:
        print("No record found")
def query3():
    sql="update ORDERS set Rate=Rate+(5/100)*Rate;"
    cr.execute(sql)
    sql="select * from ORDERS;"
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
