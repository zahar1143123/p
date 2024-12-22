import sqlite3 as sq

con = sq.connect('test.db')

cur = con.cursor()

res = cur.execute('SELECT * from user')

rl = res.fetchall()
print(rl)
# cur.execute('''INSERT INTO user VALUES
#             ('Andret','Balkso','Olefgodvich','qwerty'),
#             ('Alex','Pions','Leoan','qwerty')
#             ''')

# con.commit()

# cur.execute("CREATE TABLE user(name,surname,dad_name,password)")
# cur.fetchone()

with open(file='users.txt', mode='a') as file:
    for i in rl:
        file.write(f'\n{i}')
    file.close()