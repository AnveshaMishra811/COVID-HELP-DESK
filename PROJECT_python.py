import mysql.connector
import random
import welcomescreen

mydb=mysql.connector.connect(host='localhost',\
                             user='root',\
                             passwd='anoushka22')

mycursor=mydb.cursor()

#mycursor.execute("CREATE DATABASE health")
'''mycursor.execute('show databases')
print(mycursor)
for i in mycursor:
    print(i)'''
mycursor.execute('use health')

#mycursor.execute ("CREATE TABLE userinfo (patient_id varchar(15) primary key,first_name varchar(30),last_name varchar(20),age integer,gender varchar(7), blood_group varchar(4),address varchar(50), phone_number varchar(10), profession varchar(20),state varchar(30) ) ")

'''mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)'''

'''first=input("ENTER YOUR FIRST NAME : ")
last=input("ENTER YOUR LAST NAME : ")
age=int(input("ENTER YOUR AGE : "))
gen=input("ENTER YOUR GENDER : ")
blogrp=input("ENTER YOUR BLOOD GROUP : ")
addr=input("ENTER YOUR ADDRESS : ")
phnum=int(input("ENTER YOUR PHONE NUMBER : "))
prof=input("ENTER YOUR PROFESSION : ")
state=input("ENTER YOUR RESIDING STATE: ")

p=' '
while True:
    name=first+last
    prt=name[0:4]
    l1=list(prt)
    q=random.randint(0,9999)
    s=str(q)
    for i in l1:
        p+=i
    id=p+s
    break

    
evalue="INSERT INTO userinfo\
(patient_id,first_name,last_name,age,gender,blood_group,address,phone_number,profession,state)\
VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
entry=(id,first,last,age,gen,blogrp,addr,phnum,prof,state)
mycursor.execute(evalue,entry)
mydb.commit()'''



def mainmenu():
    ch=0
    while ch<=3:
        print()
        print("1~CORONA INFORMATION")
        print("2~SELF ASSESSMENT")
        print("3~COVID-19 UPDATES")
        print()
        ch=int(input("Enter the number written against the menu option you want to access"))
        if ch==1:
            import coronainfo
            c=input('DO YOU WANT TO EXPLORE MORE OPTIONS?')
            if c=='n' or c=='N' or c=='no' or c=='No' or c=='NO':
                print()
                import exit
                break
        elif ch==2:
            import self_assessment
            c=input('DO YOU WANT TO EXPLORE MORE OPTIONS?')
            if c=='n' or c=='N' or c=='no' or c=='No' or c=='NO':
                print()
                import exit
                break
        elif ch==3:
            import matplot
            c=input('DO YOU WANT TO EXPLORE MORE OPTIONS?')
            if c=='n' or c=='N' or c=='no' or c=='No' or c=='NO':
                print()
                import exit
                break

mainmenu()
            
