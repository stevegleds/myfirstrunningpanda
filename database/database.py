import sqlite3

conn = sqlite3.connect('example.db')

c = conn.cursor()
# Create table first and then don't run again
# c.execute('''
#           CREATE TABLE runner
#           (id INTEGER PRIMARY KEY ASC AUTOINCREMENT , name VARCHAR(250) NOT NULL, created DATETIME NOT NULL, pbPace FLOAT, pbTime DATETIME)
#           ''')
# c.execute('''
#           CREATE TABLE address
#           (id INTEGER PRIMARY KEY ASC, street_name VARCHAR(250), street_number VARCHAR(250),
#            post_code VARCHAR(250) NOT NULL, person_id INTEGER NOT NULL,
#            FOREIGN KEY(person_id) REFERENCES person(id))
#           ''')

c.execute('''
          INSERT INTO runner VALUES('Steve', 15/02/2015, 9.50, '9:30')
          ''')
# c.execute('''
#           INSERT INTO address VALUES(1, 'python road', '1', '00000', 1)
#           ''')

conn.commit()
conn.close()

# conn = sqlite3.connect('example.db')
#
# c = conn.cursor()
# c.execute('SELECT * FROM person')
# print(c.fetchall())
# c.execute('SELECT * FROM address')
# print(c.fetchall())
# conn.close()
'''
        self.name = name.title()  # makes sure we use capital first letters
        self.created = created
        self.prevPace = None
        self.prevTime = None
        self.prevDate = None
        self.pbPace = None
        self.pbTime = None
        self.pbDate = None
        '''