from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from dbConnectReservation import connectdata

db = connectdata()
root = Tk()

l1 = ttk.Label(root, text="full name : ").grid(row=0, column=0)
e1 = ttk.Entry(root)
e1.grid(row=0, column=1, columnspan=2)

l2 = ttk.Label(root, text="Gender").grid(row=1, column=0)
rbvar = StringVar()
r1 = ttk.Radiobutton(root, text="male", variable=rbvar, value="is male").grid(row=1, column=1)
r2 = ttk.Radiobutton(root, text="female", variable=rbvar, value="is female").grid(row=1, column=2)


l3 = ttk.Label(root, text="Comments ").grid(row=2, column=0)
t1 = Text(root, width=20, height=10)
t1.grid(row=2, column=1)

b1 = ttk.Button(root, text="list").grid(row=3, column=1)
b2 = ttk.Button(root, text="Submit")
b2.grid(row=3, column=2)


def clickButton():
    print("full name :{}".format(e1.get()))
    print("Gender :{}".format(rbvar.get()))
    print("comments :{}".format(t1.get(1.0, 'end')))
    msg = db.addasd(e1.get(), rbvar.get(), t1.get(1.0, 'end'))
    messagebox._show(title="add info", message=msg)
    t1.delete(0.0, 'end')
    e1.delete(0, "end")




b2.config(command=clickButton)
root.mainloop()