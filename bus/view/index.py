# coding:utf-8
import sqlite3

from view import route, url_for, View
import random
import config
import datetime
import requests
import json

@route('/', name='index')
class Index(View):
    def get(self):
        self.render()


@route('/jump_test', name='jump')
class Jump(View):
    def get(self):
        self.messages.error('Message Test: Error!!')
        self.messages.error('中文测试')
        self.redirect(url_for('about'))


@route('/about', name='about')
class About(View):
    def get(self):
        self.render()


@route('/position', name='position')
class Position(View):
    def get(self):
        self.render('position.html')


@route('/pos', name='pos')
class Position(View):
    """
    i = 0
    def get(self):
        position = ['119.2205783, 26.02993','119.219333,26.032609','119.21918,26.033299','119.218857,26.034062','119.218426,26.034549','119.218021,26.034898','119.217141,26.03575']
        re_pos = position[self.i]
        self.i += 1
        self.write(re_pos)
    """
    def get(self):
        # print(self)
        position = get_position()
        position1 = get_position()
        conn = sqlite3.connect(config.DB_PATH)
        c = conn.cursor()
        cursor = c.execute("select * from gps a where exists(select * from (select name,max(time) as FTime from gps group by name) x where x.name=a.name and a.time=x.FTime);")
        temp = {}
        for i in cursor:
            pos = i[3].split(',')
            # print('x:',float(pos[0]), 'y:', float(pos[1]))
            x = get_street_baidu(float(pos[1]),float(pos[0]))
            lat = x['lat']
            lng = x['lng']
            temp[i[1]] = {'position_x': lng, 'position_y': lat, 'temperature': i[4], 'humidity': i[5]}
        c.close()
        self.finish(temp,
        )
        # self.finish({'a':1})


def get_position():  # 这个设计用得不习惯，我在这个文件中没办法创建全局变量，因为是从其他文件调用这里的class，变量好像会无效。用config试试
    # print(config.i)
    position = [[119.2205783, 26.02993], [119.219333, 26.032609], [119.21918, 26.033299], [119.218857, 26.034062], [119.218426, 26.034549], [119.218021, 26.034898], [119.217141, 26.03575]]
    # pos = position[config.i]
    # config.i = (config.i+1) % 7
    return position[int(random.random()*10) % 7]

    
def get_street_baidu(lat_gps, lng_gps):
    # 输入gps坐标，逆地址解析返回百度地图地址信息
    try:
        url = 'http://api.map.baidu.com/geocoder/v2/?&' \
              'location=' + str(lat_gps) + ',' + str(lng_gps) + \
              '&output=json&ak=1xW52e31qGyTjB19cLC8kZH8MRHU3S6E&extensions_road=ture&coordtype=wgs84ll'
        response = requests.get(url)
        string = response.content
        json_data = json.loads(string, encoding='utf8')
        if 'result' in json_data.keys():
            result = json_data['result']
            street = result['location']
        else:
            street = None
    except Exception as e:
        print(e)
    return street

    
@route('/label', name='label')
class Label(View):
    def get(self):
        self.finish(config.POSITION)

    def post(self):
        label = self.get_argument('message')
        # num = self.get_argument('')
        #
        label = label.split()[0]
        conn = sqlite3.connect(config.DB_PATH)
        c = conn.cursor()
        cursor = c.execute('insert into wait(location) values("%s")' % label)
        conn.commit()
        c.close()
        config.POSITION[label][0] += 1
        print(config.POSITION[label][0])
        self.finish({'status': 'success'})


@route('/console', name='console')
class Console(View):
    def get(self):
        self.render('console.html', pos=config.POSITION)

    def post(self):
        message = self.get_argument('message')
        print(message)
        if message in config.POSITION:

            config.POSITION[message][0] = 0
            self.finish({'status': '清零成功'})
            # self.render('console.html', pos = config.POSITION)
        else:
            self.finish({'status': 'failed'})
            
            
@route('/chart', name='chart')
class Chart(View):
    def get(self):
        time_list, final =echarts()
        print(time_list, final)
        self.render(time_list=time_list, data=final)


def echarts():
    conn = sqlite3.connect(config.DB_PATH)
    c = conn.cursor()
    time_list = get_time()
    temp = get_data(time_list, c)
    final = excel_data(temp)
    conn.close()
    return time_list, final


def get_time():
    time_now = datetime.datetime.now()
    return [(time_now+datetime.timedelta(hours=-i)).strftime("%Y-%m-%d %H:%M:%S") for i in range(6)][::-1]
    

def get_data(time_list, c):
    temp = {}
    for i in range(5):
        cursor = c.execute("select location, count(location) as num from wait where time(time) between time('%s') and time('%s') group by location;" % (time_list[i], time_list[i+1]))
        ext = {}
        for j in cursor:
            ext[j[0]] = j[1]
            # print(j)
            # time.sleep(0.1)
        temp[time_list[i]] = ext
        # print(time_list[i])
        # print('\n')
    return temp
    
def excel_data(temp):
        
    name = {}
    for i in config.POSITION:
        a=[]
        for j in temp:
            if i in temp[j]:
                a.append(temp[j][i])
            else:
                a.append(0)
        name[i] = a
    return name

    
@route('/pos', name='pos')
class Pos(View):
    def get(self):
        self.render()
    
    def post():
        data = self.get_argument('pos')
        print(data)
        self.finish("{'state': 'success'}")
