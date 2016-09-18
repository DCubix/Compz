# -*- coding: utf-8 -*-
from .component import *
from .rect import *
from .gfx import *


class List(Component):

	def __init__(self, style=None):
		super(List, self).__init__(style)
		self.items = []
		self.itemHeight = 18
		self.selectedIndex = -1
		self.__y = 0
		self.width = 100
		self.height = 120

	def draw(self):
		if not self.visible:
			return

		Component.draw(self)

		b = self.transformedBounds()

		if self.selectedIndex != -1:
			r = Rect(b.x + 1, self.__y, b.width - 2, self.itemHeight)
			t = self.style.skin
			reg = self.style.getTextureRegion(self.type, COMP_STATE_CUSTOM)

			o = self.style.offset
			self.system.gfx.draw9Patch(r.x, r.y, r.width, r.height, o, texture=t, uv=reg.data)

		fnt = self.style.font
		_, h = fnt.measure("E|]")
		centerY = self.itemHeight / 2 - h / 2

		glColor4f(*self.foreColor)
		self.system.gfx.clipBegin(b.x, b.y, b.width, b.height)
		yoff = b.y
		for item in self.items:
			text = str(item)
			w, _ = fnt.measure(text)
			if yoff + self.itemHeight > b.y + b.height:
				break
			fnt.draw(text, b.x + 6, yoff + centerY)
			yoff += self.itemHeight
		self.system.gfx.clipEnd()

	def event(self):
		if self.visible and self.enabled:
			bounds = self.transformedBounds()
			mx, my = GFX_mousePosition()
			if bounds.hasPoint(mx, my):
				if self.state == COMP_STATE_NORMAL:
					self.state = COMP_STATE_HOVER
					self.events.call(EV_MOUSE_ENTER, self)
			elif self.state == COMP_STATE_HOVER or \
					self.state == COMP_STATE_CLICK:
				self.state = COMP_STATE_NORMAL
				self.events.call(EV_MOUSE_LEAVE, self)

			if GFX_mouseClick(events.LEFTMOUSE):
				if self.state == COMP_STATE_HOVER:
					b = self.transformedBounds()
					yoff = b.y
					for i in range(len(self.items)):
						if yoff + self.itemHeight > b.y + b.height:
							break
						ir = Rect(b.x, yoff, b.width, self.itemHeight)
						if ir.hasPoint(mx, my):
							self.selectedIndex = i
							self.events.call(EV_PROPERTY_CHANGE, self)
							break
						yoff += self.itemHeight
					self.__y = yoff
					self.state = COMP_STATE_CLICK

			if GFX_mouseRelease(events.LEFTMOUSE):
				if self.state == COMP_STATE_CLICK:
					if bounds.hasPoint(mx, my):
						self.state = COMP_STATE_HOVER
						self.events.call(EV_MOUSE_CLICK, self)
				else:
					self.state = COMP_STATE_NORMAL
				self.events.call(EV_MOUSE_RELEASE, self)