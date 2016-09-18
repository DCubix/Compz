# -*- coding: utf-8 -*-


class LayoutBase:

	def __init__(self):
		self.spacing = 4
		self.padding = 4

	def get_width(self, comps):
		w = 0
		for comp in comps:
			w += comp.width + self.spacing
		return w + (self.padding * 2)

	def get_height(self, comps):
		h = 0
		for comp in comps:
			h += comp.height + self.spacing
		return h + (self.padding * 2)

	def apply(self, comp):
		pass

	def reset(self):
		pass