# -*- coding: utf-8 -*-
from .component import *
from .checkbox import *
from .gfx import *
from .rect import *


class Radio(CheckBox):

	def __init__(self, text="CheckBox", style=None):
		super(Radio, self).__init__(text, style)
		self.group = None

	@property
	def type(self):
		return COMP_TYPE_RADIO

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
						if self.group is not None:
							if self.group.previous is not None:
								self.group.previous.selected = False
							self.selected = True
							self.group.previous = self
							self.group.selectedIndex = self.group.children.index(self)
							self.group.events.call(EV_PROPERTY_CHANGE, self.group)
						else:
							self.selected = not self.selected
						self.events.call(EV_MOUSE_CLICK, self)
				else:
					self.state = COMP_STATE_NORMAL
					self.events.call(EV_MOUSE_RELEASE, self)