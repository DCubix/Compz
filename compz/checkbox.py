# -*- coding: utf-8 -*-
from .component import *
from .gfx import *
from .rect import *


class CheckBox(Component):

	def __init__(self, text="CheckBox", style=None):
		super(CheckBox, self).__init__(style)
		self._selected = False
		self.text = text
		self.height = 18
		self.check_size = [16, 16]

	@property
	def type(self):
		return COMP_TYPE_CHECK

	@property
	def selected(self):
		return self._selected

	@selected.setter
	def selected(self, v):
		if v != self._selected:
			self._selected = v
			self.events.call(EV_PROPERTY_CHANGE, self)

	def draw(self):
		if self.visible:
			valid = self.style is not None

			sw, sh = self.check_size
			_, h = self.style.font.measure("E|]")
			b = self.transformedBounds()
			if valid:
				y = b.y + b.height / 2 - sh / 2
				o = self.style.offset
				region = self.style.getTextureRegion(self.type, self.state)
				tex = self.style.skin

				self.system.gfx.draw9Patch(b.x + 4, y, sw, sh, o,
											texture=tex, uv=region.data)
				if self.selected:
					check_region = self.style.getTextureRegion(self.type, COMP_STATE_CUSTOM)
					self.system.gfx.drawQuadUV(b.x + 4, y, sw, sh,
												texture=tex, uv=check_region.data)
			else:
				print("Could NOT draw CheckBox. You have to specify a Style")

			glColor4f(*self.foreColor)
			h2 = b.height / 2 - h / 2
			self.style.font.draw(self.text, b.x + sw + 6, b.y + h2)

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