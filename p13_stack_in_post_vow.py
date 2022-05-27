OPERATORS = set(['+', '-', '*', '/', '(', ')', '^'])  # set of operators
PRIORITY = {'+':1, '-':1, '*':2, '/':2, '^':3} # dictionary having priorities 
 
def infix_to_postfix(expression): 
    stack = [] 	# initially stack empty
    output = '' # initially output empty
    for ch in expression:
        if ch not in OPERATORS:  
            output+= ch
        elif ch=='(':  
            stack.append('(')
        elif ch==')':
            while stack and stack[-1]!= '(':
                output+=stack.pop()
            stack.pop()
        else:
            while stack and stack[-1]!='(' and PRIORITY[ch]<=PRIORITY[stack[-1]]:
                output+=stack.pop()
            stack.append(ch)
    while stack:
        output+=stack.pop()
    return output
def vow_stk(word):
    vowels =['a','e','i','o','u']
    Stack = []
    for letter in word:
        if letter in vowels:
            if letter not in Stack:
                Stack.append(letter)
    return Stack
    #print(Stack)

ch="y"
while ch=="y" or ch=="Y":
    print("1.Conver Infix expression to  Postfix expression")
    print("2.Creation of vowel stack")
    op=int(input("Enter your choice:"))
    if op==1:
        print(OPERATORS)
        expression = input('Enter infix expression..... having the above operators alone')
        print('infix expression: ',expression)
        print('postfix expression: ',infix_to_postfix(expression))
    elif op==2:
        word = input("Enter the word to search for vowels :")
        result=vow_stk(word.lower())
        print("The number of different vowels present in",word,"is",len(result))
    else:
        print("Invalid option!!!")
    ch=input("Do you want to continue?Y/N   ")
