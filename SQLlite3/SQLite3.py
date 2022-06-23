import sqlite3

db = sqlite3.connect('test_db.sqlite')
cursor = db.cursor()

# cursor.execute('''
#                 CREATE TABLE IF NOT EXISTS users (
#                 id INTEGER PRIMARY KEY,
#                 name TEXT NOT NULL,
#                 email TEXT NOT NULL UNIQUE )''')

# cursor.execute('insert into users (name, email) values ("giorgi javakhidze", "giorgijavaxidze@gmail.com")')
# cursor.execute('insert into users (name, email) values ("liza javakhidze", "lizajavaxidze@gmail.com")')
# cursor.execute('insert into users (name, email) values ("salome sabanadze", "salomesabanadze@gmail.com")')
# cursor.execute('insert into users (name, email) values ("maxime ", "max@gmail.com")')
# cursor.executescript('''insert into users (name, email) values ("kino ", "kino@gmail.com");
#                         insert into users (name, email) values ("dato ", "dato@gmail.com");
#
#                         ''')

# users = [
#     ('user1', 'user1@gmail.com'),
#     ('user2', 'user2@gmail.com'),
#     ('user3', 'user3@gmail.com'),
#
# ]

# cursor.executemany("insert into users (name, email) values (?, ?)", users)

# db.commit()

email = 'max@gmail.com'
cursor.execute("select * from users")
res = cursor.fetchall()

for user in res:
    print(user[1] + "\t" + user[2])

db.close( )