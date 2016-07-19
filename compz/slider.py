# -*- coding: utf-8 -*-
from bge import events

from .component import *
from .rect import *
from .gfx import *


EV_SLIDER_VALUE_CHANGE = 7


class Slider(Component):

	def __init__(self, _min=0, _max=1, style=None):
		super(Slider, self).__init__(style)
		self.height = 24
		self.minimum = _min
		self.maximum = _max
		self._value = 0.5
		self._mx = 0
		self._track = Rect(0, 0, 1, 1)
		self.precision = 1

		self.events.register(EV_SLIDER_VALUE_CHANGE)

	@property
	def value(self):
		return self._value

	@value.setter
	def value(self, v):
		if self._value != v:
			self._value = round(v, self.precision)
			self.events.call(EV_SLIDER_VALUE_CHANGE, self)

	def draw(self):
		tex = None
		o = 4
		s = 16
		x, y = self.position.x, self.position.y
		w, h = self.bounds.width, self.bounds.height

		valid = self.style is not None and \
				self.style.textures[COMP_STATE_NORMAL] is not None

		if self.parent is not None:
			b = self.parent.transformedBounds()
			self.system.gfx.clipBegin(b.x, b.y, b.width, b.height)

		px = self._mx + x
		py = y + h / 2
		if valid:
			o = self.style.offset
			s = self.style.size
			track = self.style.textures["custom"]
			self.system.gfx.draw9Patch(self._track.x, self._track.y,
										self._track.width, self._track.height,
										o, s, t=track)

			pointer = self.style.textures[self.state]
			self.system.gfx.drawQuad(px - pointer.size[0] / 2,
									py - pointer.size[1] / 2,
									pointer.size[0], pointer.size[1],
									texture=pointer)
		else:
			gfx = self.system.gfx

			gfx.drawQuad(self._track.x, self._track.y,
						self._track.width, self._track.height,
						color=self.backColor)
			gfx.drawWireQuad(self._track.x, self._track.y,
						self._track.width, self._track.height)

			if self.state == COMP_STATE_NORMAL:
				gfx.drawQuad(px - 4, py - 8, 8, 16, color=self.backColor)
			elif self.state == COMP_STATE_HOVER:
				c = self.backColor
				gfx.drawQuad(px - 4, py - 8, 8, 16,
												color=(c[0] + 0.2, c[1] + 0.2,
												c[2] + 0.2, c[3]))
			elif self.state == COMP_STATE_CLICK:
				c = self.backColor
				gfx.drawQuad(px - 4, py - 8, 8, 16,
												color=(c[0] - 0.2, c[1] - 0.2,
												c[2] - 0.2, c[3]))
			elif self.state == COMP_STATE_INACTIVE:
				c = self.backColor
				gfx.drawQuad(px - 4, py - 8, 8, 16,
												color=(c[0] - 0.4, c[1] - 0.4,
												c[2] - 0.4, c[3]))
			gfx.drawWireQuad(px - 4, py - 8, 8, 16)

	def event(self):
		if self.visible and self.enabled:
			bounds = self.transformedBounds()
			mx, my = GFX_mousePosition()

			self._track = track = Rect(bounds.x + 8,
										bounds.y + bounds.height / 2 - 4,
										bounds.width - 16, 8)
			px = mx - track.x

			self._mx = abs(((self.minimum + self.value) * track.width) /
							((self.maximum - self.minimum) + 0.0001)) + 8

			if bounds.hasPoint(mx, my):
				if self.state == COMP_STATE_NORMAL:
					self.state = COMP_STATE_HOVER
					self.events.call(EV_MOUSE_ENTER, self)
			elif self.state == COMP_STATE_HOVER or \
					self.state == COMP_STATE_CLICK:
				self.state = COMP_STATE_NORMAL
				self.events.call(EV_MOUSE_LEAVE, self)

			if GFX_mouseDown(events.LEFTMOUSE):
				if self.state == COMP_STATE_HOVER:
					self.state = COMP_STATE_CLICK
					self.events.call(EV_MOUSE_CLICK, self)

			if GFX_mouseRelease(events.LEFTMOUSE):
				if self.state == COMP_STATE_CLICK:
					if bounds.hasPoint(mx, my):
						self.state = COMP_STATE_HOVER
					else:
						self.state = COMP_STATE_NORMAL
					self.events.call(EV_MOUSE_RELEASE, self)

			if self.state == COMP_STATE_CLICK:
				if px < 0:
					px = 0
				elif px > track.width:
					px = track.width
				v = px * abs(self.maximum - self.minimum) / track.width
				self.value = v