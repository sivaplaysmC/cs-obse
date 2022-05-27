import statistics
import random
import urllib.request
import webbrowser
ch="y"
while ch=='y' or ch=='Y':
    print("1.Statistics")
    print("2.Random")
    print("3.Url & Webbrowser")
    op=int(input("Enter your option:"))
    if op==1:
        l=list()
        num=int(input("Enter the total number of element in the list:"))
        for i in range (num):
            n=int(input("Enter the number:"))
            l.append(n)
        print("Mean:",statistics.mean(l))
        print("Median:",statistics.median(l))
        print(l)
        print("Mode:",statistics.mode(l))
    elif op==2:
        number=random.randint(10,20)
        ctr=0
        while ctr<5:
            guess=int(input("Guess a number in range 10....20  :"))
            if guess==number:
                print("You won!!!  The number was",number)
                break
            else:
                ctr+=1
            if not ctr<5:
                print("You lost!!!  The number was",number)
    elif op==3:
        weburl=urllib.request.urlopen('http://www.cbseacademic.nic.in')
        print(weburl)
        html=weburl.read()
        data=weburl.getcode()
        url=weburl.geturl()
        hd=weburl.headers
        inf=weburl.info()
        print("The url is  :",url)
        print("HTTP status code is:",data)
        print("headers returned \n",hd)
        print("the info() returned : \n",inf)
        print("Now opening the url:",url) 
        webbrowser.open_new(url)
    else:
        print("Incorrect option")
    ch=input("Do you want to continue?(y/n):")   

            
                
