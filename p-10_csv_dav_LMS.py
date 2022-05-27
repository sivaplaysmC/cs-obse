
# library Management System
import csv
# Define global variables
lib_fields = ['book_no', 'book_name', 'book_author', 'book_publisher', 'book_genre']
lib_database = 'library.csv'
book_data=[
[1,"Da Vinci Code,The","Dan Brown", "Transworld", "Mystery Thriller"],
[2,"Harry Potter and the Deathly Hallows","J.K.Rowling","Bloomsbury","Children Fiction"],
[3,"Who Will Cry When You Die","Robin Sharma","JAICO BOOKS","Philosophy"],
[4,"Harry Potter and the Philosopher's Stone","J.K.Rowling","Bloomsbury","Children Fiction"],
[5,"Inferno","Dan Brown", "Transworld", "Mystery Thriller"]
]
with open(lib_database, "w",newline='') as f:
        writer = csv.writer(f)
        writer.writerows(book_data)

def display_menu():
    print("--------------------------------------")
    print(" Welcome to Library Management System")
    print("---------------------------------------")
    print("""1. Add New Book
2. View Books
    a. author wise
    b. genre wise
    c. view all
3. Search Book
4. Update Book Info
5. Delete Book
6. Quit""")
    
def add_book():
    print("-------------------------")
    print("Add Book Information")
    print("-------------------------")
    book_data = []
    for field in lib_fields:
        value = input("Enter " + field + ": ")
        book_data.append(value)
    with open(lib_database, "a",newline='') as f:
        writer = csv.writer(f)
        writer.writerows([book_data])
    print("Data saved successfully")
    input("Press any key to continue")
    return
def view_books():
    print("--- book Records ---")
    print("""View Books
    a. author wise
    b. genre wise
    c. view all""")
    
    choice=input("Enter your choice to view as ---a b c---")
    if choice=="a":
        author=input("Enter name of author")
        flag=False
        with open(lib_database, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if(row[2]==author):
                    flag=True
                    print ("--------------------------------------------------------")
                    print(' book_no: '+row[0]+' book_name: '+row[1])
                    print(' book_author: '+row[2])
                    print(' book_publisher: '+row[3]+' book_genre: '+row[4])
                    print ("--------------------------------------------------------")
        if flag==False:
             print("the entered author not found")
                           
    if choice=="b":
        gen=input("Enter the genre you want to look for")
        flag=False
        with open(lib_database, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if(row[4]==gen):
                    flag=True
                    print ("--------------------------------------------------------")
                    print(' book_no: '+row[0]+' book_name: '+row[1])
                    print(' book_author: '+row[2])
                    print(' book_publisher: '+row[3]+' book_genre: '+row[4])
                    print ("--------------------------------------------------------")

        if flag==False:
            print("the entered genre not found")

    if choice=="c":
        with open(lib_database, "r") as f:
            reader = csv.reader(f)
            print(reader)
            for row in reader:
                print ("--------------------------------------------------------")
                print(' book_no: '+row[0]+' book_name: '+row[1])
                print(' book_author: '+row[2])
                print(' book_publisher: '+row[3]+' book_genre: '+row[4])
                print ("--------------------------------------------------------")     
    input("Press any key to continue")

def search_book():
    print("--- Search book ---")
    book_no = input("Enter book_no no. to search: ")
    with open(lib_database, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) > 0:
                if book_no == row[0]:
                    print("----- book Found -----")
                    print ("--------------------------------------------------------")
                    print(' book_no: '+row[0]+' book_name: '+row[1])
                    print(' book_author: '+row[2])
                    print(' book_publisher: '+row[3]+' book_genre: '+row[4])
                    print ("--------------------------------------------------------")
                    
                    break
        else:
            print("book_no No. not found in our database")
    input("Press any key to continue")


def update_book():
    print("--- Update book ---")
    book_no = input("Enter book_no to update: ")
    index_book = None
    updated_data = []
    with open(lib_database, "r") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if book_no == row[0]:
                    index_book = counter
                    print("book Found: at index ",index_book)
                    book_data = []
                    for field in lib_fields:
                        value = input("Enter " + field + ": ")
                        book_data.append(value)
                    updated_data.append(book_data)
                else:
                    updated_data.append(row)
                counter += 1
        # Check if the record is found or not
    if index_book is not None:
        with open(lib_database, "w",newline='') as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("book_no No. not found in our database")

    input("Press any key to continue")


def delete_book():   
    print("--- Delete book ---")
    book_no = input("Enter book_no no. to delete: ")
    book_found = False
    updated_data = []
    with open(lib_database, "r") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if book_no != row[0]:
                    updated_data.append(row)
                    counter += 1
                else:
                    book_found = True

    if book_found is True:
        with open(lib_database, "w",newline='') as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("book_no no. ", book_no, "deleted successfully")
    else:
        print("book_no No. not found in our database")

    input("Press any key to continue")


    

while True:
    display_menu()

    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_book()
    elif choice == 2:
        view_books()
    elif choice == 3:
        search_book()
    elif choice == 4:
        update_book()
    elif choice == 5:
        delete_book()
    elif choice==6:
        print("Invalid choice)
    else:
        break

print("-------------------------------")
print(" Thank you for using our system")
print("-------------------------------")
