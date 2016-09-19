# -*- coding: utf-8 -*-
from bge import events, render

from .point import *
from .rect import *
from .gfx import *
from .style import *
from .event import *


COMP_STATE_NORMAL = 0
COMP_STATE_CLICK = 1
COMP_STATE_HOVER = 2
COMP_STATE_INACTIVE = 3
COMP_STATE_CUSTOM = 4

COMP_TYPE_PANEL = 0
COMP_TYPE_BUTTON = 1
COMP_TYPE_CHECK = 2
COMP_TYPE_RADIO = 3
COMP_TYPE_ENTRY = 4
COMP_TYPE_SLIDER = 5


class Component:

	def __init__(self, style=None):
		self.id = 0
		self.bounds = Rect(0, 0, 100, 100)
		self.parent = None
		self.backColor = (0.6, 0.6, 0.6, 1)
		self.foreColor = (0.9, 0.9, 0.9, 1)
		self.system = None
		self.events = Event()
		self.name = ""

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
		self.columnSpan = 1
		self.rowSpan = 1
		self.margin = [0, 0]

		self.drawBackground = True
		self._prevTex = None

		self.finished = False

	@property
	def type(self):
		return COMP_TYPE_PANEL

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
			bounds = self.transformedBounds()
			mx, my = GFX_mousePosition()
			if bounds.hasPoint(mx, my):
				if GFX_mouseClick(events.LEFTMOUSE):
					if self.system.active is not None:
						self.system.active.state = COMP_STATE_NORMAL
					self.system.active = self
			else:
				if GFX_mouseClick(events.LEFTMOUSE):
					if self.system.active is not None:
						self.system.active.focused = False
						self.system.active = None

	def draw(self):
		if not self.drawBackground:
			return

		x, y = self.position.x, self.position.y
		w, h = self.bounds.width, self.bounds.height

		valid = self.style is not None

		if self.parent is not None:
			b = self.parent.transformedBounds()
			self.system.gfx.clipBegin(b.x, b.y, b.width, b.height)

		if valid:
			o = self.style.offset
			region = self.style.getTextureRegion(self.type, self.state)
			tex = self.style.skin
			self.system.gfx.draw9Patch(x, y, w, h, o, texture=tex, uv=region.data)
		else:
			print("Could NOT draw Component. You have to specify a Style")

	def endDraw(self):
		if self.parent is not None:
			self.system.gfx.clipEnd()
			self.finished = True
