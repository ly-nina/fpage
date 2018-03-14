import sqlite3



def create_db(conn):
    with open(r'F:\website\fpage\bus\db\schema.sql', 'r') as f:
        a = f.read()
        c = conn.cursor()
        c.executescript(a)
        
        
conn = sqlite3.connect(r'F:\website\fpage\bus\db\bus.db')
c = conn.cursor()

create_db(conn)


c.execute('insert into gps(name, latlng) values("a","b")')
cursor = c.execute('select * from gps;')

for i in cursor:
    print(i)

