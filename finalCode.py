#Importing needed modules
import tkinter.messagebox
from tkinter import *
from tkinter import messagebox, ttk
import mysql.connector as msc


class Student:
    def __init__(self,root):
        self.root=root
        #________Defining Name of Window Top of GUI Interface_________
        self.root.title("Student Management System")
        self.root.geometry("1350x700+5+712")

        title=Label(self.root,text="STUDENT ERP",font=("times new roman",40,"bold"),bg="#808A87",fg="yellow1")
        title.pack(side=TOP)
        

        #__________All_Variables__________
        #Creating Variable for accesing in proceding code
        self.Roll_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()
        
        
        #__________Manage_Frame___________
        #Creating Frame for taking inputs in the program
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="#808A87")
        Manage_Frame.place(x=20,y=100,width=450,height=580)

        m_title=Label(Manage_Frame,text="Manage Students",bg="#808A87",fg="yellow1",font=("times new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        #Taking Roll No. as input
        lbl_roll=Label(Manage_Frame,text="Roll No.",bg="#808A87",fg="yellow1",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_Roll=Entry(Manage_Frame,textvariable=self.Roll_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        #Taking Name as input
        lbl_name=Label(Manage_Frame,text="Name",bg="#808A87",fg="yellow1",font=("times new roman",20,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        txt_name=Entry(Manage_Frame,textvariable=self.name_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")
        
        #Taking Email as input
        lbl_Email=Label(Manage_Frame,text="Email",bg="#808A87",fg="yellow1",font=("times new roman",20,"bold"))
        lbl_Email.grid(row=3,column=0,pady=10,padx=20,sticky="w")
        
        txt_Email=Entry(Manage_Frame,textvariable=self.email_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Email.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        #Taking Gender as input
        lbl_Gender=Label(Manage_Frame,text="Gender",bg="#808A87",fg="yellow1",font=("times new roman",20,"bold"))
        lbl_Gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        combo_Gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("times new roman",13,"bold"),state='readonly')
        combo_Gender['values']=("Male","Female","Other")
        combo_Gender.grid(row=4,column=1,padx=20,pady=10)

        #Taking Contact No. as input
        lbl_Contact=Label(Manage_Frame,text="Contact",bg="#808A87",fg="yellow1",font=("times new roman",20,"bold"))
        lbl_Contact.grid(row=5,column=0,pady=10,padx=20,sticky="w")

        txt_Contact=Entry(Manage_Frame,textvariable=self.contact_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Contact.grid(row=5,column=1,pady=10,padx=20,sticky="w")

        #Taking Date Of Birth as input
        lbl_DOB=Label(Manage_Frame,text="D.O.B.",bg="#808A87",fg="yellow1",font=("times new roman",20,"bold"))
        lbl_DOB.grid(row=6,column=0,pady=10,padx=20,sticky="w")

        txt_DOB=Entry(Manage_Frame,textvariable=self.dob_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_DOB.grid(row=6,column=1,pady=10,padx=20,sticky="w")

        #Taking Address as input
        lbl_Address=Label(Manage_Frame,text="Address",bg="#808A87",fg="yellow1",font=("times new roman",20,"bold"))
        lbl_Address.grid(row=7,column=0,pady=10,padx=20,sticky="w")

        self.txt_Address=Text(Manage_Frame,width=30,height=4,font=("",10))
        self.txt_Address.grid(row=7,column=1,pady=10,padx=20,sticky="w")
        

        #__________Button_Frame___________
        #Creating Buttons for futher operation on clicking these buttons
        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="#808A87")
        btn_Frame.place(x=15,y=515,width=400)

        Addbtn=Button(btn_Frame,text="Add",width=10,command=self.add_students).grid(row=0,column=0,padx=8,pady=10)
        Updatebtn=Button(btn_Frame,text="Update",width=10,command=self.update_data).grid(row=0,column=1,padx=8,pady=10)
        Deletebtn=Button(btn_Frame,text="Delete",width=10,command=self.delete_data).grid(row=0,column=2,padx=8,pady=10)
        Clearbtn=Button(btn_Frame,text="Clear",width=10,command=self.clear).grid(row=0,column=3,padx=8,pady=10)


        #__________Detail_Frame___________
        #Frame for showing taken inputs in the program
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="#808A87")
        Detail_Frame.place(x=500,y=100,width=800,height=580)

        #____________Table_Frame_____________
        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="#808A87")
        Table_Frame.place(x=10,y=10,width=770,height=550)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Student_table=ttk.Treeview(Table_Frame,columns=("Roll","name","Email","Gender","Contact","DOB","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("Roll",text="Roll No.")
        self.Student_table.heading("name",text="Name")
        self.Student_table.heading("Email",text="Email")
        self.Student_table.heading("Gender",text="Gender")
        self.Student_table.heading("Contact",text="Contact")
        self.Student_table.heading("DOB",text="D.O.B")
        self.Student_table.heading("Address",text="Address")
        self.Student_table['show']='headings'
        self.Student_table.column("Roll",width=1)
        self.Student_table.column("name",width=60)
        self.Student_table.column("Email",width=74)
        self.Student_table.column("Gender",width=2)
        self.Student_table.column("Contact",width=14)
        self.Student_table.column("DOB",width=4)
        self.Student_table.column("Address",width=100)
        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
        
    #Defining  funtion for taking entries from GUI application and adding it in MySQL table
    def add_students(self):
        if self.Roll_var.get()=="" or self.name_var.get()=="":
            tkinter.messagebox.showerror("Error","All fields are required!!!!!!!")
        else:
            con=msc.connect(host="localhost",user="root",passwd="Lakshmi@1234",database="stm")
            cur=con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_var.get(),
                                                                             self.name_var.get(),
                                                                             self.email_var.get(),
                                                                             self.gender_var.get(),
                                                                             self.contact_var.get(),
                                                                             self.dob_var.get(),
                                                                             self.txt_Address.get('1.0',END)
                                                                             ))
            con.commit()
            self.fetch_data()
            tkinter.messagebox.showinfo("Data Entry","Student data has been saved.")
            self.clear()
            con.close()            

            
    #Defining  funtion for taking entries from GUI application and adding it in MySQL table
    def fetch_data(self):
        conn=msc.connect(host="localhost",user="root",passwd="Lakshmi@1234",database="stm")
        cur=conn.cursor()
        cur.execute("SELECT * FROM students ")
        rows=cur.fetchall()
        output=''
        self.Student_table.delete(*self.Student_table.get_children())
        for x in rows:
            output=output+str(x[0])+' '+x[1]+' '+x[2]+' '+x[3]+' '+x[4]+' '+x[5]+' '+x[6]+'\n'
            self.Student_table.insert('',END,values=x)
        conn.commit()
        cur.close()
        conn.close()

        
    #Defining  funtion for clearing entries in text box for further use
    def clear(self):
        self.Roll_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_Address.delete("1.0",END)
        tkinter.messagebox.showinfo("Fields","Entry fields are now vacant,you can add new data.")
        

    #Defining  funtion for setting cursor
    def get_cursor(self,ev):
        curosor_x=self.Student_table.focus()
        contents=self.Student_table.item(curosor_x)
        x=contents['values']
        self.Roll_var.set(str(x[0]))
        self.name_var.set(x[1])
        self.email_var.set(x[2])
        self.gender_var.set(x[3])
        self.contact_var.set(x[4])
        self.dob_var.set(x[5])
        self.txt_Address.delete("1.0",END)
        self.txt_Address.insert(END,x[6])
        

    #Defining  funtion for updating MySQL table data from GUI program
    def update_data(self):
        con=msc.connect(host="localhost",user="root",passwd="Lakshmi@1234",database="stm")
        cur=con.cursor()
        cur.execute("update students set name=%s,Email=%s,Gender=%s,Contact=%s,DOB=%s,Address=%s where Roll=%s",(
                                                                         self.name_var.get(),
                                                                         self.email_var.get(),
                                                                         self.gender_var.get(),
                                                                         self.contact_var.get(),
                                                                         self.dob_var.get(),
                                                                         self.txt_Address.get('1.0',END),
                                                                         self.Roll_var.get()
                                                                         ))
        con.commit()
        self.fetch_data()
        tkinter.messagebox.showinfo("Updation","Student data has been updated.")
        self.clear()
        con.close()        
        

    #Defining  funtion for deleting entries from MySQL table through GUI application
    def delete_data(self):
        con=msc.connect(host="localhost",user="root",passwd="Lakshmi@1234",database="stm")
        cur=con.cursor()
        a=str(self.Roll_var.get())
        cur.execute("DELETE FROM students WHERE Roll=%s",(a,))
        con.commit()
        con.close()
        self.fetch_data()
        tkinter.messagebox.showinfo("Deletion","Student data has been deleted.")
        


root=Tk()
ob=Student(root)
root.mainloop()