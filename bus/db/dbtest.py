import sqlite3
import time

# 这是为了循环插入数据

DB_PATH = 'bus.db'
SQL_SCHEMA = 'schema.sql'

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

position = ['119.2025935650,26.0355478269','119.2031085491,26.0377843661','119.2047125101,26.0362419298','119.2044335604,26.0349790451','119.2051148415,26.0336775847','119.2067402601,26.0322025788','119.2078024149,26.0306745303','119.2081618309,26.0289054399','119.2092937231,26.0271510457','119.2103022337,26.0253047735','119.2090630531,26.0240176672','119.2076575756,26.0255361611','119.2066758871,26.0258205752','119.2057532072,26.0280811406','119.2052865029,26.0297538354','119.2056727410,26.0307564767','119.2052114010,26.0329497246','119.2043370009,26.0348778209']



# position = ['119.21933100,26.03269500', '119.21933100,26.03269500', '119.21827100,26.03468300', '119.21827100,26.03468300', '119.21632200,26.03676100']
# 
# position = position[::-1]

while True:
    for i in position:
        c.execute('insert into gps(name, latlng, temperature, humidity) values("xb1","%s", 25, 50)' % i)
        conn.commit()
        time.sleep(5)
    
    print('xxx\n')
    # cursor = c.execute('select * from gps;')
    # 
    # for i in cursor:
    #     print(i)


c.close()