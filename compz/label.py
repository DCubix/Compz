# -*- coding: utf-8 -*-
from .component import *
from .gfx import *


TEXT_ALIGN_LEFT = 0
TEXT_ALIGN_RIGHT = 1
TEXT_ALIGN_CENTER = 2


class Label(Component):

	def __init__(self, text="Label"):
		super(Label, self).__init__()

		self.text = text
		self.textAlignment = TEXT_ALIGN_LEFT
		self.height = 25

	def draw(self):
		if self.visible:
			gfx = self.system.gfx

			_, h = self.style.font.measure("E]")
			w, _ = self.style.font.measure(self.text)
			b = self.transformedBounds()

			if self.textAlignment == TEXT_ALIGN_LEFT:
				w2 = 2
			elif self.textAlignment == TEXT_ALIGN_RIGHT:
				w2 = b.width - w - 2
			else:
				w2 = b.width / 2 - w / 2

			h2 = b.height / 2 - h / 2

			glColor4f(*self.foreColor)
			gfx.clipBegin(b.x + 2, b.y + 2, b.width - 4, b.height - 4)
			self.style.font.draw(self.text, b.x + w2, b.y + h2)
			gfx.clipEnd()