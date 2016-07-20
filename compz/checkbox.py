# -*- coding: utf-8 -*-
from .component import *
from .gfx import *
from .rect import *


EV_CHECK_STATE_CHANGED = 8


class CheckBox(Component):

	def __init__(self, text="CheckBox", style=None):
		super(CheckBox, self).__init__(style)
		self._selected = False
		self.text = text
		self.height = 18
		self._sz = [16, 16]
		self.events.register(EV_CHECK_STATE_CHANGED)

	@property
	def selected(self):
		return self._selected

	@selected.setter
	def selected(self, v):
		if v != self._selected:
			self._selected = v
			self.events.call(EV_CHECK_STATE_CHANGED, self)

	def draw(self):
		if self.visible:
			valid = self.style is not None and \
				self.style.textures[COMP_STATE_NORMAL] is not None

			_, h = self.style.font.measure("E]")
			b = self.transformedBounds()
			if valid:
				o = self.style.offset
				s = self.style.size
				tex = self.style.textures[self.state]
				self.system.gfx.draw9Patch(b.x + 4,
											b.y + b.height / 2 - self._sz[1] / 2,
											self._sz[0], self._sz[1], o, s,
											t=tex)
				if self.selected:
					t = self.style.textures["custom"]
					self.system.gfx.drawQuad(b.x + 4,
										b.y + b.height / 2 - self._sz[1] / 2,
										self._sz[0], self._sz[1], texture=t)
			else:
				Component.draw(self)
				if self.selected:
					self.system.gfx.drawQuad(b.x + 4,
										b.y + b.height / 2 - self._sz[1] / 2,
										self._sz[0], self._sz[1],
										color=(0, 0, 0, 1))

			glColor4f(*self.foreColor)
			h2 = b.height / 2 - h / 2
			self.style.font.draw(self.text, b.x + self._sz[0] + 6, b.y + h2)

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
					self.state = COMP_STATE_CLICK

			if GFX_mouseRelease(events.LEFTMOUSE):
				if self.state == COMP_STATE_CLICK:
					if bounds.hasPoint(mx, my):
						self.state = COMP_STATE_HOVER
						self.selected = not self.selected
						self.events.call(EV_MOUSE_CLICK, self)
				else:
					self.state = COMP_STATE_NORMAL
					self.events.call(EV_MOUSE_RELEASE, self)