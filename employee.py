from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk

class employeeClass: 
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+90")
        self.root.title("Retail Merchandise Management System | Developed by Samyam Sandip")
        self.root.config(bg="white")
        self.root.focus_force() #to highlight the window of employee whenever the employee button is pressed

        #------------------searchFrame----------------------#
        SearchFrame=LabelFrame(self.root, text="Search Employee", bg="white", font=("Baskerville Old Face", 14), bd=3)
        SearchFrame.place(x=250, y=20, width=600, height=70)

        #--------------------dropdown----------------------#
        cmb_search=ttk.Combobox(SearchFrame, values=("Select","Email","Name","Contact"),state='readonly', justify=CENTER, font=("Times New Roman", 13))
        cmb_search.place(x=8, y=8, width=150)
        cmb_search.current(0) #Select is shown in the dropdown when nothing is selected

        txt_search=Entry(SearchFrame, font=("Times New Roman", 15), bg="lightyellow", width=28).place(x=170, y=7)
        btn_search=Button(SearchFrame, text="Search", font=("Times New Roman", 14, "italic", "bold"), bg="#008080", fg="white", cursor="hand2").place(x=465, y=6, width=120, height=30)
if __name__ == "__main__":
    root = Tk()
    obj = employeeClass(root)
    root.mainloop()