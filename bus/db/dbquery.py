import sqlite3
import time


conn = sqlite3.connect(r'F:\website\fpage\bus\db\bus.db')
c = conn.cursor()



cursor = c.execute("select * from gps a where exists(select * from (select name,max(time) as FTime from gps group by name) x where x.name=a.name and a.time=x.FTime);")

temp = {}
for i in cursor:
    print(i)
    pos = i[3].split(',')
    temp[i[1]] = {'position_x': float(pos[0]), 'position_y': float(pos[1]), 'temperature': i[4], 'humidity': i[5]}

conn.close()


