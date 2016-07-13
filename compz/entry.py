# -*- coding: utf-8 -*-
from bge import events

from .event import *
from .component import *
from .gfx import *
from .timer import *


class Entry(Component):

	def __init__(self, text="", style=None):
		super(Entry, self).__init__(style)
		self.width = 120
		self.height = 25
		self.__text = text
		self.readOnly = False
		self.masked = False
		self.__blink = False
		self.__x = 0
		self.__t = Timer()

	@property
	def text(self):
		return self.__text

	@text.setter
	def text(self, v):
		self.__text = v
		if self.__x > len(v):
			self.__x = len(v)

	def draw(self):
		Component.draw(self)

		if self.visible:
			b = self.transformedBounds()
			_, h = self.style.font.measure("E]")
			h2 = b.height / 2 - h / 2

			glColor4f(*self.foreColor)
			offx = 0
			i = 0
			cx = 0
			for c in self.text:
				if not self.masked:
					cw, _ = self.style.font.measure(c)
					if i + 1 == self.__x:
						cx = offx + cw
					self.style.font.draw(c, b.x + 6 + offx, b.y + h2)
				else:
					cw, _ = self.style.font.measure("*")
					if i + 1 == self.__x:
						cx = offx + cw
					self.style.font.draw("*", b.x + 6 + offx, b.y + h2)
				offx += cw
				i += 1

			if self.state == COMP_STATE_CLICK and self.__blink:
				self.style.font.draw("|", b.x + 5 + cx, b.y + h2 - 2)

	def update(self):
		Component.update(self)
		if self.state == COMP_STATE_CLICK and not self.readOnly:
			self.__t.update()
			if self.__t.time >= 0.5:
				self.__blink = not self.__blink
				self.__t.reset()

	def event(self):
		if self.visible and self.enabled:
			bounds = self.transformedBounds()
			mx, my = GFX_mousePosition()
			if bounds.hasPoint(mx, my):
				if self.state == COMP_STATE_NORMAL:
					self.state = COMP_STATE_HOVER
					self.events.call(EV_MOUSE_ENTER, self)

			if GFX_mouseClick(events.LEFTMOUSE):
				if self.state == COMP_STATE_HOVER:
					self.state = COMP_STATE_CLICK
					self.events.call(EV_MOUSE_CLICK, self)
				elif self.state == COMP_STATE_CLICK and not bounds.hasPoint(mx, my):
					self.state = COMP_STATE_NORMAL
					self.events.call(EV_MOUSE_RELEASE, self)

			if self.__x > len(self.text):
				self.__x = len(self.text)
			if self.state == COMP_STATE_CLICK and not self.readOnly:
				shift = GFX_keyDown(events.LEFTSHIFTKEY) or \
						GFX_keyDown(events.RIGHTSHIFTKEY)
				if GFX_keyPressed(events.LEFTARROWKEY):
					if self.__x > 0:
						self.__x -= 1
					self.events.call(EV_KEY_PRESS, self,
						events.LEFTARROWKEY)
					self.__blink = True
				elif GFX_keyPressed(events.RIGHTARROWKEY):
					if self.__x < len(self.text):
						self.__x += 1
					self.events.call(EV_KEY_PRESS, self,
						events.RIGHTARROWKEY)
					self.__blink = True
				elif GFX_keyPressed(events.BACKSPACEKEY):
					if self.__x > 0:
						self.__x -= 1
						s = self.text
						self.text = s[:self.__x] + s[self.__x + 1:]
					self.events.call(EV_KEY_PRESS, self,
						events.BACKSPACEKEY)
					self.__blink = True
				elif GFX_keyPressed(events.DELKEY):
					if len(self.text[self.__x:]) != 0:
						s = self.text
						self.text = s[:self.__x] + s[self.__x + 1:]
					self.events.call(EV_KEY_PRESS, self,
						events.DELKEY)
					self.__blink = True
				else:
					for k, v in GFX_SupportedKeys.items():
						if GFX_keyPressed(v):
							key = events.EventToCharacter(v, shift)
							s = self.text
							self.text = s[:self.__x] + key + s[self.__x:]
							self.__x += 1
							self.__blink = True
							self.events.call(EV_KEY_PRESS, self, v)
							break