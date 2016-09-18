# -*- coding: utf-8 -*-
from bge import events

from .component import *
from .rect import *
from .gfx import *


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
		self.pointer_size = [16, 16]

	@property
	def type(self):
		return COMP_TYPE_SLIDER

	@property
	def value(self):
		return self._value

	@value.setter
	def value(self, v):
		if self._value != v:
			self._value = round(v, self.precision)
			self.events.call(EV_PROPERTY_CHANGE, self)

	def draw(self):
		x, y = self.position.x, self.position.y
		w, h = self.bounds.width, self.bounds.height

		valid = self.style is not None

		if self.parent is not None:
			b = self.parent.transformedBounds()
			self.system.gfx.clipBegin(b.x, b.y, b.width, b.height)

		px = self._mx + x
		py = y + h / 2
		gfx = self.system.gfx
		if valid:
			o = self.style.offset
			tex = self.style.skin
			region = self.style.getTextureRegion(self.type, self.state)
			trackregion = self.style.getTextureRegion(self.type, COMP_STATE_CUSTOM)
			gfx.draw9Patch(self._track.x, self._track.y,
							self._track.width, self._track.height,
							o, texture=tex, uv=trackregion.data)

			pw, ph = self.pointer_size
			gfx.drawQuadUV(px - pw / 2, py - ph / 2, pw, ph, texture=tex, uv=region.data)
		else:
			print("Could NOT draw Component. You have to specify a Style")

	def event(self):
		if self.visible and self.enabled:
			bounds = self.transformedBounds()
			mx, my = GFX_mousePosition()
			hpw = self.pointer_size[0] / 2

			self._track = track = Rect(bounds.x + hpw,
										bounds.y + bounds.height / 2 - hpw / 2,
										bounds.width - self.pointer_size[0], hpw)
			px = mx - track.x

			self._mx = abs(((self.minimum + self.value) * track.width) /
							((self.maximum - self.minimum) + 0.0001)) + hpw

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