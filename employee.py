# from tkinter import *
# from PIL import Image, ImageTk
# from tkinter import ttk

# class employeeClass: 
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("1100x550+220+90")
#         self.root.title("Retail Merchandise Management System | Developed by Samyam Sandip")
#         self.root.config(bg="white")
#         self.root.focus_force() #to highlight the window of employee whenever the employee button is pressed

#         #-----------------------------------#
#         #All Variables ------------------------#
#         self.var_searchby = StringVar()
#         self.var_searchtxt = StringVar()
#         self.var_emp_id = StringVar()
#         self.var_gender = StringVar()
#         self.var_contact = StringVar()
#         self.var_name = StringVar()
#         self.var_dob = StringVar()
#         self.var_doj = StringVar()
#         self.var_email = StringVar()
#         self.var_pass = StringVar()
#         self.var_utype = StringVar() #user type
#         self.var_salary = StringVar()





#         #------------------searchFrame----------------------#
#         SearchFrame=LabelFrame(self.root, text="Search Employee", bg="white", font=("Baskerville Old Face", 14), bd=3)
#         SearchFrame.place(x=250, y=20, width=600, height=70)

#         #--------------------dropdown----------------------#
#         cmb_search=ttk.Combobox(SearchFrame, textvariable=self.var_searchby, values=("Select","Email","Name","Contact"),state='readonly', justify=CENTER, font=("Times New Roman", 13))
#         cmb_search.place(x=8, y=8, width=150)
#         cmb_search.current(0) #Select is shown in the dropdown when nothing is selected

#         txt_search=Entry(SearchFrame, textvariable=self.var_searchtxt, font=("Times New Roman", 15), bg="lightyellow", width=28).place(x=170, y=7)
#         btn_search=Button(SearchFrame, text="Search", font=("Times New Roman", 14, "italic", "bold"), bg="#008080", fg="white", cursor="hand2").place(x=465, y=6, width=120, height=30)

#         #-----------------------Title---------------------------#
#         title = Label(self.root, text="Employee Details", font=("goudy old style", 15), bg="#0f4d7d", fg="white").place(x=50, y=100, width=983)

#         #----------------------Content---------------------------#
#         #----------row1----------------#
#         lbl_empid = Label(self.root, text="Emp ID:", font=("Times New Roman", 15), bg="white").place(x=50, y=150)
#         lbl_gender = Label(self.root, text="  Gender:", font=("Times New Roman", 15), bg="white").place(x=350, y=150)
#         lbl_contact = Label(self.root, text="Contact:", font=("Times New Roman", 15), bg="white").place(x=750, y=150)

#         txt_empid = Entry(self.root, textvariable=self.var_emp_id , font=("Times New Roman", 15), bg="lightyellow").place(x=150, y=150, width=180)
#         cmb_gender=ttk.Combobox(self.root, textvariable=self.var_gender, values=("Select","Male","Female","Other"),state='readonly', justify=CENTER, font=("Times New Roman", 13))
#         cmb_gender.place(x=500, y=150, width=180)
#         cmb_gender.current(0)
#         txt_contact = Entry(self.root, textvariable= self.var_contact, font=("Times New Roman", 15), bg="lightyellow").place(x=850, y=150, width=180)

#         #------------row2-----------------#
#         lbl_name = Label(self.root, text="Name:", font=("Times New Roman", 15), bg="white").place(x=50, y=190)
#         lbl_dob = Label(self.root, text="  D.O.B.:", font=("Times New Roman", 15), bg="white").place(x=350, y=190)
#         lbl_doj = Label(self.root, text="D.O.J.:", font=("Times New Roman", 15), bg="white").place(x=750, y=190)

#         txt_name = Entry(self.root, textvariable=self.var_name , font=("Times New Roman", 15), bg="lightyellow").place(x=150, y=190, width=180)
#         txt_dob = Entry(self.root, textvariable=self.var_dob , font=("Times New Roman", 15), bg="lightyellow").place(x=500, y=190, width=180)
#         txt_doj = Entry(self.root, textvariable= self.var_doj, font=("Times New Roman", 15), bg="lightyellow").place(x=850, y=190, width=180)

#         #------------row3-----------------#
#         lbl_email = Label(self.root, text="Email:", font=("Times New Roman", 15), bg="white").place(x=50, y=230)
#         lbl_pass = Label(self.root, text="  Password:", font=("Times New Roman", 15), bg="white").place(x=350, y=230)
#         lbl_utype = Label(self.root, text="User Type:", font=("Times New Roman", 15), bg="white").place(x=750, y=230)

#         txt_email = Entry(self.root, textvariable=self.var_email , font=("Times New Roman", 15), bg="lightyellow").place(x=150, y=230, width=180)
#         txt_pass = Entry(self.root, textvariable=self.var_pass , font=("Times New Roman", 15), bg="lightyellow").place(x=500, y=230, width=180)
#         txt_utype = Entry(self.root, textvariable= self.var_utype, font=("Times New Roman", 15), bg="lightyellow").place(x=850, y=230, width=180)
#         cmb_utype=ttk.Combobox(self.root, textvariable=self.var_utype, values=("Admin","Employee"),state='readonly', justify=CENTER, font=("Times New Roman", 13))
#         cmb_utype.place(x=850, y=230, width=180)
#         cmb_utype.current(0)
        
#         #------------row4-----------------#
#         lbl_address = Label(self.root, text="Address:", font=("Times New Roman", 15), bg="white").place(x=50, y=270)
#         lbl_salary = Label(self.root, text="Salary:", font=("Times New Roman", 15), bg="white").place(x=500, y=270)

#         self.txt_address = Text(self.root, font=("Times New Roman", 15), bg="lightyellow")
#         self.txt_address.place(x=150, y=270, width=300, height=65)
#         txt_salary = Entry(self.root, textvariable=self.var_salary, font=("Times New Roman", 15), bg="lightyellow").place(x=600, y=270, width=180)

#         #-----------buttons---------------#
#         btn_add=Button(self.root, text="SAVE", font=("goudy old style", 14, "bold"), bg="#006f80", fg="white", cursor="hand2").place(x=500, y=305, width=110, height=28)
#         btn_update=Button(self.root, text="UPDATE", font=("goudy old style", 14, "bold"), bg="#4caf50", fg="white", cursor="hand2").place(x=620, y=305, width=110, height=28)
#         btn_delete=Button(self.root, text="DELETE", font=("goudy old style", 14, "bold"), bg="#f44336", fg="white", cursor="hand2").place(x=740, y=305, width=110, height=28)
#         btn_clear=Button(self.root, text="CLEAR", font=("goudy old style", 14, "bold"), bg="#607d8b", fg="white", cursor="hand2").place(x=860, y=305, width=110, height=28)

#         #-------------Employee Details-------------------#
#         emp_frame = Frame(self.root, bd=3, relief=RIDGE)
#         emp_frame.place(x=0, y=350, relwidth=1, height=200)

#         scrolly=Scrollbar(emp_frame, orient=VERTICAL)
#         scrollx=Scrollbar(emp_frame, orient=HORIZONTAL)
#         scrollx.config(command=self.EmployeeTable.xview)
#         scrolly.config(command=self.EmployeeTable.yview)
#         self.EmployeeTable=ttk.Treeview(emp_frame, columns=("eid", "name", "email", "gender", "contact", "dob", "doj", "pass", "utype", "address", "salary"), yscrollcommand= scrolly.set, xscrollcommand=scrollx.set)
#         scrollx.pack(side=BOTTOM, fill=X)
#         scrolly.pack(side=RIGHT, fill=Y)

#         self.EmployeeTable.heading("eid", text="EMP ID")
#         self.EmployeeTable.heading("name", text="Name")
#         self.EmployeeTable.heading("email", text="Email")
#         self.EmployeeTable.heading("gender", text="Gender")
#         self.EmployeeTable.heading("contact", text="Contact")
#         self.EmployeeTable.heading("dob", text="D.O.B.")
#         self.EmployeeTable.heading("doj", text="D.O.J.")
#         self.EmployeeTable.heading("pass", text="Password")
#         self.EmployeeTable.heading("utype", text="User Type")
#         self.EmployeeTable.heading("address", text="Address")
#         self.EmployeeTable.heading("salary", text="Salary")
#         self.EmployeeTable["show"]="headings"
#         self.EmployeeTable.column("eid", width=90)
#         self.EmployeeTable.column("name", width=100)
#         self.EmployeeTable.column("gender", width=100)
#         self.EmployeeTable.column("email", width=100)
#         self.EmployeeTable.column("contact", width=100)
#         self.EmployeeTable.column("dob", width=100)
#         self.EmployeeTable.column("doj", width=100)
#         self.EmployeeTable.column("pass", width=100)
#         self.EmployeeTable.column("utype", width=100)
#         self.EmployeeTable.column("address", width=100)
#         self.EmployeeTable.column("salary", width=100)
#         self.EmployeeTable.pack(fill=BOTH,expand=1)

# if __name__ == "__main__":
#     root = Tk()
#     obj = employeeClass(root)
#     root.mainloop()
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3

class employeeClass: 
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x550+220+90")
        self.root.title("Retail Merchandise Management System | Developed by Samyam Sandip")
        self.root.config(bg="white")
        self.root.focus_force()  # to highlight the window of employee whenever the employee button is pressed

        # All Variables
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        self.var_emp_id = StringVar()
        self.var_gender = StringVar()
        self.var_contact = StringVar()
        self.var_name = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_email = StringVar()
        self.var_pass = StringVar()
        self.var_utype = StringVar()  # user type
        self.var_salary = StringVar()

        # Search Frame
        SearchFrame = LabelFrame(self.root, text="Search Employee", bg="white", font=("Baskerville Old Face", 14), bd=3)
        SearchFrame.place(x=250, y=20, width=600, height=70)

        # Dropdown
        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby, values=("Select", "Email", "Name", "Contact"), state='readonly', justify=CENTER, font=("Times New Roman", 13))
        cmb_search.place(x=8, y=8, width=150)
        cmb_search.current(0)  # Select is shown in the dropdown when nothing is selected

        txt_search = Entry(SearchFrame, textvariable=self.var_searchtxt, font=("Times New Roman", 15), bg="lightyellow", width=28)
        txt_search.place(x=170, y=7)
        btn_search = Button(SearchFrame, text="Search", font=("Times New Roman", 14, "italic", "bold"), bg="#008080", fg="white", cursor="hand2")
        btn_search.place(x=465, y=6, width=120, height=30)

        # Title
        title = Label(self.root, text="Employee Details", font=("goudy old style", 15), bg="#0f4d7d", fg="white")
        title.place(x=50, y=100, width=983)

        # Row 1
        lbl_empid = Label(self.root, text="Emp ID:", font=("Times New Roman", 15), bg="white")
        lbl_empid.place(x=50, y=150)
        lbl_gender = Label(self.root, text="  Gender:", font=("Times New Roman", 15), bg="white")
        lbl_gender.place(x=350, y=150)
        lbl_contact = Label(self.root, text="Contact:", font=("Times New Roman", 15), bg="white")
        lbl_contact.place(x=750, y=150)

        txt_empid = Entry(self.root, textvariable=self.var_emp_id, font=("Times New Roman", 15), bg="lightyellow")
        txt_empid.place(x=150, y=150, width=180)
        cmb_gender = ttk.Combobox(self.root, textvariable=self.var_gender, values=("Select", "Male", "Female", "Other"), state='readonly', justify=CENTER, font=("Times New Roman", 13))
        cmb_gender.place(x=500, y=150, width=180)
        cmb_gender.current(0)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("Times New Roman", 15), bg="lightyellow")
        txt_contact.place(x=850, y=150, width=180)

        # Row 2
        lbl_name = Label(self.root, text="Name:", font=("Times New Roman", 15), bg="white")
        lbl_name.place(x=50, y=190)
        lbl_dob = Label(self.root, text="  D.O.B.:", font=("Times New Roman", 15), bg="white")
        lbl_dob.place(x=350, y=190)
        lbl_doj = Label(self.root, text="D.O.J.:", font=("Times New Roman", 15), bg="white")
        lbl_doj.place(x=750, y=190)

        txt_name = Entry(self.root, textvariable=self.var_name, font=("Times New Roman", 15), bg="lightyellow")
        txt_name.place(x=150, y=190, width=180)
        txt_dob = Entry(self.root, textvariable=self.var_dob, font=("Times New Roman", 15), bg="lightyellow")
        txt_dob.place(x=500, y=190, width=180)
        txt_doj = Entry(self.root, textvariable=self.var_doj, font=("Times New Roman", 15), bg="lightyellow")
        txt_doj.place(x=850, y=190, width=180)

        # Row 3
        lbl_email = Label(self.root, text="Email:", font=("Times New Roman", 15), bg="white")
        lbl_email.place(x=50, y=230)
        lbl_pass = Label(self.root, text="  Password:", font=("Times New Roman", 15), bg="white")
        lbl_pass.place(x=350, y=230)
        lbl_utype = Label(self.root, text="User Type:", font=("Times New Roman", 15), bg="white")
        lbl_utype.place(x=750, y=230)

        txt_email = Entry(self.root, textvariable=self.var_email, font=("Times New Roman", 15), bg="lightyellow")
        txt_email.place(x=150, y=230, width=180)
        txt_pass = Entry(self.root, textvariable=self.var_pass, font=("Times New Roman", 15), bg="lightyellow")
        txt_pass.place(x=500, y=230, width=180)
        cmb_utype = ttk.Combobox(self.root, textvariable=self.var_utype, values=("Admin", "Employee"), state='readonly', justify=CENTER, font=("Times New Roman", 13))
        cmb_utype.place(x=850, y=230, width=180)
        cmb_utype.current(0)

        # Row 4
        lbl_address = Label(self.root, text="Address:", font=("Times New Roman", 15), bg="white")
        lbl_address.place(x=50, y=270)
        lbl_salary = Label(self.root, text="Salary:", font=("Times New Roman", 15), bg="white")
        lbl_salary.place(x=500, y=270)

        self.txt_address = Text(self.root, font=("Times New Roman", 15), bg="lightyellow")
        self.txt_address.place(x=150, y=270, width=300, height=65)
        txt_salary = Entry(self.root, textvariable=self.var_salary, font=("Times New Roman", 15), bg="lightyellow")
        txt_salary.place(x=600, y=270, width=180)

        # Buttons
        btn_add = Button(self.root, text="SAVE", command=self.add, font=("goudy old style", 14, "bold"), bg="#006f80", fg="white", cursor="hand2")
        btn_add.place(x=500, y=305, width=110, height=28)
        btn_update = Button(self.root, text="UPDATE", font=("goudy old style", 14, "bold"), bg="#4caf50", fg="white", cursor="hand2")
        btn_update.place(x=620, y=305, width=110, height=28)
        btn_delete = Button(self.root, text="DELETE", font=("goudy old style", 14, "bold"), bg="#f44336", fg="white", cursor="hand2")
        btn_delete.place(x=740, y=305, width=110, height=28)
        btn_clear = Button(self.root, text="CLEAR", font=("goudy old style", 14, "bold"), bg="#607d8b", fg="white", cursor="hand2")
        btn_clear.place(x=860, y=305, width=110, height=28)

        # Employee Details
        emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=0, y=350, relwidth=1, height=200)

        scrolly = Scrollbar(emp_frame, orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)

        self.EmployeeTable = ttk.Treeview(emp_frame, columns=("eid", "name", "email", "gender", "contact", "dob", "doj", "pass", "utype", "address", "salary"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        self.EmployeeTable.pack(fill=BOTH, expand=1)

        self.EmployeeTable.heading("eid", text="EMP ID")
        self.EmployeeTable.heading("name", text="Name")
        self.EmployeeTable.heading("email", text="Email")
        self.EmployeeTable.heading("gender", text="Gender")
        self.EmployeeTable.heading("contact", text="Contact")
        self.EmployeeTable.heading("dob", text="D.O.B.")
        self.EmployeeTable.heading("doj", text="D.O.J.")
        self.EmployeeTable.heading("pass", text="Password")
        self.EmployeeTable.heading("utype", text="User Type")
        self.EmployeeTable.heading("address", text="Address")
        self.EmployeeTable.heading("salary", text="Salary")
        self.EmployeeTable["show"] = "headings"

        self.EmployeeTable.column("eid", width=90)
        self.EmployeeTable.column("name", width=100)
        self.EmployeeTable.column("email", width=100)
        self.EmployeeTable.column("gender", width=100)
        self.EmployeeTable.column("contact", width=100)
        self.EmployeeTable.column("dob", width=100)
        self.EmployeeTable.column("doj", width=100)
        self.EmployeeTable.column("pass", width=100)
        self.EmployeeTable.column("utype", width=100)
        self.EmployeeTable.column("address", width=100)
        self.EmployeeTable.column("salary", width=100)

        self.EmployeeTable.pack(fill=BOTH, expand=1)
        self.EmployeeTable.bind("<ButtonRelease-1>", self.get_data)

        
        self.show()

#----------------------------------------#
    def add(self):
        con= sqlite3.connect(database=r'rmms.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error", "Employee ID must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM employee WHERE eid=?", (self.var_emp_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error", "This Employee ID already assigned, try different.", parent=self.root)
                else:
                    cur.execute("INSERT INTO employee(eid, name, email, gender, contact, dob, doj, pass, utype, address, salary) values(?,?,?,?,?,?,?,?,?,?,?)",(
                        self.var_emp_id.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_contact.get(),
                        self.var_dob.get(),
                        self.var_doj.get(),
                        self.var_pass.get(),
                        self.var_utype.get(), 
                        self.txt_address.get('1.0',END),
                        self.var_salary.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Employee Added Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}", parent=self.root)

    def show(self):
        con=sqlite3.connect(database=r'rmms.db')
        cur=con.cursor()
        try:
            cur.execute("SELECT * FROM employee")
            rows = cur.fetchall()
            if len(rows)>0:
                self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                for row in rows:
                    self.EmployeeTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}", parent=self.root)
    
    def get_data(self, ev):
        
if __name__ == "__main__": 
    root = Tk()
    obj = employeeClass(root)
    root.mainloop()