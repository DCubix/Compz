# -*- coding: utf-8 -*-
from .layout_base import *


class GridLayout(LayoutBase):

	def __init__(self):
		super(GridLayout, self).__init__()
		self.padding = 4

		self.rows = 6
		self.columns = 2

	def getCellSize(self, width, height):
		return (width / self.columns, height / self.rows)

	def apply(self, comp):
		w, h = comp.parent.width, comp.parent.height
		cw, ch = self.getCellSize(w - self.padding * 2, h - self.padding * 2)
		csw = cw
		csh = ch

		if comp.columnSpan > 1 and comp.columnSpan <= self.columns:
			csw = cw * comp.columnSpan
		if comp.rowSpan > 1 and comp.rowSpan <= self.rows:
			csh = ch * comp.rowSpan

		cx = (cw * comp.column) + self.padding
		cy = (ch * comp.row) + self.padding

		comp.position = [cx + comp.margin[0], cy + comp.margin[1]]
		comp.width = csw - comp.margin[0] * 2
		comp.height = csh - comp.margin[1] * 2