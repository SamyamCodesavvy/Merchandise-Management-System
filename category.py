from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3

class categoryClass: 
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x550+220+90")
        self.root.title("Retail Merchandise Management System | Developed by Samyam Sandip")
        self.root.config(bg="white")
        self.root.focus_force()
        #============variables================#
        self.var_cat_id = StringVar()
        self.var_name = StringVar()
    
        #===========TITLE================
        lbl_title = Label(self.root, text="Manage Product Category", font=("goudy old style", 20, "bold"), bg="#184a45", fg="white", bd=3, relief=RIDGE)
        lbl_title.pack(side=TOP, fill=X, padx=20, pady=20)

        lbl_name = Label(self.root, text="Enter Category Name:", font=("Times New Roman", 16, "italic"), bg="white")
        lbl_name.place(x=50, y=100)
        
        txt_name = Entry(self.root, textvariable=self.var_name, font=("Times New Roman", 16), bg="lightyellow")
        txt_name.place(x=50, y=150, width=300)

        btn_add = Button(self.root, text="ADD", command=self.add, font=("goudy old style", 15, "bold"), bg="#008080", fg="white", cursor="hand2")
        btn_add.place(x=355, y=148, width=120, height=30)
        
        btn_delete = Button(self.root, text="DELETE", command=self.delete, font=("goudy old style", 15, "bold"), bg="#c7313d", fg="white", cursor="hand2")
        btn_delete.place(x=485, y=148, width=120, height=30)

        #=========Category Details============#
        cat_frame = Frame(self.root, bd=3, relief=RIDGE)
        cat_frame.place(x=675, y=100, width=380, height=360)

        scrolly = Scrollbar(cat_frame, orient=VERTICAL)
        scrollx = Scrollbar(cat_frame, orient=HORIZONTAL)

        self.category_table = ttk.Treeview(cat_frame, columns=("cid", "name"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set, show="headings")
        scrollx.config(command=self.category_table.xview)
        scrolly.config(command=self.category_table.yview)

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        self.category_table.pack(fill=BOTH, expand=1)

        self.category_table.heading("cid", text="Cat. ID")
        self.category_table.heading("name", text="Name")
        self.category_table.column("cid", width=90)
        self.category_table.column("name", width=100)
        self.category_table.bind("<ButtonRelease-1>", self.get_data)
        
        #=========Image==============#
        img_path = "images/category_window_pic.png"
        img = Image.open(img_path)
        img = img.resize((552, 330), Image.LANCZOS)
        self.image = ImageTk.PhotoImage(img)
        
        # Adjust the placement if needed
        img_label = Label(self.root, image=self.image)
        img_label.place(x=50, y=190)  

        # Display the categories when the window is opened
        self.show()

    #===================Functions=============#
    def add(self):
        con = sqlite3.connect(database=r'rmms.db')
        cur = con.cursor()
        try:
            if self.var_name.get() == "":
                messagebox.showerror("Error", "Category name should be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM category WHERE name=?", (self.var_name.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "This Category is already present in the database, try different.", parent=self.root)
                else:
                    cur.execute("INSERT INTO category(name) values(?)", (self.var_name.get(),))
                    con.commit()
                    messagebox.showinfo("Success", "Category Added Successfully", parent=self.root)
                    self.show()  # Update the table after adding
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
    
    def show(self):
        con = sqlite3.connect(database=r'rmms.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM category")
            rows = cur.fetchall()
            if len(rows) > 0:
                self.category_table.delete(*self.category_table.get_children())
                for row in rows:
                    self.category_table.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def get_data(self, ev):
        f = self.category_table.focus()
        content = self.category_table.item(f)
        row = content['values']
        self.var_cat_id.set(row[0])
        self.var_name.set(row[1])

    def delete(self):
        con= sqlite3.connect(database=r'rmms.db')
        cur=con.cursor()
        try:
            if self.var_cat_id.get()=="":
                messagebox.showerror("Error", "Please select or enter a category name from the list.", parent=self.root)
            else:
                cur.execute("SELECT * FROM category WHERE cid=?", (self.var_cat_id.get(),))
                row=cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Please Try Again!", parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm", "Do you really want to delete?", parent =self.root)
                    if op == True:

                        cur.execute("DELETE FROM category WHERE cid=?",(self.var_cat_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Category Deleted Successfully", parent=self.root)
                        self.show()
                        self.var_cat_id.set("")
                        self.var_name.set("")
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to : {str(ex)}", parent=self.root)

if __name__ == "__main__": 
    root = Tk()
    obj = categoryClass(root)
    root.mainloop()
