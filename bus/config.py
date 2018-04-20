# coding:utf-8

HOST = '0.0.0.0'
PORT = 9000
DEBUG = True
TITLE = 'bus'
VERSION = '1.2.0'
TEMPLATE = 'tornado'  # jinja2/mako/tornado
DATABASE_URI = "sqlite:///database.db"
COOKIE_SECRET = "6aOO5ZC55LiN5pWj6ZW/5oGo77yM6Iqx5p+T5LiN6YCP5Lmh5oSB44CC"
i = 0
DB_PATH = "./db/bus.db"
# DB_PATH = r'F:\website\fpage\bus\db\bus.db'
# DB_PATH = r'E:\Study\Ending\website\fpage\bus\db\bus.db'

POSITION = {'学生街左': [0, [119.21449,26.040397]], '学生街右': [1, [119.2155,26.039756]], '图书馆左': [2, [119.217868,26.033316]], '图书馆右': [3, [119.219233,26.033316]], '南区食堂左': [4, [119.218029,26.027833]], '南区食堂右': [5, [119.218213,26.028004]], }  # 这是用来放置显示等车人数的label数据

ID = ['123456789ABCDEF'] # TCP Server
NAME = ['XB01'] # TCP Server

try:
    from private import *
except:
    pass
