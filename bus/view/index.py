# coding:utf-8

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
	'''
	i = 0
	def get(self):
		position = ['119.2205783, 26.02993','119.219333,26.032609','119.21918,26.033299','119.218857,26.034062','119.218426,26.034549','119.218021,26.034898','119.217141,26.03575']
		re_pos = position[self.i]
		self.i += 1
		self.write(re_pos)
	'''
	def get(self):
		# print(self)
		position = get_position()
		self.finish({'position_x': position[0], 'position_y': position[1]})


def get_position():# 这个设计用得不习惯，我在这个文件中没办法创建全局变量，因为是从其他文件调用这里的class，变量好像会无效。用config试试
	print(config.i)
	position = [[119.2205783, 26.02993],[119.219333,26.032609],[119.21918,26.033299],[119.218857,26.034062],[119.218426,26.034549],[119.218021,26.034898],[119.217141,26.03575]]
	pos = position[config.i]
	config.i = (config.i+1) % 7
	return pos
	
	
	

