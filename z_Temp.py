import tkinter as tk 
from tkinter import *
from tkinter import ttk 


root = Tk()
frame = tk.Frame(root, bg='#3498db')
frame_btns = tk.Frame(frame, bg='#3498db')

data = [
        [1,"AAA","BBB","ab@mail.com",17],
        [3,"EEE","FFF","ef@mail.com",91],
        [4,"GGG","HHH","gh@mail.com",47],
        [7,"MMM","NNN","mn@mail.com",25],
        [8,"PPP","QQQ","pq@mail.com",43],
        [9,"RRR","SSS","rs@mail.com",94],
       ]

label_id = tk.Label(frame, text='ID:', font=('verdana',14), bg='#3498db')
entry_id = tk.Entry(frame, font=('verdana',14))

label_fname = tk.Label(frame, text='First Name:', font=('verdana',14), bg='#3498db')
entry_fname = tk.Entry(frame, font=('verdana',14))

label_lname = tk.Label(frame, text='Last Name:', font=('verdana',14), bg='#3498db')
entry_lname = tk.Entry(frame, font=('verdana',14))

label_email = tk.Label(frame, text='Email:', font=('verdana',14), bg='#3498db')
entry_email = tk.Entry(frame, font=('verdana',14))

label_age = tk.Label(frame, text='Age:', font=('verdana',14), bg='#3498db')
entry_age = tk.Entry(frame, font=('verdana',14))

btn_add = tk.Button(frame_btns, text='Add', font=('verdana',14), bg='#f39c12',
                    fg='#ffffff', width=10)
btn_edit = tk.Button(frame_btns, text='Edit', font=('verdana',14), bg='#f39c12',
                     fg='#ffffff', width=10)
btn_remove = tk.Button(frame_btns, text='Remove', font=('verdana',14), bg='#f39c12',
                       fg='#ffffff', width=10)

trv = ttk.Treeview(frame, columns=(1,2,3,4,5), show='headings')
trv.column(1, anchor='center', width=100)
trv.column(2, anchor='center', width=100)
trv.column(3, anchor='center', width=100)
trv.column(4, anchor='center', width=100)
trv.column(5, anchor='center', width=100)

trv.heading(1, text='ID')
trv.heading(2, text='First Name')
trv.heading(3, text='Last Name')
trv.heading(4, text='Email')
trv.heading(5, text='Age')

# create a function to display data in treeview
def displayData():
    for row in data:
        trv.insert('',END, values=row)


displayData()


# create a function to display the selected row from treeview
def displaySelectedItem(a):

    # clear entries
    entry_id.delete(0,END)
    entry_fname.delete(0,END)
    entry_lname.delete(0,END)
    entry_email.delete(0,END)
    entry_age.delete(0,END)

    selectedItem = trv.selection()[0]
    entry_id.insert(0, trv.item(selectedItem)['values'][0])
    entry_fname.insert(0, trv.item(selectedItem)['values'][1])
    entry_lname.insert(0, trv.item(selectedItem)['values'][2])
    entry_email.insert(0, trv.item(selectedItem)['values'][3])
    entry_age.insert(0, trv.item(selectedItem)['values'][4])


trv.bind("<<TreeviewSelect>>", displaySelectedItem)


frame.grid(row=0, column=0)

label_id.grid(row=0, column=0, sticky='e')
entry_id.grid(row=0, column=1)

trv.grid(row=0, column=2, rowspan=5, padx=10, pady=10)

label_fname.grid(row=1, column=0, sticky='e')
entry_fname.grid(row=1, column=1)

label_lname.grid(row=2, column=0, sticky='e')
entry_lname.grid(row=2, column=1)

label_email.grid(row=3, column=0, sticky='e')
entry_email.grid(row=3, column=1)

label_age.grid(row=4, column=0, sticky='e')
entry_age.grid(row=4, column=1)



root.mainloop()