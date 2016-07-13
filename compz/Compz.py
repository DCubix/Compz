# -*- coding: utf-8 -*-
from bge import logic

from .panel import *
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

		self.panelCount = 0

	def setStyle(self, style):
		for comp in self.components:
			comp.style = style

	def addComp(self, comp):
		if isinstance(comp, Panel):
			self.panelCount += 1
			comp.index = self.panelCount
		comp.system = self
		self.components.append(comp)
		return comp

	def __draw__(self):
		self.gfx.set2D()
		comps = sorted(self.components, key=lambda x: x.zorder)
		for comp in comps:
			if not comp.visible:
				continue
			if comp.parent is not None:
				if not comp.parent.visible:
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
			if comp.parent is not None:
				if not comp.parent.visible or not comp.parent.enabled:
					continue
			if comp.update():
				break
		self.event()