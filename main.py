import tkinter as tk
import sqlite3 as sq
import os
from tkinter import messagebox

con = sq.connect('userstest.db')


cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS user(name,surname,dad_name,password)")

root = tk.Tk()

def click():
    root.withdraw()
    os.system('python user.py')
    root.deiconify()

def check():
    code = Admin_Input.get()

    if code == 'Q9bR6LQZhKp0':
        root.withdraw()
        os.system('python adm.py')
        root.deiconify()
    else:
        messagebox.showwarning('Ошибка','Введен неправильный код')
        

def send_inf():
    take_name = Name_Input.get()
    take_sur = Surname_Input.get()
    take_dad = Dad_Input.get()
    take_pass = Password_Input.get()

    cur.execute(f"""INSERT INTO user VALUES
                ('{take_name}','{take_sur}','{take_dad}','{take_pass}')""")
    
    con.commit()
    

    cur.execute('SELECT MAX(rowid), * FROM user')
    data = cur.fetchone()

    with open(file='users.txt', mode='a') as file:
        file.write(f'\n{data}')
        file.close()

    click()


def check_inf():
    take_name = Name_Input.get()
    take_sur = Surname_Input.get()
    take_dad = Dad_Input.get()
    take_pass = Password_Input.get()

    cur.execute('SELECT * from user')
    rl = cur.fetchall()

    # names = []
    # surnames = []
    # dads = []
    # passwords = []
    users = [

    ]
    for i in rl:
        use = {'name': i[0], 'surname': i[1], 'dad': i[2], 'password': i[3]}
        users.append(use)

    for user in users:
        if (user['name']==take_name and user['surname']==take_sur and user['dad']==take_dad and user['password']==take_pass):
            click()
            break
    else:
        messagebox.showwarning('Произошла ошибка','Неверный пароль либо же такого пользователя не существует')
            

Frame = tk.Frame(root)

Admin_Text = tk.Label(Frame, text='Введиие код, чтобы войти как админ', pady=5).grid(row=7, column=0)
Admin_Input = tk.Entry(Frame)
Admin_Input.grid(row=7, column=1, padx=10)
Btn_Admin = tk.Button(Frame, text='Отправить код', command=check).grid(row=7, column=2)

Registration_Text = tk.Label(Frame, text='Регистрация', pady=10).grid(row=0, column=0, columnspan=2)

Name_Text = tk.Label(Frame, text='Введите свое имя', pady=5).grid(row=1, column=0)
Name_Input = tk.Entry(Frame)
Name_Input.focus()
Name_Input.grid(row=1, column=1)

Name_Text = tk.Label(Frame, text='Введите свою фамилию', pady=5).grid(row=2, column=0)
Surname_Input = tk.Entry(Frame)
Surname_Input.grid(row=2, column=1)

Name_Text = tk.Label(Frame, text='Введите своё отчество', pady=5).grid(row=3, column=0)
Dad_Input = tk.Entry(Frame)
Dad_Input.grid(row=3, column=1)

Name_Text = tk.Label(Frame, text='Введите свой пароль', pady=5).grid(row=4, column=0)
Password_Input = tk.Entry(Frame, show='*')
Password_Input.grid(row=4, column=1)

Reg_Btn = tk.Button(Frame, text='Зарегистрироваться', command=send_inf).grid(row=5, column=0, columnspan=2)

Is_Text = tk.Label(Frame, text='Уже есть аккаунт ?', pady=20).grid(row=6, column=0)
Is_Btn = tk.Button(Frame, text='Войти', command=check_inf).grid(row=6, column=1, sticky='ew')

Frame.pack()

# Image = tk.PhotoImage(file='../images/')    

# root.config(background='')

root.title('Регистрация')
root.state('zoomed')

root.mainloop()



