import sqlite3
import time



def create_db(conn):
    with open(r'F:\website\fpage\bus\db\schema.sql', 'r') as f:
        a = f.read()
        c = conn.cursor()
        c.executescript(a)
        
        
conn = sqlite3.connect(r'F:\website\fpage\bus\db\bus.db')
c = conn.cursor()

#create_db(conn)
#c.execute('insert into gps(name, latlng, temperature, humidity) values("xb1","119.20166670,26.37083330", 25, 50)')
#conn.commit()
cursor = c.execute('select * from gps;')

for i in cursor:
    print(i)

position = ['119.21933100,26.03269500', '119.21933100,26.03269500', '119.21827100,26.03468300', '119.21827100,26.03468300', '119.21632200,26.03676100']
for i in position:
    c.execute('insert into gps(name, latlng, temperature, humidity) values("xb1","%s", 25, 50)' %i)
    conn.commit()
    time.sleep(5)

print('xxx\n')
cursor = c.execute('select * from gps;')

for i in cursor:
    print(i)


c.close()