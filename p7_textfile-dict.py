# PROGRAM: To create a Dictionary of term and its definition with text files
filename="dictionary.txt"
dictionary={}

fout=open("dictionary.txt",'w')
term=input("Enter term:")
term=term.rstrip()
if term not in dictionary:
    definition=input("enter definition")
    dictionary[term]=definition
    store=open(filename,'w')
    for term,definition in dictionary.items():
        store.write(term+'\n')
        store.write(definition+'\n')
    store.close()
    print ("Added")    
fout.close()

choice=1
while choice!=0:
    print( """
0-Quit
1-Lookup
2-Add new word & definition
3-Modify
4-Delete
5-Create a new dictionary with selected words""")
    choice=int(input("Enter your choice"))
    if choice==0:
        print("Program terminated!")
        break
    elif choice==1:
        find=input("Enter term to be searched for:")
        find=find.rstrip()
        if find in dictionary:
            print (dictionary[find])
        else:
            print ("term not found")
    elif choice==2:
        term=input("Enter term:")
        term=term.rstrip()
        if term not in dictionary:
            definition=input("enter definition")
            dictionary[term]=definition
            store=open(filename,'w')
            for term,definition in dictionary.items():
                store.write(term+'\n')
                store.write(definition+'\n')
            store.close()
            print ("Added")
        else:
            print("Term is already present in the dictionary")
    elif choice==3:
        term=input("Enter the term to be Updated;")
        term=term.rstrip()
        if term in dictionary:
            definition=input("Enter the new definition:")
            dictionary[term]=definition
            store=open(filename,'w')
            for term,definition in dictionary.items():
                store.write(term+'\n')
                store.write(definition+'\n')
            store.close()
            print ("Updated")
        else:
            print ("Term does not exists")

    elif choice==4:
        term=input("Enter the term to be deleted:")
        term=term.rstrip()
        if term in dictionary:
            del dictionary[term]
            store=open(filename,'w')
            for term,definition in dictionary.items():
                store.write(term+'\n')
                store.write(definition+'\n')
            store.close()
            print ("Deleted")
        else:
            print ("Term does not exists")
    elif choice==5:
        newdictionary={}
        find=input("Enter term to be added to new file:")
        find=find.rstrip()
        if find in dictionary:
            newdictionary[find]=dictionary[find]
        else:
            print ("term not found")
        newstore=open("newfile.txt",'a+')
        for term,definition in newdictionary.items():
            newstore.write(term+'\n')
            newstore.write(definition+'\n')
        newstore.close()
        newstore=open("newfile.txt",'r')
        check=newstore.read()
        print("Printing from the new file")
        print(check)       
        
    else:
        print ("Wrong choice")


