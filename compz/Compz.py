# -*- coding: utf-8 -*-
from bge import logic

from .component import *
from .gfx import *


CZ_DRAW_MODE_VBO = 0
CZ_DRAW_MODE_DL = 1


class Compz:

	def __init__(self, drawMode=CZ_DRAW_MODE_VBO):
		if drawMode == CZ_DRAW_MODE_DL:
			self.gfx = GFXdl()
		else:
			self.gfx = GFXvbo()

		self.components = []
		self.active = None

		self.scene = logic.getCurrentScene()
		self.scene.post_draw.append(self.__draw__)

	def setStyle(self, style):
		for comp in self.components:
			comp.style = style

	def addComp(self, comp):
		comp.system = self
		self.components.append(comp)

	def __draw__(self):
		self.gfx.set2D()
		comps = sorted(self.components, key=lambda x: x.zorder, reverse=True)
		for comp in comps:
			if not comp.visible:
				continue
			comp.draw()
			comp.endDraw()

	def event(self):
		comps = sorted(self.components, key=lambda x: x.zorder, reverse=True)
		for comp in comps:
			comp.event()

	def update(self):
		comps = sorted(self.components, key=lambda x: x.zorder, reverse=True)
		for comp in comps:
			comp.update()
		self.event()