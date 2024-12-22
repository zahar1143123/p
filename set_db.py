import sqlite3 as sq

con = sq.connect('userstest.db')

cur = con.cursor()

cur.execute('DROP TABLE IF EXISTS user')


# cur.execute('SELECT rowid, * from user')

# data = cur.fetchall()

# with open(file='users.txt', mode='a') as file:
#     for i in data:
#         file.write(f'\n{i}')
#     file.close()
