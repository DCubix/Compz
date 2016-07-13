# -*- coding: utf-8 -*-
from bge import events, render

from .point import *
from .rect import *
from .gfx import *
from .style import *
from .event import *


COMP_STATE_NORMAL = "normal"
COMP_STATE_HOVER = "hover"
COMP_STATE_CLICK = "clicked"
COMP_STATE_INACTIVE = "inactive"


class Component:

	def __init__(self, style=None):
		self.index = 0
		self.bounds = Rect(0, 0, 100, 100)
		self.parent = None
		self.backColor = (0.6, 0.6, 0.6, 1)
		self.foreColor = (0.9, 0.9, 0.9, 1)
		self.system = None
		self.events = Event()

		self.state = COMP_STATE_NORMAL

		if style is not None:
			self.style = style
		else:
			self.style = Style()

		self.zorder = 99

		self.visible = True
		self.enabled = True
		self.focused = False

		self.row = 0
		self.column = 0
		self.margin = [0, 0]

		self.drawBackground = True

	@property
	def position(self):
		pos = self.getParentPosition()
		return Point(pos.x + self.bounds.x, pos.y + self.bounds.y)

	@position.setter
	def position(self, val):
		if isinstance(val, list):
			self.bounds.x, self.bounds.y = val
		else:
			self.bounds.x, self.bounds.y = val.x, val.y

	@property
	def x(self):
		return self.position.x

	@x.setter
	def x(self, v):
		self.position = [v, self.position.y]

	@property
	def y(self):
		return self.position.y

	@y.setter
	def y(self, v):
		self.position = [self.position.x, v]

	@property
	def width(self):
		return self.bounds.width

	@width.setter
	def width(self, v):
		self.bounds.width = v

	@property
	def height(self):
		return self.bounds.height

	@height.setter
	def height(self, v):
		self.bounds.height = v

	def transformedBounds(self):
		x, y = self.position.x, self.position.y
		w, h = self.bounds.width, self.bounds.height
		return Rect(x, y, w, h)

	def getParentPosition(self):
		pos = Point(0, 0)
		if self.parent is not None:
			pos.x = self.parent.position.x
			pos.y = self.parent.position.y
		return pos

	def centerOnScreen(self, vertical=True, horizontal=True):
		# Since self.parent has a layout, you can't do this.
		if self.parent is not None:
			return
		if horizontal:
			w = render.getWindowWidth()
			self.x = w / 2 - self.width / 2

		if vertical:
			h = render.getWindowHeight()
			self.y = h / 2 - self.height / 2

	def event(self):
		pass

	def update(self):
		if self.visible and self.enabled:
			pindex = self.parent.index if self.parent is not None else 1
			bounds = self.transformedBounds()
			mx, my = GFX_mousePosition()
			if bounds.hasPoint(mx, my):
				if GFX_mouseClick(events.LEFTMOUSE):
					if self.system.active is not None:
						self.system.active.state = COMP_STATE_NORMAL
						self.system.active.focused = False
						if hasattr(self.system.active, "layout"):
							self.system.active.zorder = 99 + pindex
						else:
							self.system.active.zorder = -99 + pindex
					self.system.active = self
					self.focused = True
					self.zorder = 99 + pindex
			else:
				if GFX_mouseClick(events.LEFTMOUSE):
					if self.system.active is not None:
						self.system.active.focused = False
						self.system.active = None

	def draw(self):
		if not self.drawBackground:
			return

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

		if valid:
			o = self.style.offset
			s = self.style.size
			tex = self.style.textures[self.state]
			self.system.gfx.draw9Patch(x, y, w, h, o, s, t=tex)
		else:
			gfx = self.system.gfx
			if self.state == COMP_STATE_NORMAL:
				gfx.drawQuad(x, y, w, h, color=self.backColor)
			elif self.state == COMP_STATE_HOVER:
				c = self.backColor
				gfx.drawQuad(x, y, w, h, color=(c[0] + 0.2, c[1] + 0.2,
												c[2] + 0.2, c[3]))
			elif self.state == COMP_STATE_CLICK:
				c = self.backColor
				gfx.drawQuad(x, y, w, h, color=(c[0] - 0.2, c[1] - 0.2,
												c[2] - 0.2, c[3]))
			elif self.state == COMP_STATE_INACTIVE:
				c = self.backColor
				gfx.drawQuad(x, y, w, h, color=(c[0] - 0.4, c[1] - 0.4,
												c[2] - 0.4, c[3]))
			gfx.drawWireQuad(x, y, w, h)

	def endDraw(self):
		if self.parent is not None:
			self.system.gfx.clipEnd()