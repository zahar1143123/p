import tkinter as tk
import sqlite3 as sq

con = sq.connect('votes.db')

cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS vote(title, options)")

def Send():
    title = Main_Input.get()
    arr = Options_Input.get().split()


root = tk.Tk()

Frame = tk.Frame(root)

Main = tk.Label(Frame, text='Напишите текст опроса').grid(row=0, column=0)
Main_Input = tk.Entry(Frame)
Main_Input.grid(row=0, column=1)

Main = tk.Label(Frame, text='Напишите варианты опроса').grid(row=1,column=0)
Options_Input = tk.Entry(Frame)
Options_Input.grid(row=1, column=1)
Mainl = tk.Label(Frame, text='Пример поля вариантов опроса (необходимо ставить пробел после варианта): Пример1 Пример2 Пример3').grid(row=2,column=0,columnspan=2)

Btn = tk.Button(Frame, text='Отправить', command=Send).grid(row=3,column=0,columnspan=2)




Frame.pack()
root.title('Меню админа')
root.state('zoomed')
root.mainloop()

