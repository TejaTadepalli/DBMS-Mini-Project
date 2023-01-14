from tkinter import *
from tkinter import ttk

class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+5+712")

        title=Label(self.root,text="Student Management System",font=("times new roman",40,"bold"),bg="yellow",fg="red")
        title.pack(side=TOP)

        #__________Manage_Frame___________
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Manage_Frame.place(x=20,y=100,width=450,height=580)

        m_title=Label(Manage_Frame,text="Manage Students",bg="crimson",fg="white",font=("times new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_roll=Label(Manage_Frame,text="Roll No.",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_Roll=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_name=Label(Manage_Frame,text="Name",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        txt_name=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        lbl_Email=Label(Manage_Frame,text="Email",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_Email.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        txt_Email=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Email.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        lbl_Gender=Label(Manage_Frame,text="Gender",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_Gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        combo_Gender=ttk.Combobox(Manage_Frame,font=("times new roman",13,"bold"),state='readonly')
        combo_Gender['values']=("Male","Female","Other")
        combo_Gender.grid(row=4,column=1,padx=20,pady=10)

        lbl_Contact=Label(Manage_Frame,text="Contact",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_Contact.grid(row=5,column=0,pady=10,padx=20,sticky="w")

        txt_Contact=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Contact.grid(row=5,column=1,pady=10,padx=20,sticky="w")

        lbl_DOB=Label(Manage_Frame,text="D.O.B.",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_DOB.grid(row=6,column=0,pady=10,padx=20,sticky="w")

        txt_DOB=Entry(Manage_Frame,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_DOB.grid(row=6,column=1,pady=10,padx=20,sticky="w")

        lbl_Address=Label(Manage_Frame,text="Address",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_Address.grid(row=7,column=0,pady=10,padx=20,sticky="w")

        txt_Address=Text(Manage_Frame,width=30,height=4,font=("",10))
        txt_Address.grid(row=7,column=1,pady=10,padx=20,sticky="w")
        

        #__________Button_Frame___________
        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="crimson")
        btn_Frame.place(x=15,y=515,width=400)

        Addbtn=Button(btn_Frame,text="Add",width=10).grid(row=0,column=0,padx=8,pady=10)
        Updatebtn=Button(btn_Frame,text="Update",width=10).grid(row=0,column=1,padx=8,pady=10)
        Deletebtn=Button(btn_Frame,text="Delete",width=10).grid(row=0,column=2,padx=8,pady=10)
        Clearbtn=Button(btn_Frame,text="Clear",width=10).grid(row=0,column=3,padx=8,pady=10)


        #__________Detail_Frame___________
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Detail_Frame.place(x=500,y=100,width=800,height=580)

        lbl_search=Label(Detail_Frame,text="Search By",bg="crimson",fg="white",font=("times new roman",20,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_search=ttk.Combobox(Detail_Frame,width=10,font=("times new roman",13,"bold"),state='readonly')
        combo_search['values']=("Roll number","Name","Contact")
        combo_search.grid(row=0,column=1,padx=20,pady=10)

        txt_Search=Entry(Detail_Frame,width=20,font=("times new roman",10,"bold"),bd=5,relief=GROOVE)
        txt_Search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        searchbtn=Button(Detail_Frame,text="Search",width=10,pady=5).grid(row=0,column=3,padx=10,pady=10)
        showallbtn=Button(Detail_Frame,text="Show all",width=10,pady=5).grid(row=0,column=4,padx=10,pady=10)


        #____________Table_Frame_____________
        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="crimson")
        Table_Frame.place(x=10,y=70,width=760,height=500)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        Student_table=ttk.Treeview(Table_Frame,columns=("Roll","name","Email","Gender","Contact","DOB","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=Student_table.xview)
        scroll_y.config(command=Student_table.yview)
        Student_table.heading("Roll",text="Roll No.")
        Student_table.heading("name",text="Name")
        Student_table.heading("Email",text="Email")
        Student_table.heading("Gender",text="Gender")
        Student_table.heading("Contact",text="Contact")
        Student_table.heading("DOB",text="D.O.B")
        Student_table.heading("Address",text="Address")
        Student_table['show']='headings'
        Student_table.column("Roll",width=100)
        Student_table.column("name",width=100)
        Student_table.column("Email",width=100)
        Student_table.column("Gender",width=100)
        Student_table.column("Contact",width=100)
        
        Student_table.column("DOB",width=100)
        Student_table.column("Address",width=100)
        Student_table.pack(fill=BOTH,expand=1)

root=Tk()
ob=Student(root)
root.mainloop()