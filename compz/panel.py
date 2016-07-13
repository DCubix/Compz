# -*- coding: utf-8 -*-
from .component import *


PN_ITEM_ORI_VERTICAL = 0
PN_ITEM_ORI_HORIZONTAL = 1


class Panel(Component):

	def __init__(self, style=None):
		super(Panel, self).__init__(style=style)
		self.children = []
		self.padding = 4
		self.spacing = 4
		self.itemOrientation = PN_ITEM_ORI_VERTICAL

	def addComp(self, comp):
		comp.parent = self
		self.children.append(comp)
		if comp not in self.system.components:
			self.system.addComp(comp)

	def update(self):
		Component.update(self)
		self.zorder = 100

		h = 0
		for comp in self.children:
			if self.itemOrientation == PN_ITEM_ORI_VERTICAL:
				comp.width = self.width - (self.padding * 2)
				comp.position = [self.padding, self.padding + h]
				h += comp.height + self.spacing
			else:
				comp.height = self.height - (self.padding * 2)
				comp.position = [self.padding + h, self.padding]
				h += comp.width + self.spacing