# PROGRAM: Text File analysis
fout=open("poem.txt",'w')
s="""Our deepest fear is not that we are inadequate
Our deepest fear is that we are powerful beyond measure
It is our light, not our darkness
That most frightens us
We ask ourselves
Who am I to be brilliant, gorgeous, talented, fabulous?
Actually, who are you not to be?
You are a child of God."""
fout.write(s)
fout.close()
f=open("poem.txt",'r')
check=f.read()
print(check)
choice=0
while choice<=5:
    print("""1-Display the number of vowels
2. Display the number of consonants
3. Display the number of upper case characters
4. Display the number of lower case characters
5. Replacing spaces by # in each""")
    choice=int(input("Enter choice:"))
    if choice==1:
        v=0
        vowels=['a','e','i','o','u','A','E','O','I','U']
        for ch in check:
            if ch in vowels:
                v=v+1
        print("vowel count=",v)
    elif choice==2:
        c=0
        consonants="bcdfghjklmnpqrstvwxyz"
        consonants=consonants+consonants.upper()
        for ch in check:
            if ch in consonants:
                c=c+1
        print("consonant count =",c)
    elif choice==3:
         u=0
         for ch in check:
             if ch.isupper():
                u=u+1
         print("Upper case character count=",u)
    elif choice==4:
         l=0
         for ch in check:
             if ch.islower():
                l=l+1
         print("Lower case character count=",l)
    elif choice==5:
        linelist=[line.strip() for line in open("poem.txt")]
        for i in linelist:
            print(i.replace(" ","#"))
    else:
        print("Invalid Choice...")
        print("Program Over!")

