# -*- coding: utf-8 -*-
from bge import logic

from .panel import *
from .component import *
from .gfx import *
from .font import *


class Compz:

	def __init__(self, style=None):
		self.gfx = GFXvbo()

		self.components = []
		self.active = None

		self.scene = None
		self.__gstyle = style

		self.current_id = 0

	@property
	def style(self):
		return self.__gstyle

	@style.setter
	def style(self, v):
		self.__gstyle = v
		for comp in self.components:
			comp.style = self.__gstyle

	def addComp(self, comp):
		comp.system = self
		comp.style = self.style
		comp.id = self.current_id
		self.components.append(comp)
		self.current_id += 1
		return comp

	def __draw__(self):
		self.gfx.set2D()
		comps = sorted(self.components,
			key=lambda x: isinstance(x, Panel), reverse=True)
		for comp in comps:
			if not comp.visible:
				continue
			if comp.parent is not None and not comp.parent.visible:
				continue
			comp.draw()

		for comp in comps:
			if not comp.visible:
				continue
			if comp.parent is not None and not comp.parent.visible:
				continue
			if not comp.finished:
				comp.endDraw()

		Font.first = True

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

