# -*- coding: utf-8 -*-
from bge import events

from .component import *
from .rect import *
from .gfx import *
from .style import *
from .icon import *


class Button(Component):

	def __init__(self, text="Button", style=None):
		super(Button, self).__init__(style=style)
		self.text = text
		self.bounds = Rect(0, 0, 90, 25)
		self.icon = None

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
						self.events.call(EV_MOUSE_CLICK, self)
				else:
					self.state = COMP_STATE_NORMAL
					self.events.call(EV_MOUSE_RELEASE, self)

	def draw(self):
		Component.draw(self)

		if self.visible:
			_, h = self.style.font.measure("E]")
			w, _ = self.style.font.measure(self.text)
			b = self.transformedBounds()

			glColor4f(*self.foreColor)

			w2 = b.width / 2 - w / 2
			if self.icon is not None:
				tex = self.icon.texture
				iw, ih = self.icon.size

				w2 = iw + 12
				ix = b.x + 6
				if self.icon.alignment == ICON_ALIGN_CENTER:
					ix = b.x + b.width / 2 - iw / 2
				elif self.icon.alignment == ICON_ALIGN_RIGHT:
					ix = b.x + b.width - iw - 6
					w2 = 6

				self.system.gfx.drawQuad(ix, b.y + b.height / 2 - ih / 2,
											iw, ih, texture=tex)

			h2 = b.height / 2 - h / 2
			self.style.font.draw(self.text, b.x + w2, b.y + h2)
