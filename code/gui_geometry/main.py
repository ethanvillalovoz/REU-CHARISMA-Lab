# Imports
from tkinter import * # General import when creating a GUI

from tkinter.ttk import * # Add a combobox widget

from tkinter import scrolledtext # Add a ScrolledText widget (Tkinter textarea)

from tkinter import messagebox # Used for message box

from tkinter.ttk import Progressbar # To create a progress bar, you can use the progressbar class like this:
from tkinter import ttk

from tkinter import filedialog #Add a filedialog (file & directory chooser)
from os import path

from tkinter import Menu # Add a Menu bar



def clicked(lbl, txt, window):
    res = "Welcome to " + txt.get()

    lbl.configure(text=res)

    # Function call which immediately puts the writing line where the text box is
    txt.focus()

    # To disable the entry widget, Now, you won’t be able to enter any text.
    # txt = Entry(window, width=10, state='disabled')

def main():

    #Establishes a new window for the GUI
    window = Tk()

    # Names the top page user is currently in
    window.title("Geometry Visualisation")
    # Creates a size of the window
    window.geometry('350x200')


    # CREATES A SCREEN LABEL ON SCREEN AND TEXT BOX

    # Adds a label to the screen
    lbl = Label(window, text="Hello", font=("Arial Bold", 50))
    lbl.grid(column = 0, row = 0)

    # Inserts a input text box
    txt = Entry(window, width=10)
    txt.grid(column=1, row=0)

    # Handles the button Click
    # clicked(lbl, txt, window)

    # Creates a button
    btn = Button(window, text="Click Me", command=clicked)
    btn.grid(column=2, row=0)


    # # Creating a Combo Widget
    # combo = Combobox(window)
    #
    # # Stores values/choices into a tuple
    # combo['values'] = ("Choose a shape", "Square", "Triangle", "Semi-Circle", "Clump", "Circle", "Line")
    # combo.current(0)  # set the selected item inside the tuple
    # combo.grid(column=0, row=0)


    # # Add a Checkbutton widget (Tkinter checkbox)
    # chk_state = BooleanVar()
    #
    # chk_state.set(True)  # set check state
    #
    # chk = Checkbutton(window, text='Choose', var=chk_state)
    #
    # chk.grid(column=0, row=0)
    #
    # # Also, you can use IntVar instead of BooleanVar and set the value to 0 or 1.
    # # chk_state = IntVar()
    # # chk_state.set(0)  # uncheck
    # # chk_state.set(1)  # check


    ## Radio Button Option
    # rad1 = Radiobutton(window, text='First', value=1)
    # rad2 = Radiobutton(window, text='Second', value=2)
    # rad3 = Radiobutton(window, text='Third', value=3)
    #
    # rad1.grid(column=0, row=0)
    # rad2.grid(column=1, row=0)
    # rad3.grid(column=2, row=0)

    # selected = IntVar()
    #
    # rad1 = Radiobutton(window, text='First', value=1, variable=selected)
    # rad2 = Radiobutton(window, text='Second', value=2, variable=selected)
    # rad3 = Radiobutton(window, text='Third', value=3, variable=selected)
    #
    # def clicked():
    #     print(selected.get())
    #
    # btn = Button(window, text="Click Me", command=clicked)
    #
    # rad1.grid(column=0, row=0)
    # rad2.grid(column=1, row=0)
    # rad3.grid(column=2, row=0)
    #txt
    # btn.grid(column=3, row=0)


    # ## Add a ScrolledText widget (Tkinter textarea)
    # txt = scrolledtext.ScrolledText(window, width=40, height=10)
    #
    # txt.grid(column=0, row=0)
    # txt.insert(INSERT, "Bruh this is where you write stuff")
    #
    # txt.delete(1.0, END)


    # # Create a MessageBox
    # def clicked():
    #     messagebox.showinfo('Message title', 'Message content')
    #
    # btn = Button(window, text='Click here', command=clicked)
    # # messagebox.showwarning('Message title', 'Message content')  # shows warning message
    # # messagebox.showerror('Message title', 'Message content')  # shows error message

    # Before showing the GUI window, prints out a seperate message window with a prompt and cancel/yes response
    # res = messagebox.askquestion('Message title', 'Hello')
    #
    # res = messagebox.askyesno('Message title', 'Message content')
    #
    # res = messagebox.askyesnocancel('Message title', 'Message content')
    #
    # res = messagebox.askokcancel('Message title', 'Message content')
    #
    # res = messagebox.askretrycancel('Message title', 'Message content')
    #
    # btn.grid(column=0, row=0)


    # ## Add a SpinBox (numbers widget)
    # spin = Spinbox(window, from_=0, to=100, width=5)
    # spin.grid(column=0, row=0)
    #
    # #You can specify the numbers for the Spinbox instead of using the whole range like this:
    # spin = Spinbox(window, values=(3, 8, 11), width=5)
    # # Here the Spinbox widget only shows these 3 numbers only 3, 8, and 11.
    #
    # #Set default value for Spinbox
    # #To set the Spinbox default value, you can pass the value to the textvariable parameter like this:
    #
    # var = IntVar()
    # var.set(36)
    # spin = Spinbox(window, from_=0, to=100, width=5, textvariable=var)
    # # Now, if you run the program, it will show 36 as a default value for the Spinbox.


    # # Add a Progressbar widget
    # style = ttk.Style()
    #
    # style.theme_use('default')
    #
    # style.configure("black.Horizontal.TProgressbar", background='black')
    #
    # bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')
    #
    # bar['value'] = 30
    #
    # bar.grid(column=0, row=0)


    # # Add a filedialog (file & directory chooser)
    # file = filedialog.askopenfilename()
    # files = filedialog.askopenfilenames()
    # file = filedialog.askopenfilename(filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
    # dir = filedialog.askdirectory()
    # file = filedialog.askopenfilename(initialdir=path.dirname(__file__))


    # # Add a Menu bar ## MAC OS IT IS FOR THE TOP PART WHERE YOU FINE FILE/INSERT/EDIT/ETC...
    # menu = Menu(window)
    #
    # new_item = Menu(menu)
    #
    # new_item.add_command(label='New')
    #
    # new_item.add_separator() # JUST ADDS A NEW CATEGORY UNDER FILE
    #
    # new_item.add_command(label='Edit')
    #
    # menu.add_cascade(label='File', menu=new_item)
    #
    # window.config(menu=menu)
    # #You can disable this feature by disabling the tearoff feature like this:
    # new_item = Menu(menu, tearoff=0)
    # # Just replace the new_item in the above example with this one and it won’t show the dashed line anymore.
    #
    # #I don’t need to remind you that you can type any code that works when the user clicks on any menu item by specifying the command property.
    # new_item.add_command(label='New', command=clicked)


    #Add a Notebook widget (tab control)
    # tab_control = ttk.Notebook(window)
    #
    # tab1 = ttk.Frame(tab_control)
    #
    # tab2 = ttk.Frame(tab_control)
    #
    # tab_control.add(tab1, text='First')
    #
    # tab_control.add(tab2, text='Second')
    #
    # lbl1 = Label(tab1, text='label1')
    #
    # lbl1.grid(column=0, row=0)
    #
    # lbl2 = Label(tab2, text='label2')
    #
    # lbl2.grid(column=0, row=0)
    #
    # tab_control.pack(expand=1, fill='both')

    # function calls the endless loop of the window, so the window will wait for any user interaction till we close it.
    window.mainloop()
    # ^^^^^ Must have this at the very end ALWAYS

if __name__ == "__main__":
    main()