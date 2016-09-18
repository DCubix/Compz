# -*- coding: utf-8 -*-
from .panel import *
from .radio import *
from .linear_layout import *


class RadioGroup(Panel):

	def __init__(self, radioStyle=None):
		super(RadioGroup, self).__init__()
		self.selectedIndex = -1
		self.radioStyle = radioStyle
		self.previous = None

	def addComp(self, comp):
		pass

	def addOption(self, opt):
		if not isinstance(opt, str):
			return None

		comp = Radio(text=opt, style=self.radioStyle)
		comp.group = self
		comp.text = opt
		return Panel.addComp(self, comp)

	def draw(self):
		pass

	def update(self):
		if not isinstance(self.layout, LinearLayout):
			self.layout = LinearLayout()

		self.height = 6
		if self.parent is None:
			self.width = 0
		for opt in self.children:
			self.height += opt.height + self.layout.spacing
			if self.parent is None:
				if opt.width > self.width:
					self.width = opt.width + self.layout.padding

		Panel.update(self)