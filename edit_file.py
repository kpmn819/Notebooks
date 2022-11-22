# OBJECT ORIENTED DEMO
from cgitb import text
import os
import csv
import tkinter as tk
from tkinter import ttk



class App(tk.Tk):
    global files
    files =[]
    for file in os.listdir("."):
        if file.endswith(".csv"):
            #print(os.path.join("/mydir", file))
            files.append(file)
    print(files)
    

    def __init__(self):
        super().__init__()

        self.geometry("1000x600")
        self.title('Edit Files')
        self.resizable(0, 0)

        # configure the grid
        self.columnconfigure((0,1,2,3), weight=1)
        self.rowconfigure((0,1,2,3,4), weight=1)
        tl_frame = tk.Frame(self)
        tl_frame.configure(height=100, width=400, border=2, relief='raised')
        tl_frame.grid(column=0,row=0,columnspan=1, rowspan=1, sticky=tk.NW + tk.SE,padx=20,pady=5)
        # this will be the container for the file contents
        mid_frame = tk.Frame(self)
        mid_frame.configure(height=100, width=400, border=2, relief='raised')
        mid_frame.grid(column=0,row=1,columnspan=4, rowspan=1, sticky=tk.NW + tk.SE,padx=20,pady=5)

        temp_list = ('Java', 'C#', 'C', 'C++', 'Python','Go', 'JavaScript', 'PHP', 'Swift')
        temp_var = tk.StringVar(value=temp_list)
        file_lb = tk.Listbox(mid_frame,
        listvariable= temp_var,
        height=6,selectmode='extended')
        


        file_lb.grid(
            column=0,
            row=0,
            sticky='nwes', columnspan=3
            )


        sel_label = tk.Label(tl_frame, text='Select File')
        sel_label.grid(column=0, row=0, padx=5, pady=5)
        
        #self.columnconfigure(1, weight=3)





        # Before this happens we need the file choice that means that selection has to show first
        #self.create_widgets()

    def create_widgets(self):
        # username
        username_label = ttk.Label(self, text="Username:")
        username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        username_entry = ttk.Entry(self)
        username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

        # password
        password_label = ttk.Label(self, text="Password:")
        password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

        password_entry = ttk.Entry(self,  show="*")
        password_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

        # login button
        login_button = ttk.Button(self, text="Login")
        login_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)


if __name__ == "__main__":
    app = App()
    app.mainloop()