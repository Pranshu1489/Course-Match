import os
import platform
import mysql.connector
import pandas  

mydb=mysql.connector.connect(host="localhost",user="root",passwd="#mrverma1489",database=" course_match")
mycursor=mydb.cursor()

def course_Insert():
    L=[]
    c_id=int(input("Enter the course id : "))
    L.append(c_id)
    stream=input("Enter the Stream Name: ")
    L.append(stream)
    C_name=input("Enter available opportunities or courses  in this stream : ")
    L.append(C_name)
    course=(L)
    sql="insert into course_details (c_id, stream, c_name) values (%s,%s,%s)"
    mycursor.execute(sql,course)
    mydb.commit() 

def cView():
    print("Select the search criteria : ")
    print("1. C_id")
    print("2. Stream")
    print("3. All")
    ch=int(input("Enter the choice : "))
    if ch==1:
                   s=int(input("c_id : "))
                   c=(s,)
                   sql="select * from course_details   where C_ID=%s"
                   mycursor.execute(sql,c)
                   res=mycursor.fetchall()
                   for x in res:
                                  print(x)
    elif ch==2:
        s=input("Enter stream Name : ")
        n=(s,)
        sql="select * from course_details where  STREAM=%s"
        mycursor.execute(sql,n)
        res=mycursor.fetchall()
        for x in res:
                       print(x)
    elif ch==3:
        sql="select * from course_details"
        mycursor.execute(sql)
        res=mycursor.fetchall()
        print("The course details are as follows : ")
        print("(course_id, Stream_Name,Course_opportunities)")
        for x in res:
            print(x) 

def removecourse():
    cid=int(input("Enter the course_id of the course to be deleted : "))
    ci=(cid,)
    sql=("Delete from course_details where C_ID = %s")
    mycursor.execute(sql,ci)
    print("RECORD DELETED SUCCESSFULLY")
    mydb.commit()

def MenuSet(): 
    print("Enter 1 : To Add course")
    print("Enter 2 : To View course ")
    print("Enter 3 : To Remove course")
    try:  
        userInput = int(input("Please Select An Above Option: "))  
    except ValueError:
        exit("\nHy! That's Not A Number")  
    else: print("\n")  
    if(userInput == 1):
        course_Insert()
    elif (userInput==2):
        cView()
    elif (userInput==3):
        removecourse()
    else: print("Enter correct choice. . . ") 
MenuSet() 

def runAgain():
               runAgn = input("\nwant To Run Again Y/n: ")
               if runAgn == 'y':
                              MenuSet()
                              userInput = int(input("Please Select An Above Option: "))
                              if(userInput == 1):
                                             courseInsert()
                              elif (userInput==2):
                                             cView()
                              elif (userInput==3):
                                             removecourse()
                              else:
                                             print("Enter correct choice. . . ")
               else:
                              runAgain()
runAgain() 
