# coding:utf-8
import sqlite3

from view import route, url_for, View
import random
import config


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
        conn = sqlite3.connect(r'F:\website\fpage\bus\db\bus.db')
        c = conn.cursor()
        cursor = c.execute("select * from gps a where exists(select * from (select name,max(time) as FTime from gps group by name) x where x.name=a.name and a.time=x.FTime);")
        temp = {}
        for i in cursor:
            pos = i[3].split(',')
            temp[i[1]] = {'position_x': float(pos[0]), 'position_y': float(pos[1]), 'temperature': i[4], 'humidity': i[5]}

        self.finish(temp,
        )
        # self.finish({'a':1})


def get_position():  # 这个设计用得不习惯，我在这个文件中没办法创建全局变量，因为是从其他文件调用这里的class，变量好像会无效。用config试试
    # print(config.i)
    position = [[119.2205783, 26.02993], [119.219333, 26.032609], [119.21918, 26.033299], [119.218857, 26.034062], [119.218426, 26.034549], [119.218021, 26.034898], [119.217141, 26.03575]]
    # pos = position[config.i]
    # config.i = (config.i+1) % 7
    return position[int(random.random()*10) % 7]

    
@route('/label', name='label')
class Label(View):
    def get(self):
        self.finish(config.POSITION)

    def post(self):
        label = self.get_argument('message')
        # num = self.get_argument('')
        #
        label = label.split()[0]
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

