from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3

class productClass: 
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x550+220+90")
        self.root.title("Retail Merchandise Management System | Developed by Samyam Sandip")
        self.root.config(bg="white")
        self.root.focus_force()
        #===============================
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        self.cat_list=[]
        self.sup_list=[]
        self.fetch_cat_sup()


        self.var_cat = StringVar()
        self.var_sup = StringVar()
        self.var_name = StringVar()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_status = StringVar()


        product_Frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        product_Frame.place(x=10, y=10, width=450, height=530)

        title = Label(product_Frame, text="Manage Product Details", font=("goudy old style", 17, "bold"), bg="#0f4d7d", fg="white")
        title.pack(side=TOP, fill=X)

        #================column1=====================

        lbl_category = Label(product_Frame, text="Category:", font=("Times New Roman", 16), bg="white")
        lbl_category.place(x=30, y=60)
        lbl_supplier = Label(product_Frame, text="Supplier:", font=("Times New Roman", 16), bg="white")
        lbl_supplier.place(x=30, y=110)
        lbl_product_name = Label(product_Frame, text="Name:", font=("Times New Roman", 16), bg="white")
        lbl_product_name.place(x=30, y=160)
        lbl_price = Label(product_Frame, text="Price:", font=("Times New Roman", 16), bg="white")
        lbl_price.place(x=30, y=210)
        lbl_qty = Label(product_Frame, text="Quantity:", font=("Times New Roman", 16), bg="white")
        lbl_qty.place(x=30, y=260)
        lbl_status = Label(product_Frame, text="Status:", font=("Times New Roman", 16), bg="white")
        lbl_status.place(x=30, y=310)

        #=================column2==================#
        cmb_cat = ttk.Combobox(product_Frame, textvariable=self.cat_list, values=("Select"), state='readonly', justify=CENTER, font=("Times New Roman", 13))
        cmb_cat.place(x=150, y=60, width=200)
        cmb_cat.current(0)

        cmb_sup = ttk.Combobox(product_Frame, textvariable=self.sup_list, values=("Select"), state='readonly', justify=CENTER, font=("Times New Roman", 13))
        cmb_sup.place(x=150, y=110, width=200)
        # cmb_sup.current(0)

        txt_name = Entry(product_Frame, textvariable=self.var_name, font=("Times New Roman", 13), bg="lightyellow").place(x=150, y=160, width=200)
        txt_price = Entry(product_Frame, textvariable=self.var_price, font=("Times New Roman", 13), bg="lightyellow").place(x=150, y=210, width=200)
        txt_qty = Entry(product_Frame, textvariable=self.var_qty, font=("Times New Roman", 13), bg="lightyellow").place(x=150, y=260, width=200)

        cmb_status = ttk.Combobox(product_Frame, textvariable=self.var_status, values=("Active", "Inactive"), state='readonly', justify=CENTER, font=("Times New Roman", 13))
        cmb_status.place(x=150, y=310, width=200)
        cmb_status.current(0)

        #=========buttons===============
        btn_add = Button(product_Frame, text="SAVE", command=self.add, font=("goudy old style", 14, "bold"), bg="#006f80", fg="white", cursor="hand2")
        btn_add.place(x=10, y=400, width=95, height=32)
        btn_update = Button(product_Frame, text="UPDATE", command=self.update, font=("goudy old style", 14, "bold"), bg="#4caf50", fg="white", cursor="hand2")
        btn_update.place(x=120, y=400, width=95, height=32)
        btn_delete = Button(product_Frame, text="DELETE", command=self.delete, font=("goudy old style", 14, "bold"), bg="#f44336", fg="white", cursor="hand2")
        btn_delete.place(x=230, y=400, width=95, height=32)
        btn_clear = Button(product_Frame, text="CLEAR", command=self.clear, font=("goudy old style", 14, "bold"), bg="#607d8b", fg="white", cursor="hand2")
        btn_clear.place(x=340, y=400, width=95, height=32)

        # ==========Search Frame===========
        SearchFrame = LabelFrame(self.root, text="Search Employee", bg="white", font=("Baskerville Old Face", 14), bd=3)
        SearchFrame.place(x=480, y=10, width=600, height=80)

        # ======options=========
        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby, values=("Select", "Category", "Supplier", "Name"), state='readonly', justify=CENTER, font=("Times New Roman", 13))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)  # Select is shown in the dropdown when nothing is selected

        txt_search = Entry(SearchFrame, textvariable=self.var_searchtxt, font=("Times New Roman", 15), bg="lightyellow", width=25)
        txt_search.place(x=200, y=9)
        btn_search = Button(SearchFrame, text="Search", command=self.search, font=("Times New Roman", 14, "italic", "bold"), bg="#008080", fg="white", cursor="hand2")
        btn_search.place(x=465, y=6, width=120, height=30)


        # =========Product Details==========
        p_frame = Frame(self.root, bd=3, relief=RIDGE)
        p_frame.place(x=480, y=100, width=600, height=390)

        scrolly = Scrollbar(p_frame, orient=VERTICAL)
        scrollx = Scrollbar(p_frame, orient=HORIZONTAL)

        self.product_table = ttk.Treeview(p_frame, columns=("pid", "Category", "Supplier", "name", "price", "qty", "status"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.config(command=self.product_table.xview)
        scrolly.config(command=self.product_table.yview)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        self.product_table.pack(fill=BOTH, expand=1)

        self.product_table.heading("pid", text="P ID")
        self.product_table.heading("Category", text="Category")
        self.product_table.heading("Supplier", text="Supplier")
        self.product_table.heading("name", text="Name")
        self.product_table.heading("price", text="Price")
        self.product_table.heading("qty", text="Qty")
        self.product_table.heading("status", text="Status")
        self.product_table["show"] = "headings"

        self.product_table.column("pid", width=90)
        self.product_table.column("Category", width=100)
        self.product_table.column("Supplier", width=100)
        self.product_table.column("name", width=100)
        self.product_table.column("price", width=100)
        self.product_table.column("qty", width=100)
        self.product_table.column("status", width=100)
        

        self.product_table.pack(fill=BOTH, expand=1)
        self.product_table.bind("<ButtonRelease-1>", self.get_data)

        
        self.show()

#---------------functions-------------------------#
    def fetch_cat_sup(self):
        con= sqlite3.connect(database=r'rmms.db')
        cur=con.cursor()
        try:
            cur.execute("SELECT name FROM category")
            cat=cur.fetchall()
            self.cat_list.append("Empty")
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[0])
            cur.execute("SELECT name from supplier")
            sup=cur.fetchall()
            print(sup)


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}", parent=self.root)
    def add(self):
        con= sqlite3.connect(database=r'rmms.db')
        cur=con.cursor()
        try:
            if self.var_cat.get()=="Select" or self.var_sup.get()=="Select" or self.var_name.get()=="":
                messagebox.showerror("Error", "All fields are required.", parent=self.root)
            else:
                cur.execute("SELECT * FROM product WHERE name=?", (self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error", "Product already present, try different.", parent=self.root)
                else:
                    cur.execute("INSERT INTO product(Category, Supplier, name, price, qty, status) values(?,?,?,?,?,?)",(
                        self.var_cat.get(),
                        self.var_sup.get(),
                        self.var_name.get(),
                        self.var_price.get(),
                        self.var_qty.get(),
                        self.var_dob.get(),
                        self.var_doj.get(),
                        self.var_pass.get(),
                        self.var_utype.get(), 
                        self.txt_address.get('1.0',END),
                        self.var_salary.get(),
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
            cur.execute("SELECT * FROM product")
            rows = cur.fetchall()
            if len(rows)>0:
                self.product_table.delete(*self.product_table.get_children())
                for row in rows:
                    self.product_table.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}", parent=self.root)
    
    def get_data(self, ev):
        f = self.product_table.focus()
        content = self.product_table.item(f)
        row = content['values']
        self.var_emp_id.set(row[0]),
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_contact.set(row[4]),
        self.var_dob.set(row[5]),
        self.var_doj.set(row[6]),
        self.var_pass.set(row[7]),
        self.var_utype.set(row[8]), 
        self.txt_address.delete('1.0',END),
        self.txt_address.insert(END, row[9]),
        self.var_salary.set(row[10])

    def update(self):
        con= sqlite3.connect(database=r'rmms.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error", "Employee ID must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM employee WHERE eid=?", (self.var_emp_id.get(),))
                row=cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Employee ID.", parent=self.root)
                else:
                    cur.execute("UPDATE employee SET name=?, email=?, gender=?, contact=?, dob=?, doj=?, pass=?, utype=?, address=?, salary=? WHERE eid = ?",(
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_contact.get(),

                        self.var_dob.get(),
                        self.var_doj.get(),

                        self.var_pass.get(),
                        self.var_utype.get(), 
                        self.txt_address.get('1.0',END),
                        self.var_salary.get(),
                        self.var_emp_id.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Employee Updated Successfully", parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}", parent=self.root)
        
    def delete(self):
        con= sqlite3.connect(database=r'rmms.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error", "Employee ID must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM employee WHERE eid=?", (self.var_emp_id.get(),))
                row=cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Employee ID.", parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm", "Do you really want to delete?", parent =self.root)
                    if op == True:

                        cur.execute("DELETE FROM employee WHERE eid=?",(self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Employee Deleted Successfully", parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

    def clear(self):
        self.var_emp_id.set(""),
        self.var_name.set(""),
        self.var_email.set(""),
        self.var_gender.set("Select"),
        self.var_contact.set(""),
        self.var_dob.set(""),
        self.var_doj.set(""),
        self.var_pass.set(""),
        self.var_utype.set("Admin"), 
        self.txt_address.delete('1.0',END),
        self.var_salary.set("")
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.show()
    
    def search(self):
        con=sqlite3.connect(database=r'rmms.db')
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error", "No Search By option selected.", parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error", "Search input is required.", parent=self.root)
            else:
                cur.execute("SELECT * FROM employee WHERE "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows = cur.fetchall()
                if len(rows)!=0:
                    self.product_table.delete(*self.product_table.get_children())
                    for row in rows:
                        self.product_table.insert('', END, values=row)
                else:
                    messagebox.showerror("Error", "No record found!!!", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}", parent=self.root) 
                      
if __name__ == "__main__": 
    root = Tk()
    obj = productClass(root)
    root.mainloop()