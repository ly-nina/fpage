import sqlite3
import time

# 这是为了循环插入数据

DB_PATH = r'F:\website\fpage\bus\db\bus.db'
SQL_SCHEMA = r'F:\website\fpage\bus\db\schema.sql'

def create_db(conn):
    with open(SQL_SCHEMA, 'r') as f:
        a = f.read()
        c = conn.cursor()
        c.executescript(a)
        
        
conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

#create_db(conn)
#c.execute('insert into gps(name, latlng, temperature, humidity) values("xb1","119.20166670,26.37083330", 25, 50)')
#conn.commit()
cursor = c.execute('select * from gps;')

for i in cursor:
    print(i)

position = ['119.213901,26.038254','119.213901,26.039569','119.21471,26.040316','119.21603,26.03853','119.216363,26.036777','119.218402,26.034586','119.219318,26.032833','119.219974,26.030593','119.22151,26.028483','119.222049,26.026989','119.220189,26.02647','119.218091,26.027911','119.217759,26.029213','119.217184,26.030561','119.217022,26.030999','119.217148,26.032817','119.216771,26.034156','119.216394,26.035463','119.21687,26.036055','119.215675,26.037443']



# position = ['119.21933100,26.03269500', '119.21933100,26.03269500', '119.21827100,26.03468300', '119.21827100,26.03468300', '119.21632200,26.03676100']
# 
# position = position[::-1]


for i in position:
    c.execute('insert into gps(name, latlng, temperature, humidity) values("xb1","%s", 25, 50)' % i)
    conn.commit()
    time.sleep(5)

print('xxx\n')
cursor = c.execute('select * from gps;')

for i in cursor:
    print(i)


c.close()