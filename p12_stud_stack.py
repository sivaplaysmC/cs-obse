def isempty(stk):
    if stk==[]:
        return True
    else:
        return False

def push(stk):
    
    roll=int(input("Enter the rollno::"))
    name=input("Enter the name::")
    stk.append([roll,name])
    top=len(stk)-1
    print ("element:",stk[top],"inserted successfully")
    print("the stack after insertion")
    print(stk)

    

def pop(stk):
    if isempty(stk):
        return "underflow"
    else:
        item=stk.pop()
        if len(stk)==0:
            top=None
        else:
            top=len(stk)-1
        return item

def peek(stk):
    if isempty(stk):
        return "underflow"
    else:
        top=len(stk)-1
        return stk[top]

def display(stk):
    if isempty(stk):
        print("stack empty")
    else:
        top=len(stk)-1
        print(stk[top],"<-top")
        for a in range(top-1,-1,-1):
            print(stk[a])
            
stack=[]
top=None
print(
"""
STACK OPERATIONS
1.Insert a student detail into stack
2.Remove a student detail from stack
3.Display the top most element on the stack
4.Display the contents of stack
5 EXIT
""")
while True:
    ch=int(input("Enter your choice(1-5):"))
    if ch==1:
        push(stack)
    elif ch==2:
        item=pop(stack)
        if item=="underflow":
           print("underflow...!  stack is empty")
        else:
           print("popped item is",item)
    elif ch==3:
        item=peek(stack)
        if item=="underflow":
           print("underflow...!  stack is empty")
        else:
           print("Topmost item is",item)
    elif ch==4:
        display(stack)
    elif ch==5:
        break
    else:
        print("invalid choice")




