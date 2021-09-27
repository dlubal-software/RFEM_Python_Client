from RFEM.initModel import *
from tkinter import *
from tkinter import ttk, Entry

def window(mainFunc):
    color = '#F2F3F4'
    # Creating tkinter window
    win = Tk()
    win.resizable(False, False)
    win.title('Power of automation with RFEM6')
    win.geometry("520x160")
    win.configure(bg=color)
    win.grid_columnconfigure(index=0, minsize=140)
    win.grid_columnconfigure(index=1, minsize=80)
    win.grid_columnconfigure(index=2, minsize=80)
    win.grid_columnconfigure(index=3, minsize=70)
    win.grid_columnconfigure(index=4, minsize=139)

    # Separators
    y = 3
    rh = 0.76
    ttk.Separator(win, orient=VERTICAL).place(x=140, y=y, relheight=rh)
    ttk.Separator(win, orient=VERTICAL).place(x=220, y=y, relheight=rh)
    ttk.Separator(win, orient=VERTICAL).place(x=295, y=y, relheight=rh)
    ttk.Separator(win, orient=VERTICAL).place(x=400, y=y, relheight=rh)

    Label(text="Params Type", justify=CENTER, font="Segoe 9 bold", bg=color).grid(row=0, column=0)
    Label(text="Data Type", justify=CENTER, font="Segoe 9 bold", bg=color).grid(row=0, column=1)
    Label(text="Symbol", justify=CENTER, font="Segoe 9 bold", bg=color).grid(row=0, column=2)
    Label(text="Units", justify=CENTER, font="Segoe 9 bold", bg=color).grid(row=0, column=3)
    Label(text="Magnitude", justify=CENTER, font="Segoe 9 bold", bg=color).grid(row=0, column=4)

    Label(text="hall width", bg=color).grid(row=1, column=0)
    Label(text="hall height", bg=color).grid(row=2, column=0)
    Label(text="hall height", bg=color).grid(row=3, column=0)
    Label(text="frame spacing", bg=color).grid(row=4, column=0)
    Label(text="number of frames", bg=color).grid(row=5, column=0)

    Label(text="float", bg=color).grid(row=1, column=1)
    Label(text="float", bg=color).grid(row=2, column=1)
    Label(text="float", bg=color).grid(row=3, column=1)
    Label(text="float", bg=color).grid(row=4, column=1)
    Label(text="integer", bg=color).grid(row=5, column=1)

    Label(text="L", bg=color).grid(row=1, column=2)
    Label(text="h_o", bg=color).grid(row=2, column=2)
    Label(text="h_m", bg=color).grid(row=3, column=2)
    Label(text="f_s", bg=color).grid(row=4, column=2)
    Label(text="n", bg=color).grid(row=5, column=2)

    Label(text="meters", bg=color).grid(row=1, column=3)
    Label(text="meters", bg=color).grid(row=2, column=3)
    Label(text="meters", bg=color).grid(row=3, column=3)
    Label(text="meters", bg=color).grid(row=4, column=3)
    Label(text="-", bg=color).grid(row=5, column=3)

    def validateAll(val): # 1 mandatory argument, not used
        try:
            float(e1.get())
            float(e2.get())
            float(e3.get())
            float(e4.get())
            int(e5.get())
            button1['state']="normal"
            return 1
        except:
            button1['state']="disabled"
            print("disabled")
            return 0

    # Setting entry points
    e1 = Entry(relief=FLAT, justify=CENTER, bg=color)
    e1.grid(row=1, column=4)
    e1.insert(INSERT, 20.0)
    e2 = Entry(relief=FLAT, justify=CENTER, bg=color)
    e2.grid(row=2, column=4)
    e2.insert(INSERT, 5.2)
    e3 = Entry(relief=FLAT, justify=CENTER, bg=color)
    e3.grid(row=3, column=4)
    e3.insert(INSERT, 7.3)
    e4 = Entry(relief=FLAT, justify=CENTER, bg=color)
    e4.grid(row=4, column=4)
    e4.insert(INSERT, 6.0)
    e5 = Entry(relief=FLAT, justify=CENTER, bg=color)
    e5.grid(row=5, column=4)
    e5.insert(INSERT, 6)

    def start(val):
        mainFunc(float(e1.get()),float(e2.get()),float(e3.get()),int(e5.get()),float(e4.get()))
    def close_window(val):
        win.destroy()

    # substitute for validatecommand and validation options of Entry (e1-e5)
    e1.bind('<FocusOut>', validateAll)
    e1.bind('<Key>', validateAll)
    e2.bind('<FocusOut>', validateAll)
    e2.bind('<Key>', validateAll)
    e3.bind('<FocusOut>', validateAll)
    e3.bind('<Key>', validateAll)
    e4.bind('<FocusOut>', validateAll)
    e4.bind('<Key>', validateAll)
    e5.bind('<FocusOut>', validateAll)
    e5.bind('<Key>', validateAll)

    button1=Button(text='Run', anchor=CENTER, width=12, height=1, bg=color, state="normal") # width=16
    button1.grid(row=6, column=4)
    button1.bind('<ButtonRelease-1>', start)

    button2=Button(text='Close', anchor=CENTER, width=12, height=1, bg=color, state="normal")
    button2.grid(row=6, column=3)
    button2.bind('<ButtonRelease-1>', close_window)

    win.mainloop()
