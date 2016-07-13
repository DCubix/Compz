# -*- coding: utf-8 -*-
import blf
from .gfx import *


class Font:

	def __init__(self, path=None):
		self.id = 0 if path is None else blf.load(path)
		self.size = 14.0
		self.shadowed = True
		self.shadow_offset = [0, -1]

	def measure(self, text):
		return blf.dimensions(self.id, text)

	def draw(self, text, x, y):
		if self.shadowed:
			blf.enable(self.id, blf.SHADOW)
			blf.shadow_offset(self.id, self.shadow_offset[0],
				self.shadow_offset[1])
			blf.shadow(self.id, 3, 0, 0, 0, 0.8)
		else:
			blf.disable(self.id, blf.SHADOW)

		blf.position(self.id, x, -y, 0)
		blf.size(self.id, int(self.size), 72)

		_, h = self.measure("E]")
		glPushMatrix()
		glTranslatef(0, h, 0)
		glScalef(1, -1, 1)
		blf.draw(self.id, text)
		glPopMatrix()