import sys
from dbConnect import MySQL
import tkMessageBox

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk  
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
 
import studentDemoProject_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    studentDemoProject_support.set_Tk_var()
    top = Toplevel1 (root)
    studentDemoProject_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    studentDemoProject_support.set_Tk_var()
    top = Toplevel1 (w)
    studentDemoProject_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def deleteStudent(self):
        roll=self.txtRoll.get('1.0','end-1c')
        dbresponse=self.mysql.execute("Delete from student where roll="+roll)
        tkMessageBox.showinfo("Deletion","The student was deleted successfully")
        
    def MaleSelected(self):
        self.gender="Male"
    def FemaleSelected(self):
        self.gender="Female"
    def addStudent(self):
        name=self.txtName.get('1.0','end');
        roll=self.txtRoll.get('1.0','end')
        marks=self.txtMarks.get('1.0','end')
        gender=self.sex
        age=self.Spinbox1.get();
        
        try:
            insQuery="insert into student values('"+name+"',"+roll+","+marks+","+age+",'"+gender+"')"
            self.mysql.execute(insQuery)
            tkMessageBox.showinfo("Error in adding","Error in adding student to DB")
            self.showdetails()
        except Exception:
            tkMessageBox.showerror("Adding student info","The student with name "+name+" was added successfully.")
        
    def showdetails(self):
        try:
            tkMessageBox.showinfo("Fetching data","Fetching student details..") 
            dbresponse=self.mysql.execute("select * from student")
            self.lstStudent.delete(0,self.lstStudent.size())
            for i in range(0,len(dbresponse.rows)):
                self.lstStudent.insert(i,dbresponse.rows[i])
        except Exception:
            tkMessageBox("Error","Error whie connecting to MySQL DB.")
        
    def __init__(self, top=None):
        try:
            mysql=MySQL("localhost","root","root","Student",as_dict=TRUE)
        except Exception:
            tkMessageBox.showerror("Error","Error whie connecting to MySQL DB.")




        
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'   # X11 color: 'gray85'
        _fgcolor = '#000000'   # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {Segoe UI} -size 16 -weight normal -slant "  \
            "italic -underline 0 -overstrike 0"

        top.geometry("730x689+5+712")
        top.minsize(148, 1)
        top.maxsize(1914, 1045)
        top.resizable(0, 0)
        top.title("Student data")
        top.configure(relief="raised")
        top.configure(background="#b1db22")

        self.var=IntVar()
        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.137, rely=0.058, relheight=0.356
                , relwidth=0.733)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#fbb448")

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.056, rely=0.082, height=43, width=97)
        self.Label1.configure(background="#fbb448")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font10)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Name''')

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.056, rely=0.245, height=43, width=123)
        self.Label2.configure(background="#fbb448")
        self.Label2.configure(cursor="fleur")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font10)
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Roll. No.''')

        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.075, rely=0.449, height=26, width=75)
        self.Label3.configure(background="#fbb448")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font=font10)
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''Marks''')

        self.Label4 = tk.Label(self.Frame1)
        self.Label4.place(relx=0.037, rely=0.612, height=26, width=124)
        self.Label4.configure(background="#fbb448")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font=font10)
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''Gender''')

        self.Label5 = tk.Label(self.Frame1)
        self.Label5.place(relx=0.075, rely=0.776, height=36, width=63)
        self.Label5.configure(background="#fbb448")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(font=font10)
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''Age''')

        self.txtName = tk.Text(self.Frame1)
        self.txtName.place(relx=0.318, rely=0.082, relheight=0.139
                , relwidth=0.624)
        self.txtName.configure(background="white")
        self.txtName.configure(font=font10)
        self.txtName.configure(foreground="black")
        self.txtName.configure(highlightbackground="#d9d9d9")
        self.txtName.configure(highlightcolor="black")
        self.txtName.configure(insertbackground="black")
        self.txtName.configure(selectbackground="#c4c4c4")
        self.txtName.configure(selectforeground="black")
        self.txtName.configure(wrap="word")

        self.txtRoll = tk.Text(self.Frame1)
        self.txtRoll.place(relx=0.318, rely=0.245, relheight=0.139
                , relwidth=0.624)
        self.txtRoll.configure(background="white")
        self.txtRoll.configure(font=font10)
        self.txtRoll.configure(foreground="black")
        self.txtRoll.configure(highlightbackground="#d9d9d9")
        self.txtRoll.configure(highlightcolor="black")
        self.txtRoll.configure(insertbackground="black")
        self.txtRoll.configure(selectbackground="#c4c4c4")
        self.txtRoll.configure(selectforeground="black")
        self.txtRoll.configure(wrap="word")

        self.txtMarks = tk.Text(self.Frame1)
        self.txtMarks.place(relx=0.318, rely=0.408, relheight=0.139
                , relwidth=0.624)
        self.txtMarks.configure(background="white")
        self.txtMarks.configure(font=font10)
        self.txtMarks.configure(foreground="black")
        self.txtMarks.configure(highlightbackground="#d9d9d9")
        self.txtMarks.configure(highlightcolor="black")
        self.txtMarks.configure(insertbackground="black")
        self.txtMarks.configure(selectbackground="#c4c4c4")
        self.txtMarks.configure(selectforeground="black")
        self.txtMarks.configure(wrap="word")

        self.Radiobutton1 = tk.Radiobutton(self.Frame1)
        self.Radiobutton1.place(relx=0.374, rely=0.571, relheight=0.212
                , relwidth=0.17)
        self.Radiobutton1.configure(activebackground="#ececec")
        self.Radiobutton1.configure(activeforeground="#000000")
        self.Radiobutton1.configure(background="#fbb448")
        self.Radiobutton1.configure(disabledforeground="#a3a3a3")
        self.Radiobutton1.configure(font=font10)
        self.Radiobutton1.configure(foreground="#000000")
        self.Radiobutton1.configure(highlightbackground="#d9d9d9")
        self.Radiobutton1.configure(highlightcolor="black")
        self.Radiobutton1.configure(justify='left')
        self.Radiobutton1.configure(text='''Male''')
        self.Radiobutton1.configure(variable=studentDemoProject_support.selectedButton)
        self.Radiobutton1.configure(variable=self.var,value=1,command=self.MaleSelected)

        self.Radiobutton2 = tk.Radiobutton(self.Frame1)
        self.Radiobutton2.place(relx=0.636, rely=0.571, relheight=0.212
                , relwidth=0.221)
        self.Radiobutton2.configure(activebackground="#ececec")
        self.Radiobutton2.configure(activeforeground="#000000")
        self.Radiobutton2.configure(background="#fbb448")
        self.Radiobutton2.configure(disabledforeground="#a3a3a3")
        self.Radiobutton2.configure(font=font10)
        self.Radiobutton2.configure(foreground="#000000")
        self.Radiobutton2.configure(highlightbackground="#d9d9d9")
        self.Radiobutton2.configure(highlightcolor="black")
        self.Radiobutton2.configure(justify='left')
        self.Radiobutton2.configure(text='''Female''')
        self.Radiobutton2.configure(variable=studentDemoProject_support.selectedButton)
        self.Radiobutton2.configure(variable=self.var,value=2,command=self.FemaleSelected)

        self.Spinbox1 = tk.Spinbox(self.Frame1, from_=1.0, to=100.0)
        self.Spinbox1.place(relx=0.318, rely=0.776, relheight=0.167
                , relwidth=0.622)
        self.Spinbox1.configure(activebackground="#f9f9f9")
        self.Spinbox1.configure(background="white")
        self.Spinbox1.configure(buttonbackground="#d9d9d9")
        self.Spinbox1.configure(disabledforeground="#a3a3a3")
        self.Spinbox1.configure(font=font10)
        self.Spinbox1.configure(foreground="black")
        self.Spinbox1.configure(highlightbackground="black")
        self.Spinbox1.configure(highlightcolor="black")
        self.Spinbox1.configure(insertbackground="black")
        self.Spinbox1.configure(selectbackground="#c4c4c4")
        self.Spinbox1.configure(selectforeground="black")
        self.Spinbox1.configure(textvariable=studentDemoProject_support.spinbox)

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.btnShow = tk.Button(top)
        self.btnShow.place(relx=0.164, rely=0.45, height=33, width=86)
        self.btnShow.configure(activebackground="#ececec")
        self.btnShow.configure(activeforeground="#000000")
        self.btnShow.configure(background="#fbb448")
        self.btnShow.configure(disabledforeground="#a3a3a3")
        self.btnShow.configure(foreground="#000000")
        self.btnShow.configure(highlightbackground="#d9d9d9")
        self.btnShow.configure(highlightcolor="black")
        self.btnShow.configure(pady="0")
        self.btnShow.configure(command=self.showdetails,text='''Show''')

        self.btnAdd = tk.Button(top)
        self.btnAdd.place(relx=0.356, rely=0.45, height=33, width=86)
        self.btnAdd.configure(activebackground="#ececec")
        self.btnAdd.configure(activeforeground="#000000")
        self.btnAdd.configure(background="#fbb448")
        self.btnAdd.configure(disabledforeground="#a3a3a3")
        self.btnAdd.configure(foreground="#000000")
        self.btnAdd.configure(highlightbackground="#d9d9d9")
        self.btnAdd.configure(highlightcolor="black")
        self.btnAdd.configure(pady="0")
        self.btnAdd.configure(command=self.addStudent,text='''Add''')

        self.btnModify = tk.Button(top)
        self.btnModify.place(relx=0.548, rely=0.45, height=33, width=86)
        self.btnModify.configure(activebackground="#ececec")
        self.btnModify.configure(activeforeground="#000000")
        self.btnModify.configure(background="#fbb448")
        self.btnModify.configure(disabledforeground="#a3a3a3")
        self.btnModify.configure(foreground="#000000")
        self.btnModify.configure(highlightbackground="#d9d9d9")
        self.btnModify.configure(highlightcolor="black")
        self.btnModify.configure(pady="0")
        self.btnModify.configure(text='''Modify''')

        self.btnDelete = tk.Button(top)
        self.btnDelete.place(relx=0.74, rely=0.45, height=33, width=86)
        self.btnDelete.configure(activebackground="#ececec")
        self.btnDelete.configure(activeforeground="#000000")
        self.btnDelete.configure(background="#fbb448")
        self.btnDelete.configure(cursor="fleur")
        self.btnDelete.configure(disabledforeground="#a3a3a3")
        self.btnDelete.configure(foreground="#000000")
        self.btnDelete.configure(highlightbackground="#d9d9d9")
        self.btnDelete.configure(highlightcolor="black")
        self.btnDelete.configure(pady="0")
        self.btnDelete.configure(command=self.deleteStudent,text='''Delete''')

        self.lstStudent = tk.Listbox(top)
        self.lstStudent.place(relx=0.137, rely=0.522, relheight=0.345
                , relwidth=0.732)
        self.lstStudent.configure(background="white")
        self.lstStudent.configure(disabledforeground="#a3a3a3")
        self.lstStudent.configure(font="TkFixedFont")
        self.lstStudent.configure(foreground="#000000")

if __name__ == '__main__':
    vp_start_gui()
