# -*- coding: utf-8 -*-
from .component import *
from .gfx import *
from math import sin, cos, radians, sqrt, atan2, pi
import colorsys as csys


class ColorPicker(Component):

	def __init__(self, style=None):
		super(ColorPicker, self).__init__(style)
		self._value = 1.0
		self._hue = 0.0
		self._saturation = 0.0
		self._color = (0, 0, 0)
		self.__cursor = [0, 0]
		self.__center = [0, 0]

	def __draw_circle_wire__(self, radius, steps=24):
		glColor3f(0, 0, 0)
		glBegin(GL_LINE_LOOP)

		_s = int(360 / steps)

		for angle in range(0, 360 + _s, _s):
			glVertex2f(int(cos(radians(angle)) * radius), int(sin(radians(angle)) * radius))
		glEnd()

	def __draw_semi_circle__(self, radius, steps=24):
		v = self._value

		glBegin(GL_TRIANGLE_FAN)
		glColor3f(v, v, v)
		glVertex2f(0, 0)

		_s = int(360 / steps)

		for angle in range(0, 360 + _s, _s):
			r, g, b = csys.hsv_to_rgb(angle / 360, 1.0, 1.0)
			glColor3f(r * v, g * v, b * v)
			glVertex2f(int(cos(radians(angle)) * radius), int(sin(radians(angle)) * radius))
		glEnd()

	def __draw_cursor__(self, x, y, s=7):
		glEnable(GL_BLEND)
		glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
		glColor3f(0.1, 0.1, 0.1)
		glPointSize(s)
		glBegin(GL_POINTS)
		glVertex2f(x, y)
		glEnd()
		glColor3f(0.9, 0.9, 0.9)
		glPointSize(s - 2)
		glBegin(GL_POINTS)
		glVertex2f(x, y)
		glEnd()
		glDisable(GL_BLEND)

	def __update_color__(self):
		r, g, b = csys.hsv_to_rgb(self._hue, self._saturation, self._value)
		self._color = (r, g, b)
		self.events.call(EV_PROPERTY_CHANGE, self)

	def __update_cursor__(self, mx, my):
		dx = mx - self.__center[0]
		dy = my - self.__center[1]
		angle = atan2(dy, dx)
		d = sqrt(dx * dx + dy * dy)
		radius = (min(self.width, self.height) / 2) - 4

		if d > radius:
			d = radius

		self.__cursor[0] = cos(angle) * d
		self.__cursor[1] = sin(angle) * d

		a = angle * 180 / pi
		if  angle < 0:
			a += 360

		self._hue = a / 360
		self._saturation = d / radius

		self.__update_color__()

	def __update_cursor_from_values__(self):
		_hue = self._hue * 360
		_hue = _hue * pi / 180
		radius = (min(self.width, self.height) / 2) - 4
		d = self._saturation * radius
		self.__cursor[0] = cos(_hue) * d
		self.__cursor[1] = sin(_hue) * d

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
					self.__update_cursor__(mx, my)
					self.events.call(EV_MOUSE_CLICK, self)

			if GFX_mouseDown(events.LEFTMOUSE):
				if self.state == COMP_STATE_HOVER or \
					self.state == COMP_STATE_CLICK:
					self.__update_cursor__(mx, my)

			if GFX_mouseRelease(events.LEFTMOUSE):
				if self.state == COMP_STATE_CLICK:
					if bounds.hasPoint(mx, my):
						self.state = COMP_STATE_HOVER
				else:
					self.state = COMP_STATE_NORMAL
				self.events.call(EV_MOUSE_RELEASE, self)

	def draw(self):
		Component.draw(self)
		b = self.transformedBounds()

		radius = (min(b.width, b.height) / 2) - 4
		x = self.x + b.width / 2
		y = self.y + b.height / 2
		self.__center = [x, y]
		cx = self.__cursor[0] + x
		cy = self.__cursor[1] + y

		glPushMatrix()
		glTranslatef(x, y, 0)
		self.__draw_semi_circle__(radius)
		self.__draw_circle_wire__(radius)
		glPopMatrix()

		self.__draw_cursor__(cx, cy)

		r, g, b = self._color
		glEnable(GL_BLEND)
		glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
		glColor3f(r, g, b)
		glPointSize(12)
		glBegin(GL_POINTS)
		glVertex2f(self.x + 12, self.y + 12)
		glEnd()
		glDisable(GL_BLEND)

		self.system.gfx.clipEnd()

	@property
	def color(self):
		return self._color

	@color.setter
	def color(self, c):
		self._color = c
		self._hue, self._saturation, self._value = \
								csys.rgb_to_hsv(c[0], c[1], c[2])
		self.__update_color__()
		self.__update_cursor_from_values__()

	@property
	def value(self):
		return self._value

	@value.setter
	def value(self, v):
		self._value = v
		self.__update_color__()

	@property
	def hue(self):
		return self._hue

	@hue.setter
	def hue(self, v):
		self._hue = v
		self.__update_color__()
		self.__update_cursor_from_values__()

	@property
	def saturation(self):
		return self._saturation

	@saturation.setter
	def saturation(self, v):
		self._saturation = v
		self.__update_color__()
		self.__update_cursor_from_values__()