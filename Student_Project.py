def addstudent():
    def submitadd():
        id  = idvalue.get()
        name = namevalue.get()
        mobile  =mobilevalue.get()
        email = emailvalue.get()
        address = addressvalue.get()
        gender = gendervalue.get()
        dob = dobvalue.get()
        addedtime = time.strftime("%H:%M:%S")
        addeddate = time.strftime("%d/%m/%Y")
        try:
            strr = 'insert into student_data values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr,(id,name,mobile,email,address,gender,dob,addeddate,addedtime))
            con.commit()
            res = messagebox.askyesnocancel('Notifications','Id {} Name {} Added sucessfully... and want to clean the form'.format(id,name),parent = addroot)
            if(res==True):
                idvalue.set('')
                namevalue.set('')
                mobilevalue.set('')
                emailvalue.set('')
                addressvalue.set('')
                gendervalue.set('')
                dobvalue.set('')

        except:
            messagebox.showerror('Notification','Id Already Exist try another id',parent = addroot)
        strr = 'select * from student_data'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studenttable.insert('',END,values=vv)




    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('470x470+220+200')
    addroot.title('Student Management System')
    addroot.iconbitmap('icon.ico')
    addroot.resizable(False,False)
    #------------------------------Add Student Lables--------------------#
    idlable = Label(addroot,text='Enter Id: ',font=('Times', 12,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w',bd=6)
    idlable.place(x=10,y=10)

    namelable = Label(addroot, text='Enter Name: ', font=('Times', 12, 'bold'), relief=GROOVE, borderwidth=3, width=12,anchor='w', bd=6)
    namelable.place(x=10, y=70)

    mobilelable = Label(addroot, text='Enter Mobile ', font=('Times', 12, 'bold'), relief=GROOVE, borderwidth=3, width=12,anchor='w', bd=6)
    mobilelable.place(x=10, y=130)

    emaillable = Label(addroot, text='Enter Email: ', font=('Times', 12, 'bold'), relief=GROOVE, borderwidth=3, width=12,anchor='w', bd=6)
    emaillable.place(x=10, y=190)

    Addresslable = Label(addroot,text='Enter Address: ',font=('Times', 12,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w',bd=6)
    Addresslable.place(x=10,y=250)

    genderlable = Label(addroot, text='Enter Gender: ', font=('Times', 12, 'bold'), relief=GROOVE, borderwidth=3, width=12,anchor='w', bd=6)
    genderlable.place(x=10, y=310)

    doblable = Label(addroot, text='Enter D.O.B: ', font=('Times', 12, 'bold'), relief=GROOVE, borderwidth=3, width=12,anchor='w', bd=6)
    doblable.place(x=10, y=370)
    #-------------------------Enter Student Entry--------------------------------#
    idvalue = StringVar()
    identrty = Entry(addroot,font=('roman',12,'bold'),bd=6,width=30,textvariable=idvalue)
    identrty.place(x=200, y=10)
    namevalue = StringVar()
    nameentrty = Entry(addroot, font=('roman', 12, 'bold'), bd=6, width=30, textvariable=namevalue)
    nameentrty.place(x=200,y=70)
    mobilevalue = StringVar()
    mobileentrty = Entry(addroot, font=('roman', 12, 'bold'), bd=6, width=30, textvariable=mobilevalue)
    mobileentrty.place(x=200, y=130)
    emailvalue = StringVar()
    emailentrty = Entry(addroot, font=('roman', 12, 'bold'), bd=6, width=30, textvariable=emailvalue)
    emailentrty.place(x=200, y=190)
    addressvalue = StringVar()
    addressentrty = Entry(addroot, font=('roman', 12, 'bold'), bd=6, width=30, textvariable=addressvalue)
    addressentrty.place(x=200, y=250)
    gendervalue = StringVar()
    genderentrty = Entry(addroot, font=('roman', 12, 'bold'), bd=6, width=30, textvariable=gendervalue)
    genderentrty.place(x=200, y=310)
    dobvalue = StringVar()
    dobentrty = Entry(addroot, font=('roman', 12, 'bold'), bd=6, width=30, textvariable=dobvalue)
    dobentrty.place(x=200, y=370)
#----------------------------Adding Button---------------------------------------#
    submitbtn = Button(addroot,text='Submit',font=('Times',15,'bold'),width=15,bd=4,activebackground='black',activeforeground='white',command=submitadd)
    submitbtn.place(x=150,y=410)

#------------------------------------------------------------------------------------

    addroot.mainloop()
def searchstudent():
        def search():
            id = idvalue.get()
            name = namevalue.get()
            mobile = mobilevalue.get()
            email = emailvalue.get()
            address = addressvalue.get()
            gender = gendervalue.get()
            dob = dobvalue.get()
            addeddate = time.strftime("%d/%m/%Y")
            if(id !=''):
                strr = 'select * from student_data where id =%s'
                mycursor.execute(strr,(id))
                datas = mycursor.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in datas:
                    vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                    studenttable.insert('',END,values=vv)
            elif(name !=''):
                strr = 'select * from student_data where id =%s'
                mycursor.execute(strr,(name))
                datas = mycursor.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in datas:
                    vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                    studenttable.insert('',END,values=vv)
            elif(mobile !=''):
                strr = 'select * from student_data where id =%s'
                mycursor.execute(strr,(mobile))
                datas = mycursor.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in datas:
                    vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                    studenttable.insert('',END,values=vv)
            elif(email !=''):
                strr = 'select * from student_data where id =%s'
                mycursor.execute(strr,(email))
                datas = mycursor.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in datas:
                    vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                    studenttable.insert('',END,values=vv)
            elif(address !=''):
                strr = 'select * from student_data where id =%s'
                mycursor.execute(strr,(address))
                datas = mycursor.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in datas:
                    vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                    studenttable.insert('',END,values=vv)
            elif(gender !=''):
                strr = 'select * from student_data where id =%s'
                mycursor.execute(strr,(gender))
                datas = mycursor.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in datas:
                    vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                    studenttable.insert('',END,values=vv)
            elif(dob !=''):
                strr = 'select * from student_data where id =%s'
                mycursor.execute(strr,(dob))
                datas = mycursor.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in datas:
                    vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                    studenttable.insert('',END,values=vv)
            elif(addeddate !=''):
                strr = 'select * from student_data where id =%s'
                mycursor.execute(strr,(addeddate))
                datas = mycursor.fetchall()
                studenttable.delete(*studenttable.get_children())
                for i in datas:
                    vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
                    studenttable.insert('',END,values=vv)


        searchroot = Toplevel(master=DataEntryFrame)
        searchroot.grab_set()
        searchroot.geometry('470x540+220+200')
        searchroot.title('Student Management System')
        searchroot.iconbitmap('icon.ico')
        searchroot.resizable(False, False)
        # ------------------------------Add Student Lables--------------------#
        idlable = Label(searchroot, text='Enter Id: ', font=('Times', 12, 'bold'), relief=GROOVE, borderwidth=3, width=12,
                        anchor='w', bd=6)
        idlable.place(x=10, y=10)

        namelable = Label(searchroot, text='Enter Name: ', font=('Times', 12, 'bold'), relief=GROOVE, borderwidth=3,
                          width=12, anchor='w', bd=6)
        namelable.place(x=10, y=70)

        mobilelable = Label(searchroot, text='Enter Mobile ', font=('Times', 12, 'bold'), relief=GROOVE, borderwidth=3,
                            width=12, anchor='w', bd=6)
        mobilelable.place(x=10, y=130)

        emaillable = Label(searchroot, text='Enter Email: ', font=('Times', 12, 'bold'), relief=GROOVE, borderwidth=3,
                           width=12, anchor='w', bd=6)
        emaillable.place(x=10, y=190)

        Addresslable = Label(searchroot, text='Enter Address: ', font=('Times', 12, 'bold'), relief=GROOVE, borderwidth=3,
                             width=12, anchor='w', bd=6)
        Addresslable.place(x=10, y=250)

        genderlable = Label(searchroot, text='Enter Gender: ', font=('Times', 12, 'bold'), relief=GROOVE, borderwidth=3,
                            width=12, anchor='w', bd=6)
        genderlable.place(x=10, y=310)

        doblable = Label(searchroot, text='Enter D.O.B: ', font=('Times', 12, 'bold'), relief=GROOVE, borderwidth=3,
                         width=12, anchor='w', bd=6)
        doblable.place(x=10, y=370)
        datelable = Label(searchroot, text='Enter Date: ', font=('Times', 12, 'bold'), relief=GROOVE, borderwidth=3,
                         width=12, anchor='w', bd=6)
        datelable.place(x=10, y=430)

        # -------------------------Enter Student Entry--------------------------------#
        idvalue = StringVar()
        identrty = Entry(searchroot, font=('roman', 12, 'bold'), bd=6, width=30, textvariable=idvalue)
        identrty.place(x=200, y=10)
        namevalue = StringVar()
        nameentrty = Entry(searchroot, font=('roman', 12, 'bold'), bd=6, width=30, textvariable=namevalue)
        nameentrty.place(x=200, y=70)
        mobilevalue = StringVar()
        mobileentrty = Entry(searchroot, font=('roman', 12, 'bold'), bd=6, width=30, textvariable=mobilevalue)
        mobileentrty.place(x=200, y=130)
        emailvalue = StringVar()
        emailentrty = Entry(searchroot, font=('roman', 12, 'bold'), bd=6, width=30, textvariable=emailvalue)
        emailentrty.place(x=200, y=190)
        addressvalue = StringVar()
        addressentrty = Entry(searchroot, font=('roman', 12, 'bold'), bd=6, width=30, textvariable=addressvalue)
        addressentrty.place(x=200, y=250)
        gendervalue = StringVar()
        genderentrty = Entry(searchroot, font=('roman', 12, 'bold'), bd=6, width=30, textvariable=gendervalue)
        genderentrty.place(x=200, y=310)
        dobvalue = StringVar()
        dobentrty = Entry(searchroot, font=('roman', 12, 'bold'), bd=6, width=30, textvariable=dobvalue)
        dobentrty.place(x=200, y=370)
        datevalue = StringVar()
        dateentrty = Entry(searchroot, font=('roman', 12, 'bold'), bd=6, width=30, textvariable=datevalue)
        dateentrty.place(x=200, y=430)
        # ----------------------------Adding Button---------------------------------------#
        submitbtn = Button(searchroot, text='Submit', font=('Times', 15, 'bold'), width=15, bd=4, activebackground='black', activeforeground='white', command=search)
        submitbtn.place(x=150, y=470)

        # ----------------------------

        searchroot.mainloop()








def deletestudent():
    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values'][0]
    strr = 'delete from student_data where id=%s'
    mycursor.execute(strr,(pp))
    con.commit()
    messagebox.showinfo('Notification','ID{} Deleted sucessfully'.format(pp))
    strr = 'select * from student_data'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values=vv)


def updatetudent():
    def update():
        id = idvalue.get()
        name = namevalue.get()
        mobile = mobilevalue.get()
        email = emailvalue.get()
        address = addressvalue.get()
        gender = gendervalue.get()
        dob = dobvalue.get()
        date = datevalue.get()
        time = timevalue.get()

        strr  = 'update student_data set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id= %s'
        mycursor.execute(strr,(name,mobile,email,address,gender,dob,date,time,id))
        con.commit()
        messagebox.showinfo('Notification','Id {} Modified sucessfully...'.format(id))
        strr = 'select * from student_data'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            studenttable.insert('', END, values=vv)

    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('470x600+220+140')
    updateroot.title('Student Management System')
    updateroot.iconbitmap('icon.ico')
    updateroot.resizable(False, False
                         )
    # ------------------------------Add Student Lables--------------------#
    idlable = Label(updateroot, text='Enter Id: ', font=('Times', 12, 'bold'), relief=GROOVE, borderwidth=3, width=12,
                    anchor='w', bd=6)
    idlable.place(x=10, y=10)

    namelable = Label(updateroot, text='Enter Name: ', font=('Times', 12, 'bold'), relief=GROOVE, borderwidth=3,
                      width=12, anchor='w', bd=6)
    namelable.place(x=10, y=70)

    mobilelable = Label(updateroot, text='Enter Mobile ', font=('Times', 12, 'bold'), relief=GROOVE, borderwidth=3,
                        width=12, anchor='w', bd=6)
    mobilelable.place(x=10, y=130)

    emaillable = Label(updateroot, text='Enter Email: ', font=('Times', 12, 'bold'), relief=GROOVE, borderwidth=3,
                       width=12, anchor='w', bd=6)
    emaillable.place(x=10, y=190)

    Addresslable = Label(updateroot, text='Enter Address: ', font=('Times', 12, 'bold'), relief=GROOVE, borderwidth=3,
                         width=12, anchor='w', bd=6)
    Addresslable.place(x=10, y=250)

    genderlable = Label(updateroot, text='Enter Gender: ', font=('Times', 12, 'bold'), relief=GROOVE, borderwidth=3,
                        width=12, anchor='w', bd=6)
    genderlable.place(x=10, y=310)

    doblable = Label(updateroot, text='Enter D.O.B: ', font=('Times', 12, 'bold'), relief=GROOVE, borderwidth=3,
                     width=12, anchor='w', bd=6)
    doblable.place(x=10, y=370)
    datelable = Label(updateroot, text='Enter Date: ', font=('Times', 12, 'bold'), relief=GROOVE, borderwidth=3,
                      width=12, anchor='w', bd=6)
    datelable.place(x=10, y=430)
    timelable = Label(updateroot, text='Enter Time: ', font=('Times', 12, 'bold'), relief=GROOVE, borderwidth=3,
                      width=12, anchor='w', bd=6)
    timelable.place(x=10, y=490)

    # -------------------------Enter Student Entry--------------------------------#
    idvalue = StringVar()
    identrty = Entry(updateroot, font=('roman', 12, 'bold'), bd=6, width=30, textvariable=idvalue)
    identrty.place(x=200, y=10)
    namevalue = StringVar()
    nameentrty = Entry(updateroot, font=('roman', 12, 'bold'), bd=6, width=30, textvariable=namevalue)
    nameentrty.place(x=200, y=70)
    mobilevalue = StringVar()
    mobileentrty = Entry(updateroot, font=('roman', 12, 'bold'), bd=6, width=30, textvariable=mobilevalue)
    mobileentrty.place(x=200, y=130)
    emailvalue = StringVar()
    emailentrty = Entry(updateroot, font=('roman', 12, 'bold'), bd=6, width=30, textvariable=emailvalue)
    emailentrty.place(x=200, y=190)
    addressvalue = StringVar()
    addressentrty = Entry(updateroot, font=('roman', 12, 'bold'), bd=6, width=30, textvariable=addressvalue)
    addressentrty.place(x=200, y=250)
    gendervalue = StringVar()
    genderentrty = Entry(updateroot, font=('roman', 12, 'bold'), bd=6, width=30, textvariable=gendervalue)
    genderentrty.place(x=200, y=310)
    dobvalue = StringVar()
    dobentrty = Entry(updateroot, font=('roman', 12, 'bold'), bd=6, width=30, textvariable=dobvalue)
    dobentrty.place(x=200, y=370)
    datevalue = StringVar()
    dateentrty = Entry(updateroot, font=('roman', 12, 'bold'), bd=6, width=30, textvariable=datevalue)
    dateentrty.place(x=200, y=430)
    timevalue = StringVar()
    timeentrty = Entry(updateroot, font=('roman', 12, 'bold'), bd=6, width=30, textvariable=timevalue)
    timeentrty.place(x=200, y=490)
    # ----------------------------Adding Button---------------------------------------#
    submitbtn = Button(updateroot, text='Submit', font=('Times', 15, 'bold'), width=15, bd=4, activebackground='black',
                       activeforeground='white', command=update)
    submitbtn.place(x=150, y=530)
    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values']
    if(len(pp)!=0):
        idvalue.set(pp[0])
        namevalue.set(pp[1])
        mobilevalue.set(pp[2])
        emailvalue.set(pp[3])
        addressvalue.set(pp[4])
        gendervalue.set(pp[5])
        dobvalue.set(pp[6])
        datevalue.set(pp[7])
        timevalue.set(pp[8])

    # ----------------------------

    updateroot.mainloop()


def showstudent():
    strr = 'select * from student_data'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values=vv)
def exportstudent():
    ff = filedialog.asksaveasfilename()
    gg = studenttable.get_children()
    id,name,mobile,email,address,gender,dob,addeddate,addedtime = [],[],[],[],[],[],[],[],[]
    for i in gg:
        content = studenttable.item(i)
        pp = content['values']
        id.append(pp[0])
        name.append(pp[1])
        mobile.append(pp[2])
        email.append(pp[3])
        address.append(pp[4])
        gender.append(pp[5])
        dob.append(pp[6])
        addeddate.append(pp[7])
        addedtime.append(pp[8])
    dd = ['Id','Name','Mobile','Email','Address','Gender','D.O.B','Added Date','Added Time']
    df = pandas.DataFrame(list(zip(id,name,mobile,email,address,gender,dob,addeddate,addedtime)),columns=dd)
    paths = r'{}.csv'.format(ff)
    df.to_csv(paths,index=False)
    messagebox.showinfo('Notification','Student Data is saved'.format(paths))

def exitstudent():
    res = messagebox.askyesnocancel('Notification','Do you want to exit')
    if(res == True):
        root.destroy()
######################################Connection of DataBase########
def Connectdb():
    def submitdb():
        global con ,mycursor
        host = hostvalue.get()
        user = uservalue.get()
        password = passwordvalue.get()
        #host = 'localhost'
        #user = 'root'
        #password = 'Gopu2002@'


        try:
            con = pymysql.connect(host = host,user =user,password = password)
            mycursor = con.cursor()
        except:
            messagebox.showerror('Notification','Data is incorrect please try again',parent=dbroot)
            return
        try:
            strr = 'create database student_management_system'
            mycursor.execute(strr)
            strr = 'use student_management_system'
            mycursor.execute(strr)
            strr = 'create table student_data(id int, name varchar(20), mobile varchar(12),email varchar(30),address varchar(100),gender varchar(10),dob varchar(10),date varchar(30),time varchar (30))'
            mycursor.execute(strr)
            strr = 'alter table student_data modify column id int not null'
            mycursor.execute(strr)
            strr = 'alter table student_data modify column id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('Notification', 'Database created and now you are connected...', parent=dbroot)
        except:
            strr = 'use student_management_system'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','Now you are connected to database...',parent = dbroot)
        dbroot.destroy()
    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry('470x250+800+230')
    dbroot.iconbitmap('icon.ico')
    dbroot.resizable(False,False)
    dbroot.config(bg='white')
    #________________Connectdb Labels-----------------------------------------#
    hostlabel = Label(dbroot,text="Enter Host: ",font=('Times', 12,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w',bd=6)
    hostlabel.place(x=10,y=10)

    userlabel = Label(dbroot, text="Enter User: ", font=('Times', 12, 'bold'), relief=GROOVE, borderwidth=3, width=12,anchor='w',bd=6)
    userlabel.place(x=10, y=70)
    passwordlabel = Label(dbroot, text="Enter Password: ", font=('Times', 12, 'bold'), relief=GROOVE, borderwidth=3, width=12,anchor='w',bd=6)
    passwordlabel.place(x=10, y=130)
    #--------------------------------connect Db Entry----------------#
    hostvalue = StringVar()
    hostentry = Entry(dbroot,font=('roman',12,'bold'),bd=6,width=30,textvariable=hostvalue)
    hostentry.place(x=200,y=10)
    uservalue = StringVar()
    userentry = Entry(dbroot, font=('roman', 12, 'bold'), bd=6, width=30,textvariable=uservalue)
    userentry.place(x=200, y=70)
    passwordvalue = StringVar()
    passwordentry = Entry(dbroot, font=('roman', 12, 'bold'), bd=6, width=30,textvariable=passwordvalue)
    passwordentry.place(x=200, y=130)

    #-----------------------------------connect db button-----------------#
    submitbutton = Button(dbroot,text='Submit',font=('Times',15,'bold'),width=15,bd=4,activebackground='black',activeforeground='white',command=submitdb)
    submitbutton.place(x=100,y=190)
    dbroot.mainloop()
############################################
def IntroLabelTick():
    global count, text
    if(count>=len(ss)):
        count = 0
        text = ''
        SliderLabel.config(text=text)
    else:
        text =  text +ss[count]
        SliderLabel.config(text=text)
        count +=1
    SliderLabel.after(200,IntroLabelTick)
########################### Clock##########################
import random
colors = ['white','black']
def IntroLabelColorTick():
    fg = random.choice(colors)
    SliderLabel.config(fg=fg)
    SliderLabel.after(150,IntroLabelColorTick)
def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m/%Y")
    clock.config(text='Date: '+date_string+"\n"+"Time: "+time_string)
    clock.after(150,tick)

from tkinter import *
from tkinter.font import Font
import time
from tkinter import Toplevel, messagebox, filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
import pymysql
import pandas



root = Tk()
root.title("Student Management System")
root.config(bg='orange')
root.geometry('1174x700+200+50')
root.iconbitmap('icon.ico')
root.resizable(False, False)
BigFont = Font(family="Roboto Mono", size=30, weight="normal")
################################# FRAMES ###############################################
DataEntryFrame = Frame(root, bg='white', relief=GROOVE, borderwidth=5)
DataEntryFrame.place(x=10, y=80, width=450, height=500)
#---------------------------------Data Entry Frame Intro----------------------#
frontlabel = Label(DataEntryFrame,text='Welcome',width=30,font=('Courier',25,'bold'),)
frontlabel.pack(side=TOP,expand=True)
addbtn = Button(DataEntryFrame,text='1. Add Student',width=25,font=('Courier',20,'bold'),bd=4,activebackground='black',activeforeground='white',command=addstudent)
addbtn.pack(side=TOP,expand=2,)
searchbtn = Button(DataEntryFrame,text='2. Search Student',width=25,font=('Courier',20,'bold'),bd=4,activebackground='black',activeforeground='white',command=searchstudent)
searchbtn.pack(side=TOP,expand=2,)
deletebtn = Button(DataEntryFrame,text='3. Delete Student',width=25,font=('Courier',20,'bold'),bd=4,activebackground='black',activeforeground='white',command= deletestudent)
deletebtn.pack(side=TOP,expand=2,)
updatebtn = Button(DataEntryFrame,text='4. update Student',width=25,font=('Courier',20,'bold'),bd=4,activebackground='black',activeforeground='white',command= updatetudent)
updatebtn.pack(side=TOP,expand=2,)
showbtn = Button(DataEntryFrame,text='5. Show All',width=25,font=('Courier',20,'bold'),bd=4,activebackground='black',activeforeground='white',command= showstudent)
showbtn.pack(side=TOP,expand=2,)
exportbtn = Button(DataEntryFrame,text='6. Export Data',width=25,font=('Courier',20,'bold'),bd=4,activebackground='black',activeforeground='white',command= exportstudent)
exportbtn.pack(side=TOP,expand=2,)
exitbtn = Button(DataEntryFrame,text='7. Exit',width=25,font=('Courier',20,'bold'),bd=4,activebackground='black',activeforeground='white',command= exitstudent)
exitbtn.pack(side=TOP,expand=2,)



#----------------------------------Show Data Frame-------------------------------#
ShowDataFrame = Frame(root, bg='white', relief=GROOVE, borderwidth=5)
ShowDataFrame.place(x=500, y=80, width=650, height=500)

style = ttk.Style()
style.configure('Treeview.Heading',font=('arial',10,'bold'),foreground='black')
style.configure('Treeview',font=('arial',12,'bold'),foreground='black')
scroll_x = Scrollbar(ShowDataFrame,orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame,orient=VERTICAL)
studenttable = Treeview(ShowDataFrame,columns=('ID','Name','Mobile no','Email','Address','Gender','D.O.B','Added Date','Added Time'),yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)

scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)

scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)
studenttable.heading('ID',text='ID')
studenttable.heading('Name',text='Name')
studenttable.heading('Mobile no',text='Mobile no')
studenttable.heading('Email',text='Email')
studenttable.heading('Address',text='Address')
studenttable.heading('Gender',text='Gender')
studenttable.heading('D.O.B',text='D.O.B')
studenttable.heading('Added Date',text='Added Time')
studenttable.heading('Added Time',text='Added Time')
studenttable['show'] = 'headings'

studenttable.column('ID',width=10)
studenttable.column('Name',width=200)
studenttable.column('Mobile no',width=100)
studenttable.column('Email',width=300)
studenttable.column('Address',width=200)
studenttable.column('Gender',width=100)
studenttable.column('D.O.B',width=150)
studenttable.column('Added Date',width=150)
studenttable.column('Added Time',width=150)
studenttable.pack(fill=BOTH,expand=1)





################################ Slider ##########################################
ss = "Welcome To Student Management System"
count = 0
text = ''
SliderLabel = Label(root, text=ss, font=('Courier', 25), relief=RIDGE, borderwidth=4, width=35, bg='grey')
SliderLabel.place(x=180, y=0)
IntroLabelTick()
IntroLabelColorTick()
#################################Clock###########################################
clock = Label(root, font=('Courier', 12,'bold'), relief=RIDGE, borderwidth=4, bg='grey')
clock.place(x=0, y=0)
tick()
#####################################################Connect to data base button
connectbutton = Button(root,text ="Connect to Database",width=20,font=('Courier',15),relief=RIDGE,bg='grey',borderwidth=4, activebackground='black',activeforeground='white',command=Connectdb)
connectbutton.place(x=920,y=0)
root.mainloop()
