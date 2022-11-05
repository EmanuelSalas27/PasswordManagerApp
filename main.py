import tkinter
from tkinter import messagebox

PRIMARY_COLOR = '#004E89'
BUTTON_COLOR = '#2d231b'

window = None
window2 = None
web_entry = ''
email_entry = ''
pass_entry = ''


def add():
    global web_entry, email_entry, pass_entry
    web = web_entry.get()
    email = email_entry.get()
    word = pass_entry.get()
    if len(web) == 0 or len(email) == 0 or len(word) == 0:
        messagebox.showerror('Error','Please don\'t leave the fields empty')
    else:
        is_okay = messagebox.askokcancel('Password App', f'Website:{web}\nEmail:{email}\nPassword:{word}\nIs okay?', )
        if is_okay:
            data = open('data.txt', 'a')
            data.write(f'{web} | {email} | {word}\n')
            data.close()
            web_entry.delete(0, 'end')
            pass_entry.delete(0, 'end')


def passwords_window():
    global window, window2
    window.destroy()
    window2 = tkinter.Tk()
    window2.title('Password Manager App')
    window2.config(bg=PRIMARY_COLOR, pady='20', padx='10')
    window2.geometry('500x500')
    window2.grid_rowconfigure(0, weight=1)
    window2.grid_columnconfigure(0, weight=1)
    window2.resizable(False, False)

    title2 = tkinter.Label(text='Passwords Saved', bg=PRIMARY_COLOR, fg='White', font=('', '24'))
    title2.pack()

    try:
        file = open('data.txt', 'r')
    except FileNotFoundError:
        open('data.txt', 'w')
        file = open('data.txt', 'r')

    data = file.read()
    label5 = tkinter.Label(text=data, bg=PRIMARY_COLOR, fg='White', font=('', '10'), pady=10)
    label5.pack()

    file.close()

    pass_button = tkinter.Button(text='Return', border=0, background='White', fg='Black', width=10, command=main_window)
    pass_button.pack()


def main_window():
    global window, window2, web_entry, email_entry, pass_entry

    if window2:
        window2.destroy()

    window = tkinter.Tk()
    window.title('Password Manager App')
    window.config(bg=PRIMARY_COLOR, pady='20', padx='10')
    window.geometry('500x500')
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)
    window.resizable(False, False)

    title = tkinter.Label(text='Password Manager App', bg=PRIMARY_COLOR, fg='White', font=('', '24'))
    title.grid(column=0, row=0, columnspan=4)

    label1 = tkinter.Label(text='Website:', bg=PRIMARY_COLOR, fg='White', font=('', '10'), pady=10)
    label1.grid(column=0, row=1)

    label2 = tkinter.Label(text='Email/Username:', bg=PRIMARY_COLOR, fg='White', font=('', '10'), pady=10)
    label2.grid(column=0, row=2)

    label3 = tkinter.Label(text='Password:', bg=PRIMARY_COLOR, fg='White', font=('', '10'), pady=10)
    label3.grid(column=0, row=3)

    web_entry = tkinter.Entry(width=40, borderwidth=0, background=PRIMARY_COLOR, fg='White')
    web_entry.grid(column=1, row=1, columnspan=2)

    email_entry = tkinter.Entry(width=40, borderwidth=0, background=PRIMARY_COLOR, fg='White')
    email_entry.grid(column=1, row=2, columnspan=2)

    pass_entry = tkinter.Entry(width=40, borderwidth=0, background=PRIMARY_COLOR, fg='White')
    pass_entry.grid(column=1, row=3)

    add_button = tkinter.Button(text='Add', border=0, background='White', fg='Black', width=37, command=add)
    add_button.grid(column=1, row=4, columnspan=2)

    pass_button = tkinter.Button(text='Passwords', border=0, background='White', fg='Black', width=10, command=passwords_window)
    pass_button.grid(column=0, row=4)

    email_entry.insert(0, 'emanuelsalasdeleon@hotmail.com')

    window.mainloop()


main_window()