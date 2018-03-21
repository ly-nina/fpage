import sqlite3
import time
import datetime

def get_time():
    time_now = datetime.datetime.now()
    return [(time_now+datetime.timedelta(hours=-i)).strftime("%Y-%m-%d %H:%M:%S") for i in range(6)][::-1]
    

def get_data(time_list):
    temp = {}
    for i in range(5):
        cursor = c.execute("select location, count(location) as num from wait where time(time) between time('%s') and time('%s') group by location;" % (time_list[i], time_list[i+1]))
        ext = {}
        for j in cursor:
            ext[j[0]] = j[1]
            # print(j)
            time.sleep(0.1)
        temp[time_list[i]] = ext
        # print(time_list[i])
        # print('\n')
    return temp
    
def excel_data(temp):
    POSITION = {'学生街左': [0, [119.21449,26.040397]], '学生街右': [1, [119.2155,26.039756]], '图书馆左': [2, [119.219125,26.033235]], '图书馆右': [3, [119.219233,26.033316]], '南区食堂左': [4, [119.218029,26.027833]], '南区食堂右': [5, [119.218213,26.028004]], }
        
    x = {}
    for i in POSITION:
        a=[]
        for j in temp:
            if i in temp[j]:
                a.append(temp[j][i])
            else:
                a.append(0)
        x[i] = a
    return x
    
    
    """ 这一段是测试gps表  """
# conn = sqlite3.connect(r'F:\website\fpage\bus\db\bus.db')
# c = conn.cursor()
# 
# 
# 
# cursor = c.execute("select * from gps a where exists(select * from (select name,max(time) as FTime from gps group by name) x where x.name=a.name and a.time=x.FTime);")
# 
# temp = {}
# for i in cursor:
#     print(i)
#     pos = i[3].split(',')
#     temp[i[1]] = {'position_x': float(pos[0]), 'position_y': float(pos[1]), 'temperature': i[4], 'humidity': i[5]}
# 
# conn.close()
# 


""" 这一段是测试获取图表数据 """
conn = sqlite3.connect(r'F:\website\fpage\bus\db\bus.db')
c = conn.cursor()

# cursor = c.execute("select location, count(location) as num from wait where time between '2018-03-21 01:23:48' and '2018-03-21 03:23:48' group by location;")

end_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") # 当前时间（小时）
begin_time = (datetime.datetime.now()+datetime.timedelta(hours=-5)).strftime("%Y-%m-%d %H:%M:%S") # 过去5个小时

# cursor = c.execute("select location, count(location) as num from wait where time(time) between time('%s') and time('%s') group by location;" % (begin_time, end_time))



# temp = {}
# for i in cursor:
#     print(i)
#     time.sleep(0.1)
    
time_list = get_time()
temp = get_data(time_list)
final = excel_data(temp)


conn.close()


