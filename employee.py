from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
class employeeClass: 
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Retail Merchandise Management System | Developed by Samyam Sandip")
        self.root.config(bg="white")
        self.root.focus_force() #to highlight the window of employee whenever the employee button is pressed

        #------------------searchFrame----------------------#
        SearchFrame=LabelFrame(self.root, text="Search Employee", bg="white", font=("Baskerville Old Face", 13), bd=3)
        SearchFrame.place(x=250, y=20, width=600, height=70)

        #--------------------dropdown----------------------#
        cmb_search=ttk.Combobox(SearchFrame, values=("Select","Email","Name","Contact","ID"),state='readonly', justify=CENTER, font=("Arial", 13))
        cmb_search.place(x=8, y=8, width=150)
        cmb_search.current(0) #Select is shown in the dropdown when nothing is selected
if __name__ == "__main__":
    root = Tk()
    obj = employeeClass(root)
    root.mainloop()