import mysql.connector as sqltor
server=sqltor.connect(user='root',host='localhost',password='rfscslab',database='rfs')
if server.is_connected():
    print("Successfully connected to student database.")
else:
    print("Failed to connect to student database.")

def search_student():
    stud=input("Enter student name : ")
    cursor=server.cursor()
    cursor.execute("select * from student where name like '%{}%' ".format(stud,))
    data=cursor.fetchall()
    if len(data)>=1:
        print(len(data), "results found.")
        for i in data:
            print("------ STUDENT DETAILS ------")
            print("Admission No.: ",i[0])
            print("Name: ",i[1])
            print("Gender: ",i[2])
            print("Class: ",i[3])
            print("Section: ",i[4])
            print("Stream: ",i[5])
            print("Marks: ",i[6])
            print("Phone Number: ",i[7])
            print("Email_Id: ",i[8])
    server.commit()
    cursor.close()

def update_student():
        cursor=server.cursor()
        print('1. Update Name')
        print('2. Update Gender')
        print('3. Update Class')
        print('4. Update Section')
        print('5. Update Stream')
        print('6. Update Phone Number')
        print('7. Update E-mail Id')
        opt=int(input('>>>>>> Enter your choice : '))
        print('---------------------------------------------------')
        if opt==1:
            print('###### NAME UPDATER MENU #####')
            Q=input('Enter ADMISSION_NUMBER whose data you want to update: ')
            L=input('Enter your updated name: ')
            cursor.execute("update student set NAME='{}' where ADDMISSION_NUMBER={}".format(L,Q))
            server.commit()
        elif opt==2:
            print('###### GENDER UPDATER MENU #####')
            p=input('Enter name whose data you want to update: ')
            l=input('Enter your updated Gender: ')
            cursor.execute("update student set GENDER='{}' where name='{}'".format(l,p))
            server.commit()
        elif opt==3:
            print('###### CLASS UPDATER MENU #####')
            m=input('Enter name whose data you want to update: ')
            n=input('Enter your updated class: ')
            cursor.execute("update student set CLASS='{}' where name='{}'".format(n,m))
            server.commit()
        elif opt==4:
            print('###### SECTION UPDATER MENU #####')
            y=input('Enter name whose data you want to update: ')
            e=input('Enter your updated section: ')
            cursor.execute("update student set SECTION='{}' where name='{}'".format(e,y))
            server.commit()
        elif opt==5:
            print('###### STREAM UPDATER MENU #####')
            f=input('Enter name whose data you want to update: ')
            z=input('Enter your updated stream : ')
            cursor.execute('update student set STREAM="{}" where name="{}"'.format(z,f))
            server.commit()
        elif opt==6:
            print('###### PHONE NUMBER UPDATER MENU #####')
            h=input('Enter name whose data you want to update: ')
            r=input('Enter your updated phone number: ')
            cursor.execute("update student set PHONE_NUMBER='{}' where name='{}'".format(r,h))
            server.commit()
        elif opt==7:
            print('###### EMAIL ID UPDATER MENU #####')
            j=input('Enter name whose data you want to update: ')
            k=input('Enter your updated email_id : ')
            cursor.execute("update student set EMAIL_ID='{}' where name='{}'".format(k,j))
            server.commit()
        else:
            print("Invalid selection.")
            update_student()
        cursor.close()

def add_student():
    print(".................. ADD STUDENT DETAILS ..................")
    A=int(input('Enter student admission number: '))
    B=input('Enter student name: ')
    C=input('Enter student gender: ')
    D=input('Enter student class: ')
    E=input('Enter student section: ')
    F=input('Enter student stream: ')
    G=int(input('Enter student marks: '))
    H=input('Enter student phone number: ')
    I=input('Enter student email id: ')
    cursor=server.cursor()
    code="insert into student values({},'{}','{}','{}','{}','{}',{},'{}','{}')".format(A,B,C,D,E,F,G,H,I)
    cursor.execute(code)
    server.commit()
    cursor.close()
    print("Student data added successfully.")
            
def delete_student():
        print("##### DELETION MENU #####")
        name=input("Enter admission number of student: ")
        cursor=server.cursor()
        cursor.execute("delete from student where ADMISSION_NUMBER={}".format(name,))
        print("Student data deleted successfully.")
        server.commit()
        cursor.close()

def user():
    print("### USER MENU ###")
    print("1. search_student() >>> View student details")
    
def admin():
    print("### ADMIN MENU ###")
    print("1. search_student()  >>> View student details")
    print("2. update_student() >>> Update student details")
    print("3. add_student() >>> Add student details")
    print("4. delete_student() >>> Delete student details")

print("##### WELCOME TO STUDENT MANAGEMENT SYSTEM #####")
print("1. LOG IN AS ADMIN")
print("2. LOG IN AS USER")
print("3. EXIT PROGRAM")
log=int(input("Enter your choice: "))
if log==1:
    admin()
elif log==2:
    user()
elif log==3:
    server.close()
    exit()
else:
    print("Invalid input, please restart the program to try again.")
        
