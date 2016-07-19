# -*- coding: utf-8 -*-
from bge import logic

from .panel import *
from .component import *
from .gfx import *


class Compz:

	def __init__(self):
		self.gfx = GFXvbo()

		self.components = []
		self.active = None

		self.scene = None

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
		comps = sorted(self.components,
			key=lambda x: isinstance(x, Panel), reverse=True)
		for comp in comps:
			if not comp.visible:
				continue
			if comp.parent is not None:
				if not comp.parent.visible:
					continue
			comp.draw()
			comp.endDraw()

	def event(self):
		comps = sorted(self.components, key=lambda x: isinstance(x, Panel))
		for comp in comps:
			comp.event()

	def update(self):
		if self.scene is None:
			self.scene = logic.getCurrentScene()
			self.scene.post_draw.append(self.__draw__)

		comps = sorted(self.components,
			key=lambda x: isinstance(x, Panel), reverse=True)
		for comp in comps:
			if comp.parent is not None:
				if not comp.parent.visible or not comp.parent.enabled:
					continue
			comp.update()
		self.event()