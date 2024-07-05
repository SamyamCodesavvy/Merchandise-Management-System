from tkinter import *
from PIL import Image, ImageTk
import time
class RMMS: #retail merchandise management system
    def __init__(self, root):
        # icon_path = 'images/title_icon.ico'  
        # root.iconbitmap(icon_path)
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Retail Merchandise Management System | Developed by Samyam Sandip")
        self.root.config(bg="white")

        #-------Title-------#
        self.icon_title = PhotoImage(file="images\cart.png")
        title = Label(self.root, text="SS Shopping Mart Merchandise Management System", image=self.icon_title, compound=LEFT, font=("Times New Roman", 30, "bold"), bg="#003f66", fg="#ccffff", anchor="w", padx=7).place(x=0, y=0, relwidth=1, height=75)

        #-------Logout Button-------#
        btn_logout = Button(self.root,text="Logout", font=("Times New Roman", 17, "bold"), bg="#ccffff", cursor="hand2").place(x=1375, y=13, width=150, height=50)
        
        #-------Timestamp---------#
        self.lbl_clock = Label(self.root, text="Welcome to Digital Merchandise Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS", font=("Times New Roman", 15, "italic", "bold"), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0, y=75, relwidth=1, height=30)
        self.update_clock()

        #-------Left Menu----------#
        self.MenuLogo=Image.open("images/menu_image.png")
        self.MenuLogo=self.MenuLogo.resize((250,220),Image.LANCZOS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

        LeftMenu=Frame(self.root, bd=2, relief=RIDGE, bg="white")
        LeftMenu.place(x=2, y=108, width=250, height=682)

        lbl_menuLogo=Label(LeftMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP, fill=X)

        self.icon_side = Image.open("images\sidemenu.png")
        self.icon_side=self.icon_side.resize((35,35),Image.LANCZOS)
        self.icon_side=ImageTk.PhotoImage(self.icon_side)

        lbl_menu = Label(LeftMenu,text="MENU", font=("Times New Roman", 20, "bold"), bg="#009688", fg="white")
        lbl_menu.pack(side=TOP, fill=X)
        btn_employee = Button(LeftMenu,text="Employees", font=("Arial", 17, "bold"), image=self.icon_side, compound=LEFT, padx=10, pady=11, anchor="w",bg="white", bd=2,cursor="hand2")
        btn_employee.pack(side=TOP, pady=2, fill=X)

        btn_supplier = Button(LeftMenu,text="Suppliers", font=("Arial", 17, "bold"), image=self.icon_side, compound=LEFT, padx=10, pady=11, anchor="w",bg="white", bd=2,cursor="hand2")
        btn_supplier.pack(side=TOP, pady=2, fill=X)

        btn_category = Button(LeftMenu,text="Categories", font=("Arial", 17, "bold"), image=self.icon_side, compound=LEFT, padx=10, pady=11, anchor="w",bg="white", bd=2,cursor="hand2")
        btn_category.pack(side=TOP, pady=2, fill=X)

        btn_product = Button(LeftMenu,text="Products", font=("Arial", 17, "bold"), image=self.icon_side, compound=LEFT, padx=10, pady=11, anchor="w",bg="white", bd=2,cursor="hand2")
        btn_product.pack(side=TOP, pady=2, fill=X)

        btn_sales = Button(LeftMenu,text="Sales", font=("Arial", 17, "bold"), image=self.icon_side, compound=LEFT, padx=10, pady=11, anchor="w",bg="white", bd=2,cursor="hand2")
        btn_sales.pack(side=TOP, pady=2, fill=X)

        btn_exit = Button(LeftMenu,text="Exit", font=("Arial", 17, "bold"), image=self.icon_side, compound=LEFT, padx=10, pady=11, anchor="w",bg="white", bd=2,cursor="hand2")
        btn_exit.pack(side=TOP, pady=2, fill=X)
        
        #----------content---------------#
        self.lbl_employee= Label(self.root, text="Total Employees\n[ 0 ]", bd=5, relief=RIDGE, bg="#008080", fg="white", font=("Baskerville Old Face", 20, "bold"))
        self.lbl_employee.place(x=345, y=135, height=150, width=300)

        self.lbl_category= Label(self.root, text="Total Categories\n[ 0 ]", bd=5, relief=RIDGE, bg="#008080", fg="white", font=("Baskerville Old Face", 20, "bold"))
        self.lbl_category.place(x=745, y=135, height=150, width=300)

        self.lbl_product= Label(self.root, text="Total Products\n[ 0 ]", bd=5, relief=RIDGE, bg="#008080", fg="white", font=("Baskerville Old Face", 20, "bold"))
        self.lbl_product.place(x=1145, y=135, height=150, width=300)

        self.lbl_supplier= Label(self.root, text="Total Suppliers\n[ 0 ]", bd=5, relief=RIDGE, bg="#006f80", fg="white", font=("Baskerville Old Face", 20, "bold"))
        self.lbl_supplier.place(x=545, y=320, height=150, width=300)
    
        self.lbl_sales= Label(self.root, text="Total Sales\n[ 0 ]", bd=5, relief=RIDGE, bg="#006f80", fg="white", font=("Baskerville Old Face", 20, "bold"))
        self.lbl_sales.place(x=945, y=320, height=150, width=300)

        #----------dashboard image---------------#
        db_image_path = "images/dashboard_image.png"
        dashboard_img = Image.open(db_image_path)
        dashboard_img = dashboard_img.resize((640, 295), Image.LANCZOS)
        self.dashboard_photo = ImageTk.PhotoImage(dashboard_img)
        self.dashboard_image_label = Label(self.root, image=self.dashboard_photo)
        self.dashboard_image_label.place(x=251, y=500)

        # Load and display the second image
        clothing_img_path = "images/dashboard_clothing_image.png"
        clothing_img = Image.open(clothing_img_path)
        clothing_img = clothing_img.resize((642, 295), Image.LANCZOS)
        self.clothing_photo = ImageTk.PhotoImage(clothing_img)
        self.clothing_image_label = Label(self.root, image=self.clothing_photo)
        self.clothing_image_label.place(x=890, y=500)

        #---------footer--------#
        lbl_footer = Label(self.root, text="Digital Merchandise Management System | Developed by Samyam Sandip\nFor any Technical Issue, Contact: 98xxxxxxx0", font=("Times New Roman", 15), bg="#4d636d", fg="white") 
        lbl_footer.pack(side=BOTTOM, fill=X)

    def update_clock(self):
        now = time.strftime("%d-%m-%Y %H:%M:%S")
        self.lbl_clock.config(text=f"Welcome to Digital Merchandise Management System\t\t Date: {now.split()[0]}\t\t Time: {now.split()[1]}")
        self.root.after(1000, self.update_clock)  # Update every second

if __name__ == "__main__":
    root = Tk()
    obj = RMMS(root)
    root.mainloop()
