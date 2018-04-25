import sqlite3
import random
import time
import datetime

line=("_"*170)

def account_detail(data):
    #conn = sqlite3.connect("banking.db")
    #c = conn.cursor()
    #c.execute("SELECT * FROM signin WHERE Mno=? AND Password=?", (mno,pas,))
    #data = c.fetchall()
    #print(data)
    print(line)
    print('\n')
    print("\t\t\tNAME           :  ",data[0][0])
    print("\t\t\tMOBILE NUMBER  :  ",data[0][1])
    print("\t\t\tEMAIL ID       :  ",data[0][2])
    print("\t\t\tACCOUNT NUMBER :  ",data[0][3])
    print("\t\t\tBRANCH NAME    :  ",data[0][5])
    #conn.commit()
    #conn.close()
    login_succ(data)




def balance(data):
    print(line)
    print("\n\t\t\tYOUR AVAILABLE BALANCE IS ",data[0][4])
    login_succ(data)




'''def fund_transfer(data):
    count=0
    status="DEBIT"
    print("\n\n*****ENTER BENEFICIARY DETAILS*****\n")
    bname=input("\t\t\tNAME                : ")
    baccno=input("\t\t\tACCOUNT NO.         : ")
    bcaccno=input("\t\t\tCONFIRM ACCOUNT NO. : ")
    while(baccno!=bcaccno):
        print("\n\t\t\tACCOUNT NUMBER DIDN'T MATCH\n")
        baccno = input("\t\t\tACCOUNT NO.         : ")
        bcaccno = input("\t\t\tCONFIRM ACCOUNT NO. : ")

    bifsc=input("\t\t\tIFSC CODE            : ")
    bankname=input("\t\t\tBANK NAME            : ")
    amount=float(input("\t\t\tAMOUNT               : "))
    verify = input("\t\t\tENTER YOUR PASSWORD  : ")
    while(verify!=data[0][6]):
       count+=1
       print("\n\t\t\tINCORRECT PASSWORD TRY AGAIN")
       verify = input("\n\t\t\tENTER YOUR PASSWORD  : ")
       while(count==2):
           print("\nYOU ARE ABOUT TO EXCEED MAXIMUM ALLOWED ATTEMPTS ")
           login_succ(data)
    tid = random.randint(1000000, 9000000)
    number=data[0][1]
    chek=data[0][4]-amount
    #print(type(c))
    #print(data)
    if(chek<0):
        print("\n\t\t\tINSUFFICIENT BALANCE")
        login_succ(data)

    else:
        conn=sqlite3.connect("banking.db")
        c=conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS transfer(Tid INT primary key,Name TEXT,AccNo TEXT,IFSC TEXT,"   \
                  "Bank TEXT,Amount INT,Status TEXT,Mno TEXT,foreign key(Mno) REFERENCES signin(Mno))")
        c.execute("INSERT INTO transfer(Tid,Name,AccNo,IFSC,Bank,Amount,Status,Mno) "     \
                  "VALUES(?, ?, ?, ?, ?, ?, ?, ?)",(tid,bname,baccno,bifsc,bankname,amount,status,number,))
        c.execute("UPDATE signin SET Balance=? WHERE Mno=?", (chek,data[0][1],))
        c.execute("SELECT * FROM signin WHERE Mno=?",(data[0][1],))
        data=c.fetchall()
        conn.commit()
        conn.close()
        print("\n\t\tAMOUNT IS SUCCESSFULLY TRANSFERRED")
        print("\n\t\tTRANSACTION ID IS ", tid)
        login_succ(data)
'''

def fund_transfer(data):
    count=0
    dr="DEBIT"
    cr="CREDIT"
    print(line)
    mb=input("\n\t\t\tENTER BENEFICIARY MOBILE NUMBER: ")
    conn = sqlite3.connect("banking.db")
    c=conn.cursor()
    c.execute("SELECT * FROM signin WHERE Mno=?", (mb,))
    bdata=c.fetchall()
    if(len(bdata)):
        print("\n\t\t\tNAME               : ",bdata[0][0])
        print("\t\t\tEMAIL ID           : ",bdata[0][2])
        print("\t\t\tACCOUNT NUMBER     : ",bdata[0][3])
        print("\t\t\tBRANCH NAME        : ",bdata[0][5])
        print("\n\t\t\t1.CONFIRM")
        print("\t\t\t2.BACK")
        d=int(input("\n\t\t\tSELECT OPTION: "))
        if(d==1):
            print(line)
            amount=float(input("\n\t\t\tENTER AMOUNT     :"))
            verify = input("\t\t\tENTER YOUR PASSWORD  : ")
            while (verify != data[0][6]):
                count += 1
                print("\n\t\t\tINCORRECT PASSWORD TRY AGAIN")
                verify = input("\n\t\t\tENTER YOUR PASSWORD  : ")
                while (count == 2):
                    print("\nYOU ARE ABOUT TO EXCEED MAXIMUM ALLOWED ATTEMPTS ")
                    login_succ(data)
            check=data[0][4]-amount
            if(check<0):
                print("\n\t\t\tINSUFFICIENT BALANCE")
                login_succ(data)
            else:
                Tid=random.randint(10000000,90000000)
                tm=time.time()
                date=str(datetime.datetime.fromtimestamp(tm).strftime("%d-%m-%Y"))
                tim=str(datetime.datetime.fromtimestamp(tm).strftime("%H:%M"))
                c.execute("CREATE TABLE IF NOT EXISTS transfer(Tid INT, Name TEXT, AccNo TEXT, "   \
                          "Branch TEXT,Amount INT,Status TEXT,Date TEXT,Time TEXT,Mno TEXT,foreign key(Mno) REFERENCES  signin(Mno))")
                c.execute("INSERT INTO transfer(Tid,Name,AccNo,Branch,Amount,Status,Date,Time,Mno) VALUES(?, ?, "    \
                          " ?, ?, ?, ?, ?, ?, ?)",(Tid,bdata[0][0],bdata[0][3],bdata[0][5],amount,dr,date,tim,data[0][1],))
                c.execute("INSERT INTO transfer(Tid,Name,AccNo,Branch,Amount,Status,Date,Time,Mno) VALUES(?, ?, " \
                          " ?, ?, ?, ?, ?, ?, ?)", (Tid, data[0][0], data[0][3], data[0][5], amount, cr,date,tim,bdata[0][1],))
                c.execute("UPDATE signin SET Balance=? WHERE Mno=?",(data[0][4]-amount,data[0][1]))
                c.execute("UPDATE signin SET Balance=? WHERE Mno=?",(bdata[0][4]+amount,bdata[0][1]))
                c.execute("SELECT * FROM signin WHERE Mno=?", (data[0][1],))
                data = c.fetchall()
                conn.commit()
                conn.close()
                print("\n\t\tAMOUNT IS SUCCESSFULLY TRANSFERRED")
                print("\n\t\tTRANSACTION ID IS ", Tid)
                login_succ(data)
        if(d==2):
            fund_transfer(data)
    else:
        print("\n\tUSER NOT FOUND")
        fund_transfer(data)



def mini_statement(data):
    conn=sqlite3.connect("banking.db")
    c=conn.cursor()
    c.execute("SELECT * FROM transfer WHERE Mno=?",(data[0][1],))
    th=c.fetchall()             #transaction history
    print("\n")
    print(line)
    print(" SrNo\t\tTransaction ID\t\tStatus\t\tAmount\t\t Date \t\t\tTime\t\t Acc. Number \t\tName")
    for i in range(len(th)):
        print(line)
        print("\n {}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}".format(i+1,th[i][0],th[i][5],th[i][4],th[i][6],th[i][7],th[i][2],th[i][1]))
    conn.commit()
    conn.close()
    login_succ(data)






def change_pas(data):
    mno=data[0][1]
    pas=data[0][6]
    print(line)
    print('\n')
    cpas=input("\n\t\t\tENTER YOUR CURRENT PASSWORD: ")
    if(cpas==pas):
        npas=input("\t\t\tENTER NEW PASSWORD: ")
        ncpas=input("\t\t\tCONFIRM PASSWORD: ")
        conn = sqlite3.connect("banking.db")
        c = conn.cursor()
        c.execute("UPDATE signin SET password=? WHERE Mno=?", (npas, data[0][1],))
        c.execute("SELECT * FROM signin WHERE Mno=?", (data[0][1],))
        data = c.fetchall()
        conn.commit()
        conn.close()
        print("\n\t\t\tYOUR PASSWORD HAS BEEN SUCCESSFULLY CHANGED :)")
        login_succ(data)

    else:
        print(line)
        print("INVALID CURRENT PASSWORD")
        login_succ(data)




def login_succ(data):
    print(line)
    print("\n\n\t\t\t1. ACCOUNT DETAIL.")
    print("\t\t\t2. AVAILABLE BALANCE.")
    print("\t\t\t3. FUND TRANSFER.")
    print("\t\t\t4. TRANSACTION HISTORY.")
    print("\t\t\t5. CHANGE PASSWORD")
    print("\t\t\t6. LOG OUT.")
    ch=int(input("\n\t\t\tENTER YOUR CHOICE: "))
    if ch==1:
        account_detail(data)
    if ch==2:
        balance(data)
    if ch==3:
        fund_transfer(data)
    if ch==4:
        mini_statement(data)
    if ch==5:
        change_pas(data)
    if ch==6:
        main()




def signup(name,mno,mail,accno,bal,bname,pas):
    conn = sqlite3.connect("banking.db")
    c = conn.cursor()
    try:
        c.execute("CREATE TABLE IF NOT EXISTS signin(Name TEXT,Mno INT primary key,Email TEXT, "    \
                  "AccNo INT,Balance REAL,Branch TEXT,Password TEXT)")
        c.execute("INSERT INTO signin(Name,Mno,Email,AccNo,Balance,Branch,Password)"        \
                  " VALUES(?, ?, ?, ?, ?, ?, ?)",(name,mno,mail,accno,bal,bname,pas,))
    except:
        print("\n\nTHIS MOBILE IS ALREADY REGISTERED \n\n")
        main()
    conn.commit()
    conn.close()
    print("\n\n\t\t\tYOU ARE SUCCESSFULLY REGISTERED :)\n\n")
    main()




def login(mno,pas):
    conn = sqlite3.connect("banking.db")
    c = conn.cursor()
    c.execute("SELECT * FROM signin WHERE Mno=? AND Password=?",(mno,pas,))
    data=c.fetchall()
    #print(data)
    if(len(data)):
        print(line)
        print("\n\nYOU ARE SUCCESSFULLY LOGGED IN :)")
        print("\n------------Hello {} WELCOME TO STATE BANK OF INDIA------------".format(data[0][0]))
        login_succ(data)

    else:
        print("\nINCORRECT PASSWORD")
        main()
    conn.commit()
    conn.close()




def main():
    print(line)
    print('\n')
    print("\t\t\t1. LOG IN")
    print("\t\t\t2. SIGN IN")
    print("\t\t\t3. EXIT")

    n=int(input("\n\t\t\tENTER YOUR CHOICE :"))
    if(n==2):
        print(line)
        print('\n')
        print("FILL YOUR DETAILS ")
        print("\n")
        name = input("\t\tFULL NAME: ")
        mno=input("\t\tMOBILE NUMBER: ")
        mail = input("\t\tEMAIL ID: ")
        accno=input("\t\tACCOUNT NUMBER: ")
        try:
            bal=float(input("\t\tCURRENT BALANCE: "))
        except:
            try:
                bal = float(input("\t\tENTER VALID BALANCE: "))
            except:
                print(line)
                print("\t\t\tTRY AGAIN")
                main()
        bname=input("\t\tBRANCH NAME: ")
        pas=input("\t\tPASSWORD: ")
        cpas=input("\t\tCONFIRM PASSWORD: ")
        while(pas!=cpas):
            print(line)
            print("\t\t\tPASSWORD DOES NOT MATCH\n\n")
            pas = input("\t\tPASSWORD: ")
            cpas = input("\t\tCONFIRM PASSWORD: ")

        signup(name,mno,mail,accno,bal,bname,pas)

        #accno=int(input("Account Number: "))
        #bal=int(input("Balance: "))

    if(n==1):
        print(line)
        mno=input("\n\t\t\tENTER YOUR MOBILE NUMBER: ")
        pas=input("\t\t\tENTER PASSWORD: ")
        login(mno,pas)

    if(n==3):
        exit()

    if(n!=1 and n!=2 and n!=3):
        print("\n\tSELECT CORRECT OPTION\n")
        main()


main()






