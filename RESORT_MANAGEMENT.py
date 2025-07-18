import mysql.connector as a
con=a.connect(host='localhost',user='root',passwd='root',database='resort')

if con.is_connected():
    print("Connection established successfully..")
else:
    print("Error while connecting the database..")


def AddStaff():
    n = input("Staff name:")
    cl = input("Department:")
    sa = int(input("Salary:"))
    r = int(input("Staff_id:"))
    ad = input("S_Address:")
    ph = input("S_Phone:")
    dob = input("DOB:")
    sex = input("Sex:")
    ms = input("Marital status:")
    ye = int(input("Years of experience:"))
    q = input("Qualification:")
    #sql = 'INSERT INTO Staff () VALUES ({0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10})'.format(n, cl, sa, r, ad, ph, dob, sex, ms, ye, q)

    sql = "INSERT INTO STAFF (Name, Department,Salary,Staff_id,Address,Phone,DOB,sex,marital_status,yrs_of_exp,qualification) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (n, cl, sa, r, ad, ph, dob, sex, ms, ye, q)
    c = con.cursor()
    c.execute(sql,val)
    con.commit()
    print("Data entered successfully")
    print("")


def RemoveStaff():
    Department = input("Department:")
    Staff_id = int(input("Staff_id:"))
    data = (Department, Staff_id)
    c = con.cursor()
    sql = 'DELETE FROM Staff WHERE Department=%s AND Staff_id=%s'
    c.execute(sql, data)
    con.commit()
    print("Data Updated")
    print("")


def UpdateS_Sal():
    name=input("Staff name:")
    staff_id=int(input ("staff id:") )
    salary=int(input ("Salary:"))
    data=(salary,name,staff_id)
    sq1='update Staff set salary=%s where name=%s and staff_id=%s'
    c=con.cursor()
    c.execute(sq1, data)
    con.commit ()
    print("Data Update")
    print("")


def DisplayStaff():
    cl=input("Department:")
    data=(cl,)
    sql='select * from Staff where Department=%s'
    c=con.cursor()
    c.execute(sql, data)
    d=c.fetchall()
    for i in d:
        print("S_Name:", i[0])
        print("Department:", i[1])
        print("Salary:", i[2])
        print("Staff_id:", i[3])
        print("S_Address:", i[4])
        print("S_Phone:", i[5])
        print("DOB:", i[6])
        print("sex:", i[7])
        print("marital status:", i[8])
        print("years of experience:", i[9])
        print("Qualification:", i[10])
        print("")
    print("")


def Add_M():
    n=input ("Manager name:")
    mcode=int(input("M_Code:"))
    s=int(input("Salary:"))
    a=input("Address:")
    ph=input("Phone:")
    dob=input("DOB:")
    sex=input("sex:")
    ms=input("marital status:")
    ye=int(input("years of experience:"))
    q=input("Qualification:")
    sql = 'INSERT INTO Manager (Name,Mcode,Salary,Address,Phone,DOB,Sex,marital_status,yrs_of_exp,qualification) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    data = (n, mcode, s, a, ph, dob, sex, ms, ye, q)
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("Data entered successfully")
    print("")


def Remove_M():
    name=input("Manager:")
    mcode=int(input("Mcode:"))
    data=(name, mcode)
    sql = 'DELETE FROM Manager WHERE name=%s AND mcode=%s'
    c=con.cursor()
    c.execute (sql, data) 
    con.commit()
    print("Data Updated")
    print("")


def UpdateM_Sal():
    name=input("Manager:")
    mcode=int(input ("Mcode:") )
    salary=int(input ("Salary:"))
    data=(salary,name, mcode)
    sq1='update Manager set salary=%s where name=%s and mcode=%s'
    c=con.cursor()
    c.execute(sq1, data)
    con.commit ()
    print("Data Update")
    print("")


def DisplayManager():
    c = con.cursor()
    c.execute("SELECT * FROM Manager")
    e = c.fetchall()
    for i in e:
        print("Name:", i[0])
        print("Mcode:", i[1])
        print("Salary:", i[2])
        print("Address:", i[3])
        print("Phone:", i[4])
        print("DOB:", i[5])
        print("sex:", i[6])
        print("marital status:", i[7])
        print("years of experience:", i[8])
        print("Qualification:", i[9])
        print("")


def SD_Attd():
    d=input("Department:")
    clt=input("Department Manager:")
    t=int(input("Total no. of staffs:"))
    date=input("Date:")
    ab=int(input("No of absentees:"))
    sql = 'INSERT INTO SD_Attendance (Department,Department_M,Total_St,Date,Absentees) VALUES (%s, %s, %s, %s, %s)'
    data = (d, clt, t, date, ab)
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("Data entered successfully")
    print("")


def DisplaySD_Attd():
    sql = 'SELECT * FROM SD_Attendance'
    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()
    for i in d:
        print("Department:", i[0])
        print("Department Manager:", i[1])
        print("Total no. of staffs:", i[2])
        print("Date:", i[3])
        print("Absentees:", i[4])
        print("")


def MD_Attd():
    n=input("Name: ")
    de=input("Department:")
    d=input( "Date:")
    a=input("Attendance:")
    sql = 'INSERT INTO MD_Attd (Name,Department,Date,Attendance) VALUES (%s, %s, %s, %s)'
    data = (n, de, d, a)
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("Data entered successfully")
    print("")


def DisplayMD_Attd():
    sql = 'SELECT * FROM MD_Attd'
    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()
    for i in d:
        print("Name:", i[0])
        print("Department:", i[1])
        print("Date:", i[2])
        print("Attendance:", i[3])
        print("")
    

def AddGuest():
    print('1.Garden')
    print('2.Swimming pool')
    print('3.Beach')
    print('4.Villa')
    nv=int(input("Enter the View:"))
    no=int(input("No. of room:"))
    d=int(input("Total no of days:"))
    if nv==1:
        v='Garden'
        cost=15000
        tax=12/100
        total_c=((cost*tax)+cost)*no*d
    elif nv==2:
        v='Swimming pool'
        cost=20000
        tax=12/100
        total_c=((cost*tax)+cost)*no*d
    elif nv==3:
        v='Beach'
        cost=25000
        tax=12/100
        total_c=((cost*tax)+cost)*no*d
    elif nv==4:
        v='Villa'
        cost=30000
        tax=12/100
        total_c=((cost*tax)+cost)*no*d
    else:
        print("ENTER VALID CHOICE!!!")
    n=input("Guest name:")
    rn=input("room no:")
    a=input("G_Address:")
    ph=int(input("G_Phone:"))
    paid_amt=int(input("Paid amount:"))
    balance_amt=total_c-paid_amt
    data=(n,v,rn,no,d,a,ph,total_c,paid_amt,balance_amt)
    sql = 'INSERT INTO Guest ( Name, View, Room_no, No_of_Room, No_of_Days, Address, Phone, Total_Cost, Paid_amt, Balance_amt) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("Data entered successfully")
    print("")


def DisplayGuest():
    v = input("View:")
    data = (v,)
    sql = 'SELECT * FROM Guest WHERE View = %s'
    c = con.cursor()
    c.execute(sql, data)
    d = c.fetchall()
    for i in d:
        print("G_Name:", i[0])
        print("View:", i[1])
        print("Room no:", i[2])
        print("No. of room:", i[3])
        print("No. of days:", i[4])
        print("Address:", i[5])
        print("Phone:", i[6])
        print("Total cost:", i[7])
        print("Paid amount:", i[8])
        print("Balance amount", i[9])
        print("")


def Monthly_Resort_Expense():
    dat = input("Date:")
    sa = int(input("Salaries:"))
    ad = int(input("Advertising:"))
    i = int(input("Insurance:"))
    s = int(input("Supplies:"))
    rent = int(input("Rent:"))
    elec = int(input("Electricity:"))
    w = int(input("Water:"))
    ro_m = int(input("Room maintenance:"))
    gm = int(input("Garden maintenance:"))
    pm = int(input("Pool maintenance:"))
    rm = int(input("Restaurant maintenance:"))
    total_exp = sa + ad + i + s + rent + elec + w + ro_m + gm + pm + rm
    data = (dat, sa, ad, i, s, rent, elec, w, ro_m, gm, pm, rm, total_exp)
    sql = 'INSERT INTO Monthly_Resort_Expense (Date, Salaries, Advertising, Insurance, Supplies, Rent, Electricity,  Water, Room_Maintenance, Garden_Maintenance, Pool_Maintenance, Restaurant_Maintenance, Total_Expense) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("Data entered successfully")
    print("")


def DisplayMonthly_Resort_Expense():
    sql = 'SELECT * FROM Monthly_Resort_Expense'
    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()
    for i in d:
        print("Date:", i[0])
        print("Salaries:", i[1])
        print("Advertising:", i[2])
        print("Insurance:", i[3])
        print("Supplies:", i[4])
        print("Rent:", i[5])
        print("Electricity:", i[6])
        print("Water:", i[7])
        print("Room maintenance:", i[8])
        print("Garden maintenance:", i[9])
        print("Pool maintenance:", i[10])
        print("Restaurant maintenance:", i[11])
        print("Total Expense:", i[12])
        print("")


while True:
    print("RESORT ARORA")
    print("1. Staff")
    print("2. Manager")
    print("3. Staff Attendance")
    print("4. Manager Attendance")
    print("5. Guest")
    print("6. Monthly Resort Expense")
    
    table = int(input("Enter table number: "))
    print("")
    
    if table == 1:
        while True:
            print("1. Add Staff")
            print("2. Remove Staff")
            print("3. Update Salary")
            print("4. Display Staff Details")
            task = int(input("Enter task number: "))
            
            if task == 1:
                AddStaff()
            elif task == 2:
                RemoveStaff()
            elif task == 3:
                UpdateS_Sal()
            elif task == 4:
                DisplayStaff()
            else:
                print("Enter Valid Choice!!")
            
            op = input("Continue in this table (y/n): ")
            if op.lower() != 'y':
                break
    
    elif table == 2:
        while True:
            print("1. Add Manager")
            print("2. Remove Manager")
            print("3. Update Salary")
            print("4. Display Manager Details")
            task = int(input("Enter task number: "))
            
            if task == 1:
                Add_M()
            elif task == 2:
                Remove_M()
            elif task == 3:
                UpdateM_Sal()
            elif task == 4:
                DisplayManager()
            else:
                print("Enter Valid Choice!!")
            
            op = input("Continue in this table (y/n): ")
            if op.lower() != 'y':
                break
    
    elif table == 3:
        while True:
            print("1. Staff Attendance")
            print("2. Display Staff Attendance Details")
            task = int(input("Enter task number: "))
            
            if task == 1:
                SD_Attd()
            elif task == 2:
                DisplaySD_Attd()
            else:
                print("Enter Valid Choice!!")
            
            op = input("Continue in this table (y/n): ")
            if op.lower() != 'y':
                break
    
    elif table == 4:
        while True:
            print("1. Manager Attendance")
            print("2. Display Manager Attendance Details")
            task = int(input("Enter task number: "))
            
            if task == 1:
                MD_Attd()
            elif task == 2:
                DisplayMD_Attd()
            else:
                print("Enter Valid Choice!!")
            
            op = input("Continue in this table (y/n): ")
            if op.lower() != 'y':
                break
    
    elif table == 5:
        while True:
            print("1. Add Guest")
            print("2. Display Guest Details")
            task = int(input("Enter task number: "))
            
            if task == 1:
                AddGuest()
            elif task == 2:
                DisplayGuest()
            else:
                print("Enter Valid Choice!!")
            
            op = input("Continue in this table (y/n): ")
            if op.lower() != 'y':
                break
    
    elif table == 6:
        while True:
            print("1. Monthly Resort Expense")
            print("2. Display Resort Expense")
            task = int(input("Enter task number: "))
            
            if task == 1:
                Monthly_Resort_Expense()
            elif task == 2:
                DisplayMonthly_Resort_Expense()
            else:
                print("Enter Valid Choice!!")
            
            op = input("Continue in this table (y/n): ")
            if op.lower() != 'y':
                break
    
    else:
        print("ENTER VALID CHOICE!!!")
    
    ch = input("Do you want to continue (y/n): ")
    if ch.lower() != 'y':
        break

con.close()
