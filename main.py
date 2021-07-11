from typing import Optional
import os

print("*" *80)
print("\t\t\tCHEMIST BILLING SYSTEM")
print("*" *80)

def begin():
    global option
    print("Welcome to the billing system")
    option = input("Enter l to login or r to register: ")
    if(option!="l" and option!="r"):
        print("Enter correct option")
        begin()

def register(username,password):
    print("New user")
    db = open("USERDB.txt", "a")
    db.write(username + "|" + password + "\n")
    print("User registered successfully") 
    db.close()
    main()

def login(username,password):
    db = open("USERDB.txt","r")
    for i in db:
        a,b = i.split("|")
        b = b.strip()
        if(a==username and b==password):
            print("Logged in successfully")
            main()
            break
        else:
            print("Wrong username or password")
            exit(0)
            print(" ")

def access(option):
    global name
    if(option == "l"):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        login(username,password)
    else:
        print("Enter your username and password to register")
        username = input("Username: ")
        password = input("Password: ")
        register(username,password)

def main():
    print("*" * 80)
    print("\t\t\tMENU")
    print("*" * 80)
    print("Select an Action to Continue:")
    print("1. Add new medicines")
    print("2. Delete medicines")
    print("3. Modify medicine details")
    print("4. Search for medicine")
    print("5. Search medicine by Index")
    print("6. View Medicines")
    print("7. Make a Bill")
    print("8. Exit")
    print("")
    num = int(input("Enter your choice: "))
    print("")
    if (num == 1):
        add()
        return
    if (num == 2):
        delete()
        return
    if (num == 3):
        # update()
        return
    if (num == 4):
        search()
        return
    if (num == 5):
        search_index()
        return
    if (num == 6):
        view()
        return
    if (num == 7):
        j = 1
        # bill(j)
        return
    if (num == 8):
        exit(0)


def add():
    print("*" * 80)
    print("\t\t\tADD NEW MEDICINE")
    print("*" * 80)
    print("Enter new Medicine details")
    print("")
    while True:
        name = input("Enter name: ")
        company = input("Enter manufacturer company: ")
        price = input("Enter price of 1 unit: ")
        quantity = str(float(input("Enter no of units: ")))
        mfgdate = input("Enter manufacture date {dd/mm/yyyy}: ")
        expdate = input("Enter expiry date {dd/mm/yyyy}: ")
        print("")
        md_add = open("MEDICINEDB.txt", "a")
        record = name + "|" + company + "|" + price + "|" + quantity + "|" + mfgdate + "|" + expdate
        md_add.write(record)
        md_add.write("\n")
        md_add.close()
        addop = int(input("Press 1 to continue add medicines or Press 0 to exit: "))
        if addop == 1:
            print("")
            continue
        else:
            break
    main()

def delete():
    db = open("MEDICINEDB.txt", "r")
    tempfile = open("DELETEMED.txt", "w")
    med = input("Enter medicine name to delete: ")
    s = ' '
    while s:
        s = db.readline()
        L = s.split("|")
        if len(s) > 0:
            if L[0] != med:
                tempfile.write(s)
    tempfile.close()
    db.close()
    os.remove("MEDICINEDB.txt")
    os.rename("DELETEMED.txt", "MEDICINEDB.txt")
    addop = int(input("Press 1 to continue delete medicine or Press 0 to exit: "))
    if addop == 1:
        delete()
    else:
        main()

# def update():
#     db = open("MEDICINEDB.txt","r")
#     med = str(input("Enter medicine name: "))
#     flag = True
#     index = 0
#     for line in db:
#         index += 1
#         l = line.split("|")
#         if med == l[0]:
#             flag == False
#             break
#     if flag:
#         print(med, " found in records")
#         while True:
#             t = open("MEDICINEDB.txt")
#             lines = t.readlines()
#             str1 = lines[index -1]
#             lines.remove(str1)

def search():
    string1 = input("Enter medicine to search: ")
    file1 = open("MEDICINEDB.txt", "r")
    flag = 0
    index = 0
    for line in file1:
        index += 1
        if string1 in line:
            flag = 1
            break
    if flag == 0:
        print(string1, 'Not Found')
    else:
        print(string1, 'Found In Line', index)
        while True:
            f = open("MEDICINEDB.txt")
            lines = f.readlines()   #readlines reads all the lines from the file and put it into lines
            # print(lines[index-1])  
            str1 = lines[index - 1]    #str displays the contents of the specific line given by the index var in string format
            # print(str1)
            lst1 = str1.split("|")     #lst1 takes in teh string str1 and then using delimiter function convert that into a list
            # print(lst1)
            print("Medicine: " + lst1[0] + "\nManufacturer: " + lst1[1] + "\nPPU: " + lst1[2] + "\nQuantity : " + lst1[3] + 
                    "\nDate of manufacture: " + lst1[4] + "\nDate of expiry: " + lst1[5])
            break
    file1.close()
    addop = int(input("Press 1 to continue search medicine or Press 0 to exit: "))
    if addop == 1:
        search()
    else:
        main()


def search_index():
    key = int(input("Enter record number to search: "))
    if key <= 0:
        print("Record not found")
    else:
        f = open("MEDICINEDB.txt")
        lines = f.readlines()  #retrieves all the entries in the db in the form of strings and makes a list of the strings
        # print(lines)
        krec = lines[key-1]  #krec takes in only the entry given by key-1 but its still a string
        lst = krec.split("|")  #lst contains krec converted from a string to a list using delimiter  
        print("Medicine: " + lst[0] + "\nManufacturer: " + lst[1] + "\nPPU: " + lst[2] + "\nQuantity : " + lst[3] + 
                    "\nDate of manufacture: " + lst[4] + "\nDate of expiry: " + lst[5])
        f.close()
    addop = int(input("Press 1 to continue search medicine or Press 0 to exit: "))
    if addop == 1:
        search_index()  #Hello from the other world
    else:
        main()


def view():
    f= open("MEDICINEDB.txt")
    lines = f.readlines()
    # print(lines)
    for line in lines:
        lst = line.split("|")
        # print(lst)
        print("")
        print("Medicine: " + lst[0] + "\nManufacturer: " + lst[1] + "\nPPU: " + lst[2] + "\nQuantity: " + lst[3] +
                 "\nDate of manufacture: " +  lst[4] + "\nDate of expiry: " + lst[5])
    f.close()
    main()

def bill():
    while True:
        print("*"*80)
        print("\t\t\t\tBILL")
        print("*"*80)
        cust = input("Enter customer name: ")
        bdate = input("Enter billing date: ")
        i = 0
        

begin()
access(option)

