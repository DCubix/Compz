# -*- coding: utf-8 -*-
from .layout_base import *


ITEM_ORI_VERTICAL = 0
ITEM_ORI_HORIZONTAL = 1


class LinearLayout(LayoutBase):

	def __init__(self):
		super(LinearLayout, self).__init__()
		self.orientation = ITEM_ORI_VERTICAL
		self.__h = 0

	def init(self):
		self.__h = 0

	def apply(self, comp):
		width, height = comp.parent.width, comp.parent.height
		mw, mh = comp.margin
		if self.orientation == ITEM_ORI_VERTICAL:
			comp.width = (width - (self.padding * 2)) - mw * 2
			comp.position = [self.padding + mw, self.padding + self.__h]
			self.__h += comp.height + self.spacing
		else:
			comp.height = (height - (self.padding * 2)) - mh * 2
			comp.position = [self.padding + self.__h, self.padding + mh]
			self.__h += comp.width + self.spacing