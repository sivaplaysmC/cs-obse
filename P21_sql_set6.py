import mysql.connector as s
mc=s.connect(host='localhost',user='root',passwd='',database='board_exam')
if mc.is_connected()==False:
    print("Error...")
cr=mc.cursor()

sql="""create table if not exists ITEMS(
ItemNo integer not null primary key,
Name varchar(25) not null,
Dcode integer,
Qty integer,
UnitPrice integer,
StockDate date);"""
cr.execute(sql)
mc.commit()
print("Table Created....")

def insertion():
    itemno=int(input("Enter the item no:"))
    name=input("Enter the item name:")
    dcode=int(input("Enter dcode:"))
    qty=int(input("Enter the quantity:"))
    unitprice=int(input("Enter the unitprice:"))
    sd=input("Enter the stock date:")
    sql="insert into ITEMS values({},'{}',{},{},{},'{}')".format(itemno,name,dcode,qty,unitprice,sd)
    cr.execute(sql)
    mc.commit()
    print("Record inserted....")
    
def query1():
    sql="select Name from ITEMS where year(StockDate)=2010;"
    cr.execute(sql)
    data=cr.fetchall()
    flag=False
    for i in data:
        print(i)
        flag=True
    if flag==False:
        print("No record found")
def query2():
    sql="select ItemNo,Name from ITEMS where UnitPrice>10;"
    cr.execute(sql)
    data=cr.fetchall()
    flag=False
    for i in data:
        print(i)
        flag=True
    if flag==False:
        print("No record found")
def query3():
    sql="select sum(Qty),Dcode from ITEMS group by Dcode;"
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
