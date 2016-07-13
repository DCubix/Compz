# -*- coding: utf-8 -*-
EV_MOUSE_CLICK = 0
EV_MOUSE_RELEASE = 1
EV_MOUSE_ENTER = 2
EV_MOUSE_LEAVE = 3
EV_KEY_PRESS = 4
EV_KEY_RELEASE = 5
EV_KEY_DOWN = 6


class Event:

	def __init__(self):
		self.events = {
			EV_MOUSE_CLICK: None,
			EV_MOUSE_RELEASE: None,
			EV_MOUSE_ENTER: None,
			EV_MOUSE_LEAVE: None,
			EV_KEY_PRESS: None,
			EV_KEY_RELEASE: None,
			EV_KEY_DOWN: None
		}

	def set(self, event, callback):
		self.events[event] = callback

	def call(self, event, *args):
		evt = self.events[event]
		if evt is not None:
			evt(*args)