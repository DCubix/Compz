# -*- coding: utf-8 -*-
"""
@author: TwisterGE
"""
import math


class Point:

	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def distance(self, p):
		dx = p.x - self.x
		dy = p.y - self.y
		return math.sqrt(dx * dx + dy * dy)