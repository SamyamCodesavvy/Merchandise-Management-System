from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3

class supplierClass: 
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x550+220+90")
        self.root.title("Retail Merchandise Management System | Developed by Samyam Sandip")
        self.root.config(bg="white")
        self.root.focus_force()  # to highlight the window of employee whenever the employee button is pressed

        # All Variables
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        self.var_sup_invoice = StringVar()
        self.var_contact = StringVar()
        self.var_name = StringVar()
    

    
        #=====options========#
        lbl_search = Label(self.root, text="Search by Invoice No.:" , bg="white", font=("Times New Roman", 13))
        lbl_search.place(x=665, y=80)

        txt_search = Entry(self.root, textvariable=self.var_searchtxt, font=("Times New Roman", 15), bg="lightyellow", width=14)
        txt_search.place(x=830, y=80)
        btn_search = Button(self.root, text="Search", command=self.search, font=("Times New Roman", 14, "italic", "bold"), bg="#008080", fg="white", cursor="hand2")
        btn_search.place(x=980, y=78,width=65, height=30)

        # Title
        title = Label(self.root, text="Supplier Details", font=("goudy old style", 18, "bold"), bg="#0f4d7d", fg="white", bd=4, relief=RIDGE)
        title.place(x=50, y=10, width=998, height=43)

        # Row 1
        lbl_supplier_invoice = Label(self.root, text="Invoice No.:", font=("Times New Roman", 14), bg="white")
        lbl_supplier_invoice.place(x=50, y=80)
        txt_supplier_invoice = Entry(self.root, textvariable=self.var_sup_invoice, font=("Times New Roman", 15), bg="lightyellow")
        txt_supplier_invoice.place(x=180, y=80, width=180)
        

        # Row 2
        lbl_name = Label(self.root, text="Name:", font=("Times New Roman", 14), bg="white")
        lbl_name.place(x=50, y=120)
        txt_name = Entry(self.root, textvariable=self.var_name, font=("Times New Roman", 15), bg="lightyellow")
        txt_name.place(x=180, y=120, width=180)

        # Row 3
        lbl_contact = Label(self.root, text="Contact:", font=("Times New Roman", 14), bg="white")
        lbl_contact.place(x=50, y=160)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("Times New Roman", 15), bg="lightyellow")
        txt_contact.place(x=180, y=160, width=180)
        

        # Row 4
        lbl_desc = Label(self.root, text="Description:", font=("Times New Roman", 14), bg="white")
        lbl_desc.place(x=50, y=200)

        self.txt_desc = Text(self.root, font=("Times New Roman", 15), bg="lightyellow")
        self.txt_desc.place(x=180, y=200, width=470, height=90)

        # Buttons
        btn_add = Button(self.root, text="SAVE", command=self.add, font=("goudy old style", 14, "bold"), bg="#006f80", fg="white", cursor="hand2")
        btn_add.place(x=180, y=320, width=110, height=28)
        btn_update = Button(self.root, text="UPDATE", command=self.update, font=("goudy old style", 14, "bold"), bg="#4caf50", fg="white", cursor="hand2")
        btn_update.place(x=300, y=320, width=110, height=28)
        btn_delete = Button(self.root, text="DELETE", command=self.delete, font=("goudy old style", 14, "bold"), bg="#f44336", fg="white", cursor="hand2")
        btn_delete.place(x=420, y=320, width=110, height=28)
        btn_clear = Button(self.root, text="CLEAR", command=self.clear, font=("goudy old style", 14, "bold"), bg="#607d8b", fg="white", cursor="hand2")
        btn_clear.place(x=540, y=320, width=110, height=28)

        # Employee Details
        emp_frame = Frame(self.root, bd=3, relief=RIDGE)
        emp_frame.place(x=665, y=130, width=380, height=380)

        scrolly = Scrollbar(emp_frame, orient=VERTICAL)
        scrollx = Scrollbar(emp_frame, orient=HORIZONTAL)

        self.supplierTable = ttk.Treeview(emp_frame, columns=("invoice", "name", "contact", "desc"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set, show="headings")
        scrollx.config(command=self.supplierTable.xview)
        scrolly.config(command=self.supplierTable.yview)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        self.supplierTable.pack(fill=BOTH, expand=1)

        self.supplierTable.heading("invoice", text="Invoice No.")
        self.supplierTable.heading("name", text="Name")
        self.supplierTable.heading("contact", text="Contact")
        self.supplierTable.heading("desc", text="Description")
        self.supplierTable["show"] = "headings"
        self.supplierTable.column("invoice", width=90)
        self.supplierTable.column("name", width=100)
        self.supplierTable.column("contact", width=100)
        self.supplierTable.column("desc", width=100)
        

        self.supplierTable.pack(fill=BOTH, expand=1)
        self.supplierTable.bind("<ButtonRelease-1>", self.get_data)

        
        self.show()

#----------------------------------------#
    def add(self):
        con= sqlite3.connect(database=r'rmms.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error", "Invoice must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM supplier WHERE invoice=?", (self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error", "This Invoice No. is already assigned, try different.", parent=self.root)
                else:
                    cur.execute("INSERT INTO supplier(invoice, name, contact, desc) values(?,?,?,?)",(
                        self.var_sup_invoice.get(),
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.txt_desc.get('1.0',END),
                        
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Supplier Added Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}", parent=self.root)

    def show(self):
        con=sqlite3.connect(database=r'rmms.db')
        cur=con.cursor()
        try:
            cur.execute("SELECT * FROM supplier")
            rows = cur.fetchall()
            self.supplierTable.delete(*self.supplierTable.get_children())
            for row in rows:
                self.supplierTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}", parent=self.root)
    
    def get_data(self, ev):
        f = self.supplierTable.focus()
        content = self.supplierTable.item(f)
        row = content['values']
        self.var_sup_invoice.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[2])
        self.txt_desc.delete('1.0',END)
        self.txt_desc.insert(END, row[3])

    def update(self):
        con= sqlite3.connect(database=r'rmms.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error", "Invoice No. must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM supplier WHERE invoice=?", (self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Invoice No.", parent=self.root)
                else:
                    cur.execute("UPDATE supplier SET name=?, contact=?, desc=? WHERE invoice = ?",(
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.txt_desc.get('1.0',END),
                        self.var_sup_invoice.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Supplier Updated Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}", parent=self.root)
        
    def delete(self):
        con= sqlite3.connect(database=r'rmms.db')
        cur=con.cursor()
        try:
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error", "Invoice no. must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM supplier WHERE invoice=?", (self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Invoice No.", parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm", "Do you really want to delete?", parent =self.root)
                    if op == True:

                        cur.execute("DELETE FROM supplier WHERE invoice=?",(self.var_sup_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Supplier Deleted Successfully", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def clear(self):
        self.var_sup_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("") 
        self.txt_desc.delete('1.0',END)
        self.var_searchtxt.set("")
        self.show()
    
    def search(self):
        con=sqlite3.connect(database=r'rmms.db')
        cur=con.cursor()
        try:
            if self.var_searchtxt.get()=="":
                messagebox.showerror("Error", "Invoice No. is required.", parent=self.root)
            else:
                cur.execute("SELECT * FROM supplier WHERE invoice=?", (self.var_searchtxt.get(),))
                row = cur.fetchone()
                if row!=None:
                    self.supplierTable.delete(*self.supplierTable.get_children())
                    self.supplierTable.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record found!!!", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}", parent=self.root)
        
if __name__ == "__main__": 
    root = Tk()
    obj = supplierClass(root)
    root.mainloop()