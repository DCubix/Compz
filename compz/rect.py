# -*- coding: utf-8 -*-
"""
@author: TwisterGE
"""


class Rect:

	def __init__(self, x=0, y=0, width=1, height=1):
		self.data = [x, y, width, height]

	def hasPoint(self, x, y):
		return x > self.x and \
				x < self.x + self.width and \
				y > self.y and \
				y < self.y + self.height

	@property
	def x(self):
		return self.data[0]

	@x.setter
	def x(self, v):
		self.data[0] = v

	@property
	def y(self):
		return self.data[1]

	@y.setter
	def y(self, v):
		self.data[1] = v

	@property
	def width(self):
		return self.data[2]
	
	@width.setter
	def width(self, v):
		self.data[2] = v

	@property
	def height(self):
		return self.data[3]

	@height.setter
	def height(self, v):
		self.data[3] = v